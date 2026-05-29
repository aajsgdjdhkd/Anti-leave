import os
from pathlib import Path
from rbxfile import Model, create_place
from rbxfile.types import SharedString

service_src = Path("add.Service").read_text(encoding="utf-8")
client_src  = Path("anit.Client").read_text(encoding="utf-8")

place = create_place()

server_script = Model(properties={
    "ClassName": "Script",
    "Name": "AntiLeaveService",
    "Source": SharedString(service_src)
})
place["ServerScriptService"].add_child(server_script)

if "StarterPlayer" not in place:
    starter_player = Model(properties={"ClassName": "StarterPlayer"})
    place.add_child(starter_player)
else:
    starter_player = place["StarterPlayer"]

if "StarterPlayerScripts" not in starter_player:
    sp_scripts = Model(properties={"ClassName": "StarterPlayerScripts"})
    starter_player.add_child(sp_scripts)
else:
    sp_scripts = starter_player["StarterPlayerScripts"]

client_script = Model(properties={
    "ClassName": "LocalScript",
    "Name": "AntiLeaveClient",
    "Source": SharedString(client_src)
})
sp_scripts.add_child(client_script)

place.save("Anti-leave.rbxl")
print("✅ 已生成 Anti-leave.rbxl")

import os
from pathlib import Path
from rbxfile import Model, create_place
from rbxfile.types import SharedString

# 读取脚本
client_src = Path("anit.Client").read_text(encoding="utf-8")

# 创建一个临时的 Place，在里面放 LocalScript，然后再整体保存？
# 更简单：直接创建一个 LocalScript 对象并保存为 .rbxm 文件
# 但 rbxfile 目前不支持单独保存 Model，只能通过 Place 来间接生成。

# 创建一个空的 Place
place = create_place()

# 在 StarterPlayerScripts 中放入 LocalScript
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

local_script = Model(properties={
    "ClassName": "LocalScript",
    "Name": "AntiLeaveClient",
    "Source": SharedString(client_src)
})
sp_scripts.add_child(local_script)

# 保存整个 Place 为一个 .rbxl 文件（但我们想要的是 .rbxm 模型）
# 然而 Assets API 接受 .rbxl 吗？官方文档说支持。所以我们可以直接上传 .rbxl 作为模型。
place.save("AntiLeaveModel.rbxm")   # 实际上保存的还是 .rbxl 格式，但改后缀为 .rbxm 也能用
print("✅ 已生成 AntiLeaveModel.rbxm")

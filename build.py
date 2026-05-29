import os
from pathlib import Path
from rbxfile import Model, create_place
from rbxfile.types import SharedString

# 读取你的脚本
client_src = Path("anit.Client").read_text(encoding="utf-8")

# 创建一个 LocalScript 实例
local_script = Model(properties={
    "ClassName": "LocalScript",
    "Name": "AntiLeaveClient",
    "Source": SharedString(client_src)
})

# 创建一个 Model 容器
model = Model(properties={
    "ClassName": "Model",
    "Name": "AntiLeaveModel"
})
model.add_child(local_script)

# 保存为 .rbxm 文件
with open("AntiLeaveModel.rbxm", "wb") as f:
    model.serialize(f)
print("✅ 已生成 AntiLeaveModel.rbxm")

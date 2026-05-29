import sys
import os
from pathlib import Path

try:
    from rbxfile import Model, create_place
    from rbxfile.types import SharedString
except ImportError as e:
    print(f"导入 rbxfile 失败: {e}")
    sys.exit(1)

try:
    # 读取脚本
    client_src = Path("anit.Client").read_text(encoding="utf-8")
    print(f"成功读取 anit.Client，长度: {len(client_src)} 字符")
    
    # 创建 place
    place = create_place()
    print("成功创建 place")
    
    # 确保 StarterPlayer 存在
    if "StarterPlayer" not in place:
        starter_player = Model(properties={"ClassName": "StarterPlayer"})
        place.add_child(starter_player)
        print("创建 StarterPlayer")
    else:
        starter_player = place["StarterPlayer"]
    
    # 确保 StarterPlayerScripts 存在
    if "StarterPlayerScripts" not in starter_player:
        sp_scripts = Model(properties={"ClassName": "StarterPlayerScripts"})
        starter_player.add_child(sp_scripts)
        print("创建 StarterPlayerScripts")
    else:
        sp_scripts = starter_player["StarterPlayerScripts"]
    
    # 创建 LocalScript
    local_script = Model(properties={
        "ClassName": "LocalScript",
        "Name": "AntiLeaveClient",
        "Source": SharedString(client_src)
    })
    sp_scripts.add_child(local_script)
    print("已添加 LocalScript")
    
    # 保存文件
    place.save("AntiLeaveModel.rbxm")
    print("✅ 已生成 AntiLeaveModel.rbxm")
    
except Exception as e:
    print(f"❌ 构建失败: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

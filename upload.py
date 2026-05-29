import os
import sys
import requests

API_KEY = os.environ.get("RBXCLOUD_API_KEY")
if not API_KEY:
    print("❌ 错误: 未找到 RBXCLOUD_API_KEY 环境变量")
    sys.exit(1)

print(f"API Key 存在，长度: {len(API_KEY)}")

FILE_PATH = "AntiLeaveModel.rbxm"
if not os.path.exists(FILE_PATH):
    print(f"❌ 错误: 文件 {FILE_PATH} 不存在")
    sys.exit(1)

print(f"文件大小: {os.path.getsize(FILE_PATH)} 字节")

ASSET_TYPE = "Model"
ASSET_NAME = "AntiLeaveModel"
ASSET_DESCRIPTION = "防离开脚本模型"

url = f"https://apis.roblox.com/assets/v1/assets?assetType={ASSET_TYPE}&displayName={ASSET_NAME}&description={ASSET_DESCRIPTION}"

headers = {
    "x-api-key": API_KEY,
    "Content-Type": "application/octet-stream"
}

try:
    with open(FILE_PATH, "rb") as f:
        print("正在上传...")
        response = requests.post(url, headers=headers, data=f)
    
    print(f"HTTP 状态码: {response.status_code}")
    
    if response.status_code == 200 or response.status_code == 201:
        data = response.json()
        asset_id = data.get("assetId")
        print(f"🎉 上传成功！Asset ID: {asset_id}")
        print(f"你可以在游戏中使用: rbxassetid://{asset_id}")
    else:
        print(f"❌ 上传失败: {response.status_code}")
        print(f"响应内容: {response.text}")
        
except Exception as e:
    print(f"❌ 请求异常: {e}")
    sys.exit(1)

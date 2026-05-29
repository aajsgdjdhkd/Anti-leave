import os
import requests

API_KEY = os.environ["RBXCLOUD_API_KEY"]
FILE_PATH = "AntiLeaveModel.rbxm"
ASSET_TYPE = "Model"
ASSET_NAME = "AntiLeaveModel"
ASSET_DESCRIPTION = "防离开脚本模型，插入后即可自动生效"

url = f"https://apis.roblox.com/assets/v1/assets?assetType={ASSET_TYPE}&displayName={ASSET_NAME}&description={ASSET_DESCRIPTION}"

headers = {
    "x-api-key": API_KEY,
    "Content-Type": "application/octet-stream"
}

with open(FILE_PATH, "rb") as f:
    response = requests.post(url, headers=headers, data=f)

if response.status_code == 200 or response.status_code == 201:
    data = response.json()
    asset_id = data.get("assetId")
    print(f"🎉 上传成功！Asset ID: {asset_id}")
    print(f"你可以在游戏中使用: rbxassetid://{asset_id}")
else:
    print(f"❌ 上传失败: {response.status_code}")
    print(response.text)

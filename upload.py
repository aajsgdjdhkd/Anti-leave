import os
import rblx_opencloud

API_KEY = os.environ["RBXCLOUD_API_KEY"]
UNIVERSE_ID = os.environ["UNIVERSE_ID"]
PLACE_ID = os.environ["PLACE_ID"]

rblx_opencloud.api_key = API_KEY
publisher = rblx_opencloud.PlacePublishing(universe=UNIVERSE_ID)

with open("Anti-leave.rbxl", "rb") as f:
    version = publisher.publishPlace(PLACE_ID, f)

print(f"🚀 上传成功！版本: {version}")

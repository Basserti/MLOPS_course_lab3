import requests
import json
from pyyoutube import Api
import os

import mlflow
from mlflow.tracking import MlflowClient

os.environ["MLFLOW_REGISTRY_URI"] = "/home/user/mlflow/"
mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("get_data_yt")

key = "AIzaSyA_7tgQEXwxYiHkbx9rqyZwuooVWkVMbnI"
api = Api(api_key=key)

query = "'MrBeast'"
video = api.search_by_keywords(q=query, search_type=["videos"], count=100, limit=30)

channelId = video.items[0].id.channelId

videos = []
for i in video.items:
    if i.id.kind != 'youtube#channel':
        videos.append(i.id.videoId)

view_counts = []

with mlflow.start_run():
    url = 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId='+channelId+'&maxResults=50&type=video&key='+key
    videos = []
    for i in video.items:
        if i.id.kind != 'youtube#channel':
            videos.append(i.id.videoId)
    view_counts = []
    for videoId in videos:
        url_data = 'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id='+videoId+'&key='+key
        content = requests.get(url_data).text
        data = json.loads(content)
        for i in data['items']:
            if i['kind'] == 'youtube#video':
                view_counts.append(i['statistics']['viewCount'])
    mlflow.log_artifact(local_path="/home/user/Lab3_project/scripts/get_data.py",
                        artifact_path="get_data code")
    mlflow.end_run()
print(view_counts)
with open('/home/user/Lab3_project/datasets/data.csv', 'w') as f:
    s = ''
    for i in view_counts:
        s = s + str(i) + '\n'
    f.write(s)



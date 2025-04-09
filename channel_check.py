import requests
from config import API_KEY, CHANNEL_ID
from log_config import get_logger

logger = get_logger("channel_check")

logger.info("Testing: channel_check.py")

url = "https://www.googleapis.com/youtube/v3/search"
params = {
    "part": "snippet",
    "channelId": CHANNEL_ID,
    "order": "date",
    "maxResults": 1,
    "type": "video",
    "key": API_KEY
}

response = requests.get(url, params=params)
data = response.json()

if data.get("items"):
    video = data["items"][0]
    title = video["snippet"]["title"]
    published = video["snippet"]["publishedAt"]
    video_id = video["id"]["videoId"]
    video_url = f"https://www.youtube.com/watch?v={video_id}"

    print(f"🎬 Most recent video: {title}")
    print(f"🕒 Published at: {published}")
    print(f"🔗 Watch: {video_url}")
else:
    print("No videos found — check your channel ID.")

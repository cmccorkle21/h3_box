import requests
from config import API_KEY, CHANNEL_ID

def get_upcoming_video_id():
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "channelId": CHANNEL_ID,
        "eventType": "upcoming",
        "type": "video",
        "order": "date",
        "maxResults": 1,
        "key": API_KEY
    }
    resp = requests.get(url, params=params).json()
    items = resp.get("items", [])
    if not items:
        return None
    return items[0]["id"]["videoId"]

def get_video_schedule_info(video_id):
    url = "https://www.googleapis.com/youtube/v3/videos"
    params = {
        "part": "liveStreamingDetails",
        "id": video_id,
        "key": API_KEY
    }
    resp = requests.get(url, params=params).json()
    items = resp.get("items", [])
    if not items:
        return None
    details = items[0].get("liveStreamingDetails", {})
    return {
        "scheduledStartTime": details.get("scheduledStartTime"),
        "actualStartTime": details.get("actualStartTime"),
        "videoId": video_id
    }

def get_live_stream():
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "channelId": CHANNEL_ID,
        "eventType": "live",
        "type": "video",
        "key": API_KEY
    }
    r = requests.get(url, params=params).json()
    if r.get("items"):
        return r["items"][0]["id"]["videoId"]
    return None
from youtube_utils import get_live_stream
from state import load_state, save_state
from launcher import launch_youtube_stream
from datetime import datetime, timedelta
from log_config import get_logger

logger = get_logger("check_if_live")

logger.info("Checking if H3 is live...")
print("Checking if H3 is live...")
state = load_state()
today = datetime.now().date().isoformat()
#first run of the day logic
if state["date"] != today:
    state = {
        "date": today,
        "live_check_count": 0,
        "stream_triggered_at": None,
        "last_scheduled_video_id": None
    }

if state["stream_triggered_at"]:
    if datetime.fromisoformat(state["stream_triggered_at"]) + timedelta(hours=3) > datetime.now():
        print("Stream already triggered within the last 3 hours.")
        logger.info("Stream already triggered within the last 3 hours.")
        exit(0)

if state["live_check_count"] >= 100:
    exit(0)

video_id = get_live_stream()
state["live_check_count"] += 1

if video_id:
    logger.info(f"Current live detected: {video_id}")
    print("Current live detected: " + video_id)
    launch_youtube_stream(video_id)
    state["stream_triggered_at"] = datetime.now().isoformat()
else:
    print("Current time: " + datetime.now().isoformat())
    print("No live stream detected.")
    logger.info("No live stream detected.")

save_state(state)
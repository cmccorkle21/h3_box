from youtube_utils import get_upcoming_video_id, get_video_schedule_info
from launcher import launch_youtube_stream
from state import load_state, save_state
from datetime import datetime, timedelta
from log_config import get_logger

logger = get_logger("check_scheduled")

state = load_state()

print("Checking for scheduled stream...")

if state.get("stream_triggered_at"):
    if datetime.fromisoformat(state["stream_triggered_at"]) + timedelta(hours=3) > datetime.now():
        exit(0)

video_id = get_upcoming_video_id()
if not video_id or video_id == state.get("last_scheduled_video_id"):
    exit(0)

info = get_video_schedule_info(video_id)
scheduled_time = info.get("scheduledStartTime")

if scheduled_time:
    scheduled_dt = datetime.fromisoformat(scheduled_time.replace("Z", "+00:00"))
    now = datetime.utcnow()

    if (scheduled_dt - now).total_seconds() < 900:
        logger.info(f"Upcoming video scheduled: {video_id} at {scheduled_time}")
        print(f"Upcoming video scheduled: {video_id} at {scheduled_time}")
        launch_youtube_stream(video_id)
        state["stream_triggered_at"] = datetime.now().isoformat()
        state["last_scheduled_video_id"] = video_id

save_state(state)
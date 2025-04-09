from youtube_utils import get_upcoming_video_id, get_video_schedule_info, get_live_stream

print("Checking for upcoming stream...")
upcoming_id = get_upcoming_video_id()
print("Upcoming video ID:", upcoming_id)

if upcoming_id:
    info = get_video_schedule_info(upcoming_id)
    print("Scheduled Start:", info.get("scheduledStartTime"))
    print("Actual Start:", info.get("actualStartTime"))

print("\nChecking for currently live stream...")
live_id = get_live_stream()
print("Live video ID:", live_id)
import subprocess
from config import ONN_IP, ADB_PORT
from log_config import get_logger

def launch_youtube_stream(video_id):
    youtube_url = f"https://www.youtube.com/watch?v={video_id}"
    adb_cmds = [
        f"adb connect {ONN_IP}:{ADB_PORT}",
        "adb shell input keyevent KEYCODE_WAKEUP",
        f'adb shell am start -a android.intent.action.VIEW -d "{youtube_url}"'
    ]
    for cmd in adb_cmds:
        subprocess.run(cmd, shell=True)
    logger.info(f"Launching YouTube stream on Onn: {youtube_url}")
    print(f"Launching YouTube stream on Onn: {youtube_url}")
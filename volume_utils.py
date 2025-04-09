import subprocess
import time

MAX_VOLUME = 25  # Adjust if you discover it’s different on your Onn TV

def adb_keyevent(code: int):
    subprocess.run(["adb", "shell", "input", "keyevent", str(code)], check=True)

def volume_up(times=1):
    for _ in range(times):
        adb_keyevent(24)
        time.sleep(0.1)  # allow volume OSD to keep up

def volume_down(times=1):
    for _ in range(times):
        adb_keyevent(25)
        time.sleep(0.1)

def set_volume(level: int):
    """
    Set media volume to a specific level (0–MAX_VOLUME).
    This is a brute-force approach that always works.
    """
    if not (0 <= level <= MAX_VOLUME):
        raise ValueError("Volume must be between 0 and MAX_VOLUME")

    volume_down(MAX_VOLUME)  # reset to 0
    time.sleep(0.2)
    volume_up(level)

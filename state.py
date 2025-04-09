import json
from pathlib import Path

STATE_FILE = Path("/home/admin/h3_box/h3_state.json")

def load_state():
    if not STATE_FILE.exists():
        return {
            "date": "1970-01-01",
            "live_check_count": 0,
            "stream_triggered_at": None,
            "last_scheduled_video_id": None
        }
    with open(STATE_FILE) as f:
        return json.load(f)

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)
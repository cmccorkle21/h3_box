from state import load_state, save_state
from datetime import datetime

print("Loading current state...")
state = load_state()
print(state)

print("Modifying state and saving...")
state["test_run"] = datetime.now().isoformat()
save_state(state)

print("Reloading to confirm...")
print(load_state())
#!/bin/bash

# Activate venv
source /home/admin/h3_box/venv/bin/activate

# Move to project directory
cd /home/admin/h3_box

# Run the script and log
python3 check_scheduled.py >> logs/cron_h3box.log 2>&1

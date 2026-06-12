# Automated NAV Update Scheduler

## Objective

Automatically fetch latest NAV data and update the mutual fund database every weekday at 8 PM.

## Linux Cron Job

```bash
0 20 * * 1-5 /usr/bin/python3 scripts/live_nav_fetch.py
```

Meaning:

* Minute: 0
* Hour: 20 (8 PM)
* Days: Monday to Friday

## Windows Task Scheduler

Task Name:
NAV Auto Update

Trigger:
Daily at 8:00 PM

Action:
python scripts/live_nav_fetch.py

## Expected Workflow

1. Fetch latest NAV data from MF API
2. Save updated NAV CSV files
3. Update SQLite database
4. Generate log file

## Output

Example log:

2026-06-12 20:00:01
5 schemes fetched
Database updated successfully

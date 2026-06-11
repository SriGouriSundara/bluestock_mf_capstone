# scripts/run_pipeline.py

import subprocess
import sys

scripts = [
    "scripts/etl_pipeline.py",
    "scripts/live_nav_fetch.py",
    "scripts/load_sqlite.py",
    "scripts/verify_database.py"
]

for script in scripts:
    print(f"\nRunning {script} ...")

    result = subprocess.run([sys.executable, script])

    if result.returncode != 0:
        print(f"Error while running {script}")
        sys.exit(1)

print("\nProject Pipeline Completed Successfully!")
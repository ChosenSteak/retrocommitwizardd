import os
import subprocess
from datetime import datetime, timedelta
import random

def make_commit_on_date(date_str: str, message: str = "Retro commit"):
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str

    with open("log.txt", "a") as log:
        log.write(f"[{date_str}] {message}\n")

    subprocess.run(["git", "add", "."], env=env)
    subprocess.run(["git", "commit", "-m", message], env=env)

def generate_dates(start_date, end_date, count):
    days_range = (end_date - start_date).days
    return sorted([
        start_date + timedelta(days=random.randint(0, days_range))
        for _ in range(count)
    ])

if __name__ == "__main__":
    start = datetime(2024, 6, 1)
    end = datetime(2024, 7, 1)
    dates = generate_dates(start, end, 10)

    for d in dates:
        date_str = d.strftime("%Y-%m-%dT12:00:00")
        make_commit_on_date(date_str, "Добавлен ретро-коммит")

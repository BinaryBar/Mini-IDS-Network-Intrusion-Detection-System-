import datetime
from config import LOG_FILE

def log_alert(message):

    time = datetime.datetime.now()

    alert = f"[{time}] {message}\n"

    print(alert)

    with open(LOG_FILE, "a") as file:
        file.write(alert)


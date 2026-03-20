#!usr/bin/env python3

import json
import time
import requests

#splunk HEC Configuration

SPLUNK_HEC_URL="http://localhost:8088/services/collector"
SPLUNK_HEC_TOKEN="4c62b108-30d2-40a5-9020-aec2d4"

HEADERS = {
    "Authorization":f"Splunk {SPLUNK_HEC_TOKEN}","Content-Type":"application/json"
}


def send_log(event_data):
    payload= json.dumps({      #--> to convert into a json string
        "event":event_data,
        "sourcetype":"json",
        "index":"main"
    })

try:
    res = requests.posts(SPLUNK_HEC_URL,headers=HEADERS,data=payload)
    if res.status_code == 200:
        print(f"Log event details: {event_data}")
    else:
        print(f"Failed to send logs : {res.text}")
except Exception as e:
    print(f" Error: {e}")


if __name__ == "__main__":
    c=1
    while True:
        log_event = {
            "message": f"Devops Test log{count}",
            "level":"medium",
            "service":"Devops",
            "timestamp":time.strftime("%Y-%m-%d %H: %M:%S")
        }

        send_log(log_event)

        c+=1
        time.sleep(2)














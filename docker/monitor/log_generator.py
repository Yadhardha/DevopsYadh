import time
import random
log_file = "/tmp/devops.log"
paths=["/","/login","/dashboard","/api/data"]
while True:
    log=f'127.0.0.1 --"GET {random.choice(paths)} HTTP/1.1" 200\n'
    with open(log_file,"a") as f:
        f.write(log)
    time.sleep(1)

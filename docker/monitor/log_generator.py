import time,random

f = open("/tmp/devops.log","a")

paths=["/","/login","/dashboard","/api/data"]
while True:
    f.write(f'127.0.0.1 --[] "GET {random.choice(paths)} HTTP/1.1" 200\n')
    f.flush()
    time.sleep(2)

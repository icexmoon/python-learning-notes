from threading import Thread
import time
def doSomething():
    time.sleep(5)

thread = Thread(target=doSomething)
thread.start()
print("end")
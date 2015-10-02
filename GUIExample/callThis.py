from time import sleep
exitFlag=0

class myThread (threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID


    def run(self):
        print("Starting")
        sleep(6)
        print("Exiting")
        exitFlag=1

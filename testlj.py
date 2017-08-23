import threading
import urllib

class myTherad(threading.Thread):
    def __init__(self, threadId, name):
        threading.Thread.__init__(self)
        self.threadID = threadId
        self.name = name

    def run(self):
        while True:
            print('threadId->%s', self.threadID)




for i in range(20):
    myTherad(str(i), "Thread-" + str(i)).start()

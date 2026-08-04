import threading
import time

r"""TODO: 
    create payment thread [X]
    create page loading thread [X]
    create sending email thread [X]
"""
# Creating a custom thread
class locked_thread(threading.Thread):
    """ Thread for payment """
    def __init__(self, name, delay):     
        threading.Thread.__init__(self)                         # Parents constructor
        self.name = name
        self.delay = delay
    
    def run(self):                                              # What the thread actually does
        print(f"Starting {self.name} thread...")
        lock.acquire()
        time.sleep(self.delay)                                  # Sleep for {delay} time
        print(f"{self.name} thread done processing at: {time.ctime(time.time())}\n")
        lock.release()

class lockless_threads(threading.Thread):
    """ Thread for anything but payment """
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        # Check if a lock is present
        print(f"Starting {self.name} Thread... ")
        lock.acquire()                                          # If lock is present do nothing and aquire it once done
        lock.release()                                          # Instantly leave afterwards
        self.print_stuff(self.name, self.delay)
        print(f"{self.name} thread finished execution...\n")
    
    def print_stuff(self, name, delay):
        for _ in range(0, delay):
            print(f"{name} thread: {time.ctime(time.time())}\n")
            time.sleep(1)

lock = threading.Lock()                                         

payment_thread = locked_thread("Payment", 5)                    # The threads name is payments and it will work for 5s
loading_page_thread = lockless_threads("Loading", 3)            # The threads name is loading and it will work for 3s
sending_email_thread = lockless_threads("Sending Email", 10)    # ...

payment_thread.start()
loading_page_thread.start()
sending_email_thread.start()

payment_thread.join()
loading_page_thread.join()
sending_email_thread.join()

print("Main thread exec finished!")


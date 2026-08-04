import threading
from context_managers import time_it
from program_to_multithread import get_length

# NOTE: Time taken previously was 4174ms or 4.1sec, this program however cuts that time to a fraction.

gists = ['https://gist.github.com/recluze/1d2989c7e345c8c3c542', 
        'https://gist.github.com/recluze/a98aa1804884ca3b3ad3', 
        'https://gist.github.com/recluze/5051735efe3fc189b90d', 
        'https://gist.github.com/recluze/460157afc6a7492555bb', 
        'https://gist.github.com/recluze/5051735efe3fc189b90d', 
        'https://gist.github.com/recluze/c9bc4130af995c36176d']

with time_it():
    threads = [] # List of all the threads we created
    for g in gists:
        # Create threads/workers
        t = threading.Thread(target=get_length, args=([g])) # Define what the target function to complete and its arguments are.
        # Start the threads
        t.start()
        threads.append(t)
    for t in threads:
        t.join() # Block the main thread until these threads finish
    print("Done!") 


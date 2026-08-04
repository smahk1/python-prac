from contextlib import contextmanager
import time

""" The with keyword is a commonly used context manager
    it handles the setup and after the processing it also 
    handles the cleanup which in this case is new_file.close() """
# with open('ideas.txt', 'r') as new_file:
#     for line in new_file:
#         print(line, end='')

""" We can ofcourse write custom context managers as well by doing the following: """
@contextmanager # Decorator used to make this a context manager
def time_it():
    start_time = int(round(time.time() * 1000))
    yield
    end_time = int(round(time.time() * 1000))
    print("\nTotal time: " + str(end_time - start_time) + "ms")

# def some_func(): # Randome function to exec
#     time.sleep(0.5)

# with time_it(): # Now we can use the with keyword to exec out custom CM.
#     some_func()


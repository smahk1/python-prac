import requests
from context_managers import time_it

""" Single thread program """ 

def get_length(g): 
        print(f"Requesting: {g}")
        data = requests.get(g)
        g_length = len(data.text)
        print(f"Length: {g_length}")

# with time_it():
#     get_length() # This took roughly 4 seconds on my device which is very slow



import tempfile
import shutil
import os
from contextlib import contextmanager

# Context manager that creates a temp dir to store temp data that we write and read from it
@contextmanager
def temp_dir():
    try: 
        name = tempfile.mkdtemp()
        print(f"Made tempdir: {name}")

        filename = os.path.join(name, "new_file.text") 

        with open(filename, 'w+') as file:
            yield file # giving use access to the file for writes and reads
    finally:
        print("Deleting temp dir...")
        shutil.rmtree(name) # Remove the dir and its contents

# Using the context manager
with temp_dir() as file:
    # File in dir is literally what we are yielding
    file.write("Some temp data")
    file.seek(0) # Reset the pointer
    for line in file:
        print(line) # Confirming if something was written or not.




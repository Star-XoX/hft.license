import subprocess

# Run the script in the background
subprocess.Popen(["python3", "script.py"])


print('after')


from time import sleep
while True:
    sleep(2222)
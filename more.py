import subprocess

# Run the script in the background
# subprocess.Popen(["python3", "script.py"])

# import subprocess

subprocess.Popen(["nohup", "python3", "script.py", ">", "child.log", "&"], start_new_session=True)


print('after')


from time import sleep
while True:
    sleep(2222)
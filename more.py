import subprocess
import os
# Run the script in the background
# subprocess.Popen(["python3", "script.py"])

# import subprocess

# subprocess.Popen(["nohup", "python3", "script.py", ">", "child.log", "&"], start_new_session=True)
os.system('nohup python3 -u ./script.py > ./out.script &')


print('after')


from time import sleep
while True:
    sleep(2222)
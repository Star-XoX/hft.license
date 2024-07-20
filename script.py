
import threading, signal
import os, sys, git
import subprocess
from time import sleep
from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route("/")
def hello():
    return '{"status": "nick was here"}'

def start_script():
    os.execv(sys.executable, ['python'] + sys.argv)

def update_from_repo():
    # repo = git.Repo('./')
    # repo.remotes.origin.pull()
    start_script()

def exit_after_response():
    update_from_repo()
    os.kill(os.getpid(), signal.SIGINT)



@app.route("/cmd", methods=["POST"])
def custom():
    cmd = request.get_json()["cmd"]
    try:
        output = subprocess.check_output(cmd, shell=True, text=True)
        return jsonify({"output": output})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e)})


@app.route("/restart")
def restart():
    threading.Thread(target=exit_after_response).start()
    return "working.."

if __name__ == "__main__":
    sleep(2)
    app.run(host='0.0.0.0', port = 80)
    # print(sys.executable)
    # print(sys.argv)
    # os.execv(sys.executable, ['python'] + sys.argv)
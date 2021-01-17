from watchdog.observers import observer
from watchdog.events import FileSystemEventHandler
# pip install watchdog for these packages to work

import os
import json
import time


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename


folder_to_track = "/Users/cmazv/OneDrive/Desktop/test1"
folder_destination = "/Users/cmazv/OneDrive/Desktop/newFolder"
event_handler = MyHandler()
observer = observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()

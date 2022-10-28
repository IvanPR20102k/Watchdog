import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os


class Handler(FileSystemEventHandler):
    def on_created(self, event):
        print("Создан файл:", event.src_path)
        vowels: str = "аеёиоуыэюяaeiouy"
        filepath: str = os.path.basename(event.src_path)
        filename: str = filepath[0:len(filepath)-4]
        for letter in filename:
            if letter in vowels:
                print(str(letter).lower())
            else:
                print(str(letter).upper())


event_handler = Handler()
observer = Observer()
observer.schedule(event_handler, path="./", recursive=True)
observer.start()
while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
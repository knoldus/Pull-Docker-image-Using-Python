import docker
import time
from itertools import cycle
from shutil import get_terminal_size
from threading import Thread


ending_string="..........These are the all images.........."

print(" We are going to listing all the images with id in your local system:--")


class Loader:

    def __init__(self, description="Loading...", end_point="Done!", time_out=0.2):

        self.desc = description
        self.end = end_point
        self.timeout = time_out

        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for i in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {i}", flush=True, end="")
            time.sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

    def __exit__(self, exc_type, exc_value, tb):
        self.stop()


docker_client_obj = docker.from_env()

image_name= input("enter the image name which you want to pull ")
docker_client_obj.images.pull(image_name)

image_list  = docker_client_obj.images.list()

for image in image_list:
     if __name__ == "__main__":
                with Loader("Loading for docker..."):
                    for i in range(3):
                        time.sleep(0.25)

                loader = Loader("Loading for images details...", "oohhh!!, That was too fast!", 0.05).start()
                for i in range(3):
                    time.sleep(0.25)

                loader.stop()

     print(image)
     print(image.tag)
     print(image.id)
     
print(ending_string.upper())
import random
import string
import time

#all_names = []

class Robot(object):
    global all_names
    all_names = []
    def generate_name(self):
        name = []
        random.seed(time.time())
        name.append(string.ascii_uppercase[random.randint(0,25)])
        name.append(string.ascii_uppercase[random.randint(0,25)])
        name.append(str(random.randint(0,9)))
        name.append(str(random.randint(0,9)))
        name.append(str(random.randint(0,9)))
        return ''.join(name)

    def __init__(self):
        print(all_names)
        self.name = self.generate_name()
        while self.name in all_names:
            self.name = self.generate_name()
        all_names.append(self.name)

    def reset(self):
        all_names.remove(self.name)
        self.__init__()

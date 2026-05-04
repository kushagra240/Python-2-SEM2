class Writer:
    def write(self):
        print("Writing")


class Speaker:
    def speak(self):
        print("Speaking")


class Author(Writer, Speaker):
    pass


author = Author()
author.write()
author.speak()

import os.path

class FileReader:
    def __init__(self, filename):
        self._fname = filename
        self.content = ""
        try:
            if not os.path.exists(self._fname):
                raise IOError
            with open(self._fname) as f:
                self.content = f.readlines()
        except IOError as err:
            self.content = ""
        finally:
            self.content = "".join(self.content)


    def read(self):
        return self.content


reader1 = FileReader("example.txt")
print("Result:", reader1.read())

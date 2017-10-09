import tempfile
import os.path

class File:
    def __init__(self, fname):
        f = {}
        try:
            self.fname = fname
            self.f = open(fname, "r")
            self.content = self.f.readlines()
            self.f.close()
        except FileNotFoundError:
            self.f = {"name": None}
            self.content = []



    def __add__(self, obj):
        fn1 = os.path.splitext(os.path.split(self.f.name)[1])[0]
        (fn2, ext) = os.path.splitext(os.path.split(obj.f.name)[1])
        fr = os.path.join(tempfile.gettempdir(), fn1+"+"+fn2+ext)
        if isinstance(obj, File):
            with open(fr, "w") as result:
                result.writelines(self.content)
                result.writelines(obj.content)
        return File(fr)

    def __next__(self):
        return self

    def __iter__(self):
        return self.content.__iter__()

    def __str__(self):
        return self.fname

    def write(self, line):
        try:
            self.content.append(line)
            self.f = open(self.fname, "w")
            self.f.writelines(self.content)
            self.f.close()
        finally:
            pass

if __name__ == "__main__":
    f1 = File("one.txt")
    f2 = File("two.txt")
    f3 = f1 + f2
    f4 = File("nonexistant")
    print(f1)
    print("="*78)
    print(f2)
    print("="*78)
    print(f3)
    print("="*78)
    f4.write("The fourth line of the file")
    print(f4)

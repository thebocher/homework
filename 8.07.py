import os

class AOpen:
    def __init__(self, path, mode='r', encoding='cp1251'):
        self.start_mode = mode
        self.mode = 'r+' if mode in ['rw', 'ra'] else mode
        self.path = path
        self.encoding = encoding

        self.reopen()

        self.cursor = len(self.read(-1)) if self.start_mode in ['r', 'rw', 'ra'] else None
        print(f'cursor <[ {self.cursor} ]>')
    
    def reopen(self):
        modes = {
            'r': os.O_RDONLY|os.O_CREAT,
            'w': os.O_WRONLY|os.O_CREAT|os.O_TRUNC,
            'a': os.O_WRONLY|os.O_CREAT,
            'rw': os.O_RDWR|os.O_CREAT,
            'ra': os.O_RDWR|os.O_CREAT,
        }
        self.fd = os.open(self.path, modes[self.start_mode])
        self.opened_file = os.fdopen(self.fd, self.mode , encoding=self.encoding)

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        print(*exc)
        self.close()

    def __iter__(self):
        return self

    def __next__(self):
        line = self.readline()
        if not line:
            raise StopIteration
        return line

    def read(self, n=None):
        n = self.cursor if not n else n
        ret = self.opened_file.read(n)
        self.reopen()
        return ret

    def readline(self):
        return self.opened_file.readline()
    
    def readlines(self):
        return self.opened_file.readlines()

    def write(self, s):
        return self.opened_file.write(s)

    def writeline(self, s):
        self.write('\n' + s)

    def writelines(self, list_of_string):
        for i in list_of_string:
            self.writeline(i)

    def seek(self, pos):
        self.cursor = pos

    def tell(self):
        return self.cursor

    def close(self):
        self.opened_file.close()

# with AOpen('file.txt', 'rw') as file:
#     print(f'iter <[')
#     for i in file:
#         print(i)
#     print(']>')

# print(f'readlines <[ {file.readlines()} ]>')
# print(f'tell <[ {file.tell()} ]>')
# print(f'read <[ {file.read()} ]>')
# print(f'readline <[ {file.readline()} ]>')
# print(f'write <[ {file.write("azaza")} ]>')
# print(f'writeline <[ {file.writeline("aqaqa")} ]>')
# print(f'writelines <[ {file.writelines(["a", "z", "a"])} ]>')
# file.close()
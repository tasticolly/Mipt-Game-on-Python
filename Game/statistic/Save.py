import shelve


class Save:
    def __init__(self):
        self.file = shelve.open("statistic/data")

    def __del__(self):
        self.file.close()

    def save(self, login, result):
        self.file[login] = result

    def get(self, login):
        return self.file[login]

    def find(self, login):
        return login in self.file.keys()

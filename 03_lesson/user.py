class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def say_firs_name(self):
        print(self.first_name)


    def say_last_name(self):
        print(self.last_name)

    def say_first_last_name(self):
        print(self.first_name, self.last_name)

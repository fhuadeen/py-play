from abc import ABC, abstractmethod


class Computer(ABC):
    """Use abstract class and methods to """

    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        pass
        # print("laptoping")

class Whiteboard(Computer):
    def write(self):
        print("writing")

class Programmer:
    def work(self, com):
        print("solving")
        com.process()

com1 = Laptop()
# prog = Programmer()
# prog.work(com1)
# white = Whiteboard()
# white.write()

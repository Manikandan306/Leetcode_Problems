from threading import Event

class Foo:
    def __init__(self):
        self.first_done = Event()
        self.second_done = Event()

    def first(self, printFirst):
        # printFirst() outputs "first"
        printFirst()
        self.first_done.set()  # Allow second() to run

    def second(self, printSecond):
        self.first_done.wait()  # Wait for first() to complete
        printSecond()
        self.second_done.set()  # Allow third() to run

    def third(self, printThird):
        self.second_done.wait()  # Wait for second() to complete
        printThird()

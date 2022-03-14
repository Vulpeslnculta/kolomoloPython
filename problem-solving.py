#  Added equality that code needs at the end to properly start things up
__name__ = "main"

import threading
import time

people = [
    {"first_name": "John", "last_name": "Black", "age": 30},
    {"first_name": "Michael", "last_name": "Johnsson", "age": 13},
    {"first_name": "Mery", "last_name": "Hunter", "age": 60},
    {"first_name": "Chris", "last_name": "Williams", "age": 45},
]


class Person:
    people_count = 0

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.id = self.increase_count()

    # This method should not be modified.
    def introduce(self):
        time.sleep(1)
        print(f"Hello, my first name is {self.first_name} and I am {self.age} years old.")

    @staticmethod
    def increase_count():
        Person.people_count += 1
        return Person.people_count


def main():
    # Added a global statement to remove error from line 50
    global thread
    threads = []
    for p in people:
        #  I had to change arrangement of variables
        x = Person(p["first_name"], p["last_name"], p["age"])
        threads.append(threading.Thread(target=x.introduce))

    for thread in threads:
        thread.start()
        #  Here I've timed whole thing, now it's around 1 second
        thread.join(0.01)
    thread.join()
    #  I've added simple statement to wait after all threads have ended by indent
    print(f"Number of people created: {Person.people_count}")

    return


if __name__ == "main":
    main()

#  I've fixed the entire code in terms of blank spaces and clarity that PEP 8 defines

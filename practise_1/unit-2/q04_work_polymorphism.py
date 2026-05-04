class Employee:
    def work(self):
        print("Working")


class Manager(Employee):
    def work(self):
        print("Managing the team and projects")


class Developer(Employee):
    def work(self):
        print("Writing and debugging code")


for person in (Manager(), Developer()):
    person.work()

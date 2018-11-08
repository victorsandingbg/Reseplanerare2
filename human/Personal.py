from class5 import *
        # Skapar Individen
class Personal:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        # Hämtar busschaufförer från ett txt dokument och pekar på rätt rad i txt dokumentet.


class Bussdriver(Personal):
    def __init__(self, first, last, report=None):
        super().__init__(first, last)
        self.report = report

    def __str__(self):
        return f"{self.first}, {self.last}"

        # Printar ut Bussförarensnamn
    def printname(self):
        return f"{self.first} {self.last}"


class Mechanic(Personal):
    def __init__(self, first, last):
        super().__init__(first, last)

    def call_mechanic(self, driver1, report, status):
        print(driver1, report, status)
        print(driver1, """called for a Mechanic!""""\n")
        mechanic1 = Mechanic(self)
        Buss().Traffic_addstuff(driver1, report, status, mechanic1)


class Cleaner(Personal):
    def __init__(self, first, last):
        super().__init__(first, last)

    def call_cleaner(self, driver1, report, status):
        print(driver1, report, status)
        print(driver1, """called for a Cleaner!""""\n")
        cleaner1 = Cleaner(self)
        Buss().Traffic_addstuff(driver1, report, status, cleaner1)

  #  def add_cleaner(self):
   #     cleanerlist = []
    #    cleanerlist.append(self)


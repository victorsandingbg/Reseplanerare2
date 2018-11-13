from class5 import *
        # Skapar Individen

class Personal:
    def __init__(self, first, last):
        self.first = first
        self.last = last.replace("\n", "")
        # Hämtar busschaufförer från ett txt dokument och pekar på rätt rad i txt dokumentet.


class Bussdriver(Personal):
    def __init__(self, first, last, report=None):
        super().__init__(first, last)
        self.report = report

    def __str__(self):
        return f"{self.first} {self.last}"

        # Printar ut Bussförarensnamn
    def printname(self):
        return f"{self.first} {self.last}"


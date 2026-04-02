class Student:

    def __init__(self, name, grade, notes):
        self.name = name
        self.grade = grade
        self.notes = notes
        self.spanish = float(notes["spanish"])
        self.english = float(notes["english"])
        self.history = float(notes["history"])
        self.sciences = float(notes["sciences"])


    def get_average(self):
        return (self.spanish + self.english + self.history + self.sciences) / 4
    

    def is_approved(self):
        return all(note >= 60 for note in [self.spanish, self.english, self.history, self.sciences])
class School:
    def __init__(self):
        self.__marks=80
    def viewMarks(self):
        print(self.__marks)
    def Teacher(self,marks):
        self.__marks=marks

x= School()
x.viewMarks()

x.__marks=100
x.viewMarks()

x.Teacher(130)
x.viewMarks()
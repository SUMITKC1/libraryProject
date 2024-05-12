import createSeats as cs

class startLibrary :
    def __init__(self, libraryLayout):
        self.libraryLayout = libraryLayout
        self.seatsPerRoom = {}
    def initialCase(self):
        for room, seatsInRoom in self.libraryLayout.items():
            self.seatsPerRoom[room] = {seat : 0 for seat in seatsInRoom} #0 means its a empty seat
    















#practice example
# class1 = startLibrary({1:[1,2,3,4,5,6]})
# class1.initialCase()
# print(class1.seatsPerRoom)

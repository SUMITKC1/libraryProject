from createSeats import createLayout 
from createDatabaseOfStudent import DataBase
class startLibrary :
    def __init__(self, libraryLayout):
        self.libraryLayout = libraryLayout
        self.seatsPerRoom = {}
        self.initialCase()
        self.getData = DataBase()

    
    def initialCase(self):
        for room, seatsInRoom in self.libraryLayout.items():
            self.seatsPerRoom[room] = {seat : [0, 0] for seat in seatsInRoom} #0 means its a empty seat
    
    def occupySeat(self, roomNumber, seatNumber, rollNumber):
        if (self.getData.doesRecordExists(rollNumber) == False):
            print("This record not found.")
            return
        
        if self.seatsPerRoom[roomNumber][seatNumber][0] == 0:
            self.seatsPerRoom[roomNumber][seatNumber] = [1, rollNumber]
        else:
            print("This seat is occupied.")
    
    def leaveSeat(self, roomNumber, seatNumber, rollNumber):
        if rollNumber == self.seatsPerRoom[roomNumber][seatNumber][1]:
            self.seatsPerRoom[roomNumber][seatNumber] = [0, 0]
        else:
            print("Seat is Not occupied by this Roll Number.")
    
    def tempLeaveSeat(self, roomNumber, seatNumber, rollNumber):
        self.seatsPerRoom[roomNumber][seatNumber] = [2, rollNumber]

    def showCurrentLibraryStatus(self):
        print(self.seatsPerRoom)

    def showEmptySeatsInLibrary(self):
        showingList = {}
        for room, seatsInRoom in self.seatsPerRoom.items():
            for seat, status in seatsInRoom.items():
                if status[0] == 0:
                    showingList[room] = {}
                    showingList[room][seat] = status

        return showingList



library = createLayout(2,[12,14],[(3,4),(7,2)])
library.createSeats(1)
library.createSeats(2)

libraryUsing = startLibrary(library.seats)

libraryUsing.occupySeat(1,2,"221ME358")
libraryUsing.occupySeat(1,3,"221ME346")
libraryUsing.leaveSeat(1,3,"221ME346")
print(libraryUsing.seatsPerRoom)










#practice example
# class1 = startLibrary({1:[1,2,3,4,5,6]})
# class1.initialCase()
# print(class1.seatsPerRoom)

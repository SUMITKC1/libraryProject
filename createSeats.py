class createLayout:
    def __init__(self,numberOfRooms, seatsInEachRoom, distributionsOfSeats) :
        self.numberOfRooms = numberOfRooms
        self.seatsInEachRoom = seatsInEachRoom
        self.distributionsOfSeats = distributionsOfSeats #this will be a list with touple as (columb, row) for each row
        self.seats = {} #this is a dic where each key is room number and value is list of seats
        self.layout = {} #this is a dic where each key is room number and value is list of tuple that describe the layout


    def createSeats(self,roomNumber): #create seats just by number withour taking location into consideration
        currentRoom = roomNumber - 1
        seatsInCurrentRoom = self.seatsInEachRoom[currentRoom]
        self.seats[roomNumber] = [*range(1, seatsInCurrentRoom + 1)]

    def createSeatsLayout(self,roomNumber): #considering location in the table (considering the room is a square matrix)
        currentRoom = roomNumber - 1
        currentRoomsDistribution = self.distributionsOfSeats[currentRoom] #this will be a touple with (columb, row)
        seats = []
        for columb in range(currentRoomsDistribution[0]):
            for row in range(currentRoomsDistribution[1]):
                seats.append((columb+1,row+1))
        
        self.layout[roomNumber] = seats

# class1 = createLayout(2,[12,14],[(3,4),(7,2)])
# class1.createSeatsLayout(2)
# class1.createSeatsLayout(1)
# print(class1.layout[1])



  

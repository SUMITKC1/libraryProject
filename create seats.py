class createLayout:
    def __init__(self,numberOfRooms, seatsInEachRoom, distributionsOfSeats) :
        self.numberOfRooms = numberOfRooms
        self.seatsInEachRoom = seatsInEachRoom
        self.distributionsOfSeats = distributionsOfSeats #this will be a list with touple as (columb, row) for each row

    def createSeats(self,roomNumber): #create seats just by number withour taking location into consideration
        currentRoom = roomNumber - 1
        seatsInCurrentRoom = self.seatsInEachRoom[currentRoom]
        return [*range(1, seatsInCurrentRoom + 1)]

    def createSeatsLayout(self,roomNumber): #considering location in the table (considering the room is a square matrix)
        currentRoom = roomNumber - 1
        currentRoomsDistribution = self.distributionsOfSeats[currentRoom] #this will be a touple with (columb, row)
        seats = []
        for columb in range(currentRoomsDistribution[0]):
            for row in range(currentRoomsDistribution[1]):
                seats.append((columb+1,row+1))
        return seats

        


  

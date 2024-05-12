class DataBase:
    def __init__(self, databaseCsv = "studentDetails.csv"):
        self.databaseCsv = databaseCsv
        import pandas as pd
        self.df = pd.read_csv(databaseCsv)
        

    #this is a very rough code to make it work will need to better it.
    def doesRecordExists(self, rollNumber):
        data = self.df[self.df["rollNumber"] == rollNumber]
        data = data.to_dict()
        if data["rollNumber"] == {}:
            return False
        return True

    def addRecord(self, name, rollNumber):
        dataToAppend = f"\n{name},{rollNumber}"
        with open(self.databaseCsv,mode = "a", newline="") as file:
            file.write(dataToAppend)
            print("Record updated successfully.")
    


        










TOUR_DATA_PATH: str = "Tours.csv"
TOUR_HEADERS:list[str] = ["TourID", "Destination", "Duration", "Price per Person", "Min # Walkers", "Max # Walkers"]

TOURS_DATA = []

#Dummy Data
TEST_DATA = [["Tour1", "Sugarloaf", "3", "10.00", "5", "12"], ["Tour2", "Balalaika", "2", "8.00", "6", "14"]]

def write_tours_data(data: list[list[str]]):
    '''
    writes data(list of list with str elements) to CSV file+adds headers
    '''
    temp:list[str] = []
    #parse the data into line strings
    temp.append(",".join(TOUR_HEADERS)+"\n") # HEADERS
    for elements in data:
        temp.append(",".join(elements)+"\n") # LINE DATA
    try:
        with open(TOUR_DATA_PATH, "w") as file:
            file.writelines(temp)
    except Exception as ex:
        print(ex)
        
def read_tour_data():
    '''
    will read all the data from Tours.CSV into memory
    '''
    try:
        with open(TOUR_DATA_PATH, "r") as file:
            lines = file.readlines()[1:]#skipping headers
        for line in lines:
            TOURS_DATA.append(line.split(","))
    except Exception as ex:
        print(ex)
        

    
#testing write function
#write_tours_data(TEST_DATA)

#testing read function
read_tour_data()
print(TOURS_DATA)


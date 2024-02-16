
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
        temp.append(",".join(elements)) # LINE DATA
        
        #fix for extra spaces
        if(temp[-2:]) != "\n":
            temp+="\n"
    try:
        with open(TOUR_DATA_PATH, "w") as file:
            file.writelines(temp)
    except Exception as ex:
        print(ex)
        
def read_tour_data():
    '''
    will read all the data from Tours.CSV into memory
    '''
    
    #had a bug where the data was duplicating 
    TOURS_DATA.clear() ## purgin all old data
    
    try:
        with open(TOUR_DATA_PATH, "r") as file:
            lines = file.readlines()[1:]#skipping headers
        for line in lines:
            
            # lets ignore empy lines
            if line != "\n":
                TOURS_DATA.append(line.split(","))
    except Exception as ex:
        print(ex)
        

def update_tour_data(id_to_update: str, index_to_update: int, value_to_add: str):
    '''
    Updates tour data
    id_to_update = the unique id of the tour
    index_to_update = the field u want to update 
        0 = "TourID", 
        1 = "Destination", 
        2 = "Duration", 
        3 = "Price per Person", 
        4 = "Min # Walkers", 
        5 = "Max # Walkers"
    '''
    for line in TOURS_DATA:
        if line[0] == id_to_update: # searching for the ID
            line[index_to_update] = value_to_add #setting the new value
            break # only updating the first instance of line
        
    write_tours_data(TOURS_DATA) # since we update a line we need re-write all the data to the CSV file
    read_tour_data() # re-reading data so its updated


def delete_tour_data(id_to_delete:str):
    '''
    deletes tour line based on TourID
    '''
    for index, line in enumerate(TOURS_DATA): # enumerate lets me get the index and the line value
        if line[0] == id_to_delete: # searching for the ID
            del(TOURS_DATA[index])# we found the id so we delete this line
            break # only delete the first instance of line
    write_tours_data(TOURS_DATA) # since we deleted a line we need re-write all the data to the CSV file
    read_tour_data() # re-reading data so its updated


#write_tours_data(TEST_DATA)

#testing delete function
read_tour_data()
print(TOURS_DATA) # printing before update

delete_tour_data("Tour1")
print(TOURS_DATA) # printing after update


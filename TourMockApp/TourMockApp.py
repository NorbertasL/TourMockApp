#NOTE: We are ASSUMING all the ids are unique


TOUR_DATA_PATH: str = "Tours.csv"
TOUR_HEADERS:list[str] = ["TourID", "Destination", "Duration", "Price per Person", "Min # Walkers", "Max # Walkers"]
tours_data = []

GUIDES_DATA_PATH: str = "Guides.csv"
GUIDES_HEADERS:list[str] = ["GuideID", "Name", "Basic Rate(Hourly)", "Rate per Walker"]
guides_data = []

WALKS_DATA_PATH: str = "Walks.csv"
WALKS_HEADERS:list[str] = ["WalkID", "GuideID", "TourID", "# Walkers"]
walks_data = []





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
        if temp[-1][-1:] != "\n": #temp[-1] gives us the last line in the lise(the one we just added above) and the [-1:] check the last char of the line "\n", "\n" is 1 char NOT 2
            temp[-1]+="\n"
    try:
        with open(TOUR_DATA_PATH, "w") as file:
            file.writelines(temp)
    except Exception as ex:
        print(ex)
    read_tour_data() # re-reading data so its updated
        

def write_guides_data(data: list[list[str]]):
    '''
    writes data(list of list with str elements) to CSV file+adds headers
    '''
    temp:list[str] = []
    temp.append(",".join(GUIDES_HEADERS)+"\n") # HEADERS
    for elements in data:
        temp.append(",".join(elements)) # LINE DATA
        
        #fix for extra spaces
        if temp[-1][-1:] != "\n":
            temp[-1]+="\n"
    try:
        with open(GUIDES_DATA_PATH, "w") as file:
            file.writelines(temp)
    except Exception as ex:
        print(ex)
    read_guides_data() # re-reading data so its updated
        
def write_walks_data(data: list[list[str]]):
    '''
    writes data(list of list with str elements) to CSV file+adds headers
    '''
    temp:list[str] = []
    temp.append(",".join(WALKS_HEADERS)+"\n") # HEADERS
    for elements in data:
        temp.append(",".join(elements)) # LINE DATA
        
        #fix for extra spaces
        if temp[-1][-1:] != "\n":
            temp[-1]+="\n"
    try:
        with open(WALKS_DATA_PATH, "w") as file:
            file.writelines(temp)
    except Exception as ex:
        print(ex)
    read_walks_data() # re-reading data so its updated
 
def read_tour_data():
    '''
    will read all the data from Tours.CSV into memory
    '''
    
    #had a bug where the data was duplicating 
    tours_data.clear() ## purgin all old data
    
    try:
        with open(TOUR_DATA_PATH, "r") as file:
            lines = file.readlines()[1:]#skipping headers
        for line in lines:
            
            # lets ignore empy lines
            if line != "\n":
                tours_data.append(line.split(","))
    except Exception as ex:
        print(ex)
        
def read_guides_data():
    '''
    will read all the data from Guidess.CSV into memory

    '''
    #had a bug where the data was duplicating 
    guides_data.clear() ## purgin all old data
    
    try:
        with open(GUIDES_DATA_PATH, "r") as file:
            lines = file.readlines()[1:]#skipping headers
        for line in lines:
            
            # lets ignore empy lines
            if line != "\n":
                guides_data.append(line.split(","))
    except Exception as ex:
        print(ex)
        
def read_walks_data():
    '''
    will read all the data from Walks.CSV into memory
    '''
    
    #had a bug where the data was duplicating 
    walks_data.clear() ## purgin all old data
    
    try:
        with open(WALKS_DATA_PATH, "r") as file:
            lines = file.readlines()[1:]#skipping headers
        for line in lines:
            
            # lets ignore empy lines
            if line != "\n":
                walks_data.append(line.split(","))
    except Exception as ex:
        print(ex)
        
def insert_tour_data():
    print("insert_tour_data")
    temp: list[str] = []
    #DANGER , not doing data checking 
    temp.append(input("TourID:"))
    temp.append(input("Destination:"))
    temp.append(input("Duration:"))
    temp.append(input("Price per Person:"))
    temp.append(input("Min # Walkers:"))
    temp.append(input("Max # Walkers:"))
    
    tours_data.append(temp)
    write_tours_data(tours_data)#updating CSV
    
def insert_guide_data():
    print("insert_guide_data")
    temp: list[str] = []
    #DANGER , not doing data checking 
    temp.append(input("GuideID:"))
    temp.append(input("Name:"))
    temp.append(input("Basic Rate(Hourly):"))
    temp.append(input("Rate per Walker:"))

    
    guides_data.append(temp)
    write_guides_data(guides_data)#updating CSV
    
def insert_walks_data():

    print("insert_walks_data")
    temp: list[str] = []
    #DANGER , not doing data checking 
    temp.append(input("WalkID:"))
    temp.append(input("GuideID:"))
    temp.append(input("TourID:"))
    temp.append(input("# Walkers:"))

    
    walks_data.append(temp)
    write_walks_data(walks_data)#updating CSV
    
    

def update_guides_data(id_to_update: str, index_to_update: int, value_to_add: str):
    '''
    Updates guides data
    id_to_update = the unique id of the tour
    index_to_update = the field u want to update 
    0 = "GuideID", 
    1 = "Name", 
    2 = "Basic Rate(Hourly)", 
    3 = "Rate per Walker"
    '''
    for line in guides_data:
        if line[0] == id_to_update: # searching for the ID
            line[index_to_update] = value_to_add #setting the new value
            break # only updating the first instance of line
        
    write_guides_data(guides_data) # since we update a line we need re-write all the data to the CSV file
   
    
def delete_guide_data(id_to_delete:str):
    '''
    deletes guids line based on GuidesID
    '''
    for index, line in enumerate(guides_data): # enumerate lets me get the index and the line value
        if line[0] == id_to_delete: # searching for the ID
            del(guides_data[index])# we found the id so we delete this line
            break # only delete the first instance of line
    write_guides_data(guides_data) # since we deleted a line we need re-write all the data to the CSV file
    
        
# WE DONT NEED update_tour_data I MISSREAD THE TASK
# def update_tour_data(id_to_update: str, index_to_update: int, value_to_add: str):
#     '''
#     Updates tour data
#     id_to_update = the unique id of the tour
#     index_to_update = the field u want to update 
#         0 = "TourID", 
#         1 = "Destination", 
#         2 = "Duration", 
#         3 = "Price per Person", 
#         4 = "Min # Walkers", 
#         5 = "Max # Walkers"
#     '''
#     for line in TOURS_DATA:
#         if line[0] == id_to_update: # searching for the ID
#             line[index_to_update] = value_to_add #setting the new value
#             break # only updating the first instance of line
        
#     write_tours_data(TOURS_DATA) # since we update a line we need re-write all the data to the CSV file
#     read_tour_data() # re-reading data so its updated

# WE DONT NEED delete_tour_data I MISSREAD THE TASK
# def delete_tour_data(id_to_delete:str):
#     '''
#     deletes tour line based on TourID
#     '''
#     for index, line in enumerate(TOURS_DATA): # enumerate lets me get the index and the line value
#         if line[0] == id_to_delete: # searching for the ID
#             del(TOURS_DATA[index])# we found the id so we delete this line
#             break # only delete the first instance of line
#     write_tours_data(TOURS_DATA) # since we deleted a line we need re-write all the data to the CSV file
#     read_tour_data() # re-reading data so its updated

def make_dummy_data() -> bool:#a way to populate the datbles
    WALKS_TEST_DATA = [["Walk20", "Guide71", "Tour1", "10"], 
                       ["Walk21", "Guide72", "Tour3", "8"],
                       ["Walk22", "Guide71", "Tour2", "13"],
                       ["Walk23", "Guide73", "Tour2", "8"],
                       ["Walk24", "Guide73", "Tour1", "12"],
                       ["Walk25", "Guide72", "Tour2", "6"],
                       ["Walk26", "Guide71", "Tour3", "18"],
                       ["Walk27", "Guide71", "Tour1", "11"],
                       ["Walk28", "Guide73", "Tour2", "8"],
                       ["Walk29", "Guide73", "Tour2", "8"]]
    
    GUIDES_TEST_DATA = [["Guide73", "Barbara", "12.50", "1.25"], 
                        ["Guide72", "Eddie", "15.00", "2"], 
                        ["Guide71", "Bill", "14.80", "0.95"]]
    
    TOURS_TEST_DATA = [["Tour1", "Sugarloaf", "3", "10.00", "5", "12"], 
                       ["Tour2", "Balalaika", "2", "8.00", "6", "14"], 
                       ["Tour3", "Wahtever", "4", "16.00", "7", "18"]]
    
    user_input = input("Would you like to generate dummy data(y/n):")
    if(user_input.upper() == "Y"):  
        #Generating dummy data
        write_tours_data(TOURS_TEST_DATA)
        write_guides_data(GUIDES_TEST_DATA)
        write_walks_data(WALKS_TEST_DATA)
        print(f"{TOURS_TEST_DATA} tour data generated \n {GUIDES_TEST_DATA} guides data generated \n {WALKS_TEST_DATA} walks data generated")
        return True
    return False
        
        
def print_rows(data_list):
    for data in data_list:
        print(data)

# if dumy data is generated it will auto read it in else we need to read it in ourselfs
if(not make_dummy_data()):
    #Reading in data at the starts
    print("Reading in existing data!")
    read_tour_data()
    read_guides_data()
    read_walks_data()




print("#"*20)
print_rows(tours_data)
print("-"*20)
print_rows(guides_data)
print("-"*20)
print_rows(walks_data)







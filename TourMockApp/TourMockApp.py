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
 
def get_guides_earnings():
    '''
    returns output_str, walk_costs
    '''
    #Based on the completed walks, calculate and display the Basic Pay, Bonus Pay and Total Pay
    #earned by each Guide.
    output_str = []
    walk_costs = []
    for guide in guides_data:# looping trough all the guides
        hourly_earning:float = 0
        walker_earning:float = 0
        #getting all hours worked by the guide and all people guided
        
        for walk in walks_data:
            if walk[1] == guide[0]: # walk[1] = guide id of the guide,  guide[0] = guide id
                duratio:int = 0
                for tour in tours_data: # have to find the tour duration
                    if walk[2] == tour[0]: # walk[2] = tourID, tour[0] = tourID
                        duratio = int(tour[4]) # tour[4] us the duration
                        break # dont need to keep looking
                hourly_earning += duratio*float(guide[3]) # duratio = #h for the walk, guide[2] = guide hourly rate
                walker_earning += int(walk[3])*float(guide[3]) # walk[3] = number of walkers, guide[3] = rate per walker
                walk_costs.append([walk[0], walk[2], walk[3] ,hourly_earning + walker_earning]) # saving this for company earning calc
        output_str.append(f"{guide[1]} has earned hourly:{hourly_earning}, plus {walker_earning} for walkers for a total: {hourly_earning+walker_earning}")
    return output_str, walk_costs

                
def print_company_earnings():
    #The overall Profit / Loss made by the company for these completed walks
    _, walk_costs = get_guides_earnings() # _ using to discard of the output_str, we only care about the costs
    output_string = []
    for walk in walk_costs:
        tour_price:float = 0;
        for tour in tours_data:
            if tour[0] == walk[1]:
                tour_price =  float(tour[3]) 
                break
        output_string.append(f"WalkID:{walk[0]}, profit is:{tour_price*int(walk[2]) - walk[3]}")
        
    print_rows(output_string)


        
def print_rows(data_list):
    for data in data_list:
        print(data)
        
def user_interface():
    def user_interface_tables():
        def interf_table_tours():
            while(True):
                print("1: View all tour data")
                print("2: Add new Tours")
                print("3: Go back!")
                
                user_input = input("Selection:")
    
                if(user_input == "1"): # keeping input as string and comparing to string
                    print_rows(tours_data)
                elif(user_input == "2"):
                    insert_tour_data()
                    print_rows(tours_data)
                elif(user_input == "3"):
                    return
                else:
                    print("Unknown input!")
                
        def interf_table_guides():
            def update_guide_interface():
                print_rows(guides_data)
                guide_id = input("Enter GuideID you wish to update:")
                
                
                # 0 = "GuideID", 
                # 1 = "Name", 
                # 2 = "Basic Rate(Hourly)", 
                # 3 = "Rate per Walker"
                try:
                    field_index = int(input("Select field to edit 1 = name, 2 = Rate, 3 = Walk Rare"))
                    if field_index in [1, 2 ,3]:
                        user_value = input("Eenter new value: ") # WARNING value validity not checked
                        update_guides_data(guide_id, field_index, user_value)
                        print("Update Done!")
                    else:
                       print("Bad input! Nothing was Changed") 
                except:
                    print("Bad input! Nothing was Changed")
                return # going back to previous menu
               
                    
                
                pass
            def delete_guide_interface():
                #
                print_rows(guides_data)
                guide_id = input("Enter GuideID to delete:")
                delete_guide_data(guide_id) # not checking if valid
                return # going back
            
            while(True):
                print("1: View all Guide data")
                print("2: Add new Guide")
                print("3: Update Guide")
                print("4: Delete Guide")
                print("5: Go back!")
                
                user_input = input("Selection:")
    
                if(user_input == "1"): # keeping input as string and comparing to string
                    print_rows(guides_data)
                elif(user_input == "2"):
                    insert_guide_data()
                    print_rows(guides_data)
                elif(user_input == "3"):
                    update_guide_interface()
                    print_rows(guides_data)
                elif(user_input == "4"):
                    delete_guide_interface()
                    print_rows(guides_data)
                elif(user_input == "5"):
                    return
                else:
                    print("Unknown input!")

        def interf_table_walks():
            while(True):
                print("1: View all walks data")
                print("2: Add new Walk")
                print("3: Go back!")
                
                user_input = input("Selection:")
    
                if(user_input == "1"): # keeping input as string and comparing to string
                    print_rows(walks_data)
                elif(user_input == "2"):
                    insert_walks_data()
                    print_rows(walks_data)
                elif(user_input == "3"):
                    return
                else:
                    print("Unknown input!")
        
        while(True):
            print("1: For Tours")
            print("2: For Guides")
            print("3: For Walkss")
            print("4: Go back in menu")
    
            user_input = input("Selection:")
    
            if(user_input == "1"): # keeping input as string and comparing to string
                interf_table_tours()
            elif(user_input == "2"):
                interf_table_guides()
            elif(user_input == "3"):
                interf_table_walks()
            elif(user_input == "4"):
                return # will go back 1 to previous menu
            else:
                print("Unknown input!")
    def user_interface_calculations(): #TODO
        print("1: For Guide Earnings")
        print("2: For Company Earnings per walk")
        print("3: Go back in menu")
        
        user_input = input("Selection:")
    
        if(user_input == "1"): # keeping input as string and comparing to string
            output_str, _ = get_guides_earnings() # _ var just means we are discarding the walk_cost values
            print_rows(output_str)
        elif(user_input == "2"):
            print_company_earnings()
        elif(user_input == "3"):
            return # will go back 1 to previous menu
        else:
            print("Unknown input!")
    
    while(True):
        print("1: For Tables")
        print("2: For Calulations")
        print("3: To Exit")
    
        user_input = input("Selection:")
    
        if(user_input == "1"): # keeping input as string and comparing to string
            user_interface_tables()
        elif(user_input == "2"):
            user_interface_calculations()
        elif(user_input == "3"):# will break out of the user interface loop
            return
        else:
            print("Unknown input!")
        
# if dumy data is generated it will auto read it in else we need to read it in ourselfs
if(not make_dummy_data()):
    #Reading in data at the starts
    print("Reading in existing data!")
    read_tour_data()
    read_guides_data()
    read_walks_data()

user_interface()

print("Application is finished!!!")






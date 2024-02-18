# Same as TourMockApp but using SQLite instead of CSV for storage
import sqlite3

TEST_MODE: bool = True

DB_PATH:str = "Test.db"
TOURS_TABLE_NAME:str = "tours"
GUIDES_TABLE_NAME:str = "guides"
WALKS_TABLE_NAME:str = "walks"

def execure_sql_querry(sql_statment:str, write_querry:bool = False, values:tuple = ()) -> list | bool: # list | bool Python 3.10+ Hinting
    return_value: list | bool = False 
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            return_value = cursor.execute(sql_statment, values).rowcount > 0 #rowcount = affected rows
            if write_querry:
                conn.commit()#commit is only needed for write querries
                return_value = True # No error so SQL querry was successful 
            else:
                return_value = cursor.fetchall() # fetchall is only needed if we are retiving data, write_querry == False
    except Exception as ex:
        print(ex)
    finally:
        return return_value # using finally block to make sure something is always returned
    
def create_tables():
    '''
    Creates all the needed tables for the appliaction if they do not exist
    '''
    tours_table_sql:str = f'''CREATE TABLE IF NOT EXISTS {TOURS_TABLE_NAME}(
_ID INTEGER PRIMARY KEY,
destination TEXT, 
duration REAL,
price REAL,
min_walkers INTEGER,
max_walkers INTEGER
);
'''
    guides_table_sql:str = f'''CREATE TABLE IF NOT EXISTS {GUIDES_TABLE_NAME}(
_ID INTEGER PRIMARY KEY,
name TEXT, 
hour_rate REAL,
rate_per_walker REAL
);
'''   
    walks_table_sql:str = f'''CREATE TABLE IF NOT EXISTS {WALKS_TABLE_NAME}(
_ID INTEGER PRIMARY KEY,
guide_ID INTEGER, 
tour_ID INTEGER,
walker_count INTEGER
);
'''     
      
    execure_sql_querry(tours_table_sql, True)
    execure_sql_querry(guides_table_sql, True)
    execure_sql_querry(walks_table_sql, True)  
    
def add_row_to(table:str, values:dict):
    
    sql_querry:str = f"INSERT INTO {table}({','.join(values.keys())}) VALUES({','.join('?'*len(values))})"
  
    if execure_sql_querry(sql_querry, True, tuple(values.values())):
        print(f"{values} data was added to {table}")
    else:
        print(f"FAILED to add {values} data to {table}")
    
    

    
def dummy_data_interface():
    def delete_table_data(table: str):
        sql_querry: str = f"DELETE FROM {table}"
        if execure_sql_querry(sql_querry, True):
            print(f"{table} TABLE data was DELETED!")
        else:
            print(f"{table} TABLE data DELETION FAILED!")
    
    def tours_dummy_data():
        add_row_to(TOURS_TABLE_NAME, {"destination": "Sugarloaf", "duration": 3, "price": 10.00, "min_walkers": 5, "max_walkers": 12})
        add_row_to(TOURS_TABLE_NAME, {"destination": "Dananik", "duration": 2, "price": 8.50, "min_walkers": 3, "max_walkers": 10})
        add_row_to(TOURS_TABLE_NAME, {"destination": "Sun Cliff", "duration": 2, "price": 11.00, "min_walkers": 4, "max_walkers": 11})
        
    def guides_dummydata():
         add_row_to(GUIDES_TABLE_NAME, {"name": "Barbara", "hour_rate": 12.50, "rate_per_walker": 1.25})
         add_row_to(GUIDES_TABLE_NAME, {"name": "Eddie", "hour_rate": 10.50, "rate_per_walker": 1.50})
         add_row_to(GUIDES_TABLE_NAME, {"name": "Tom", "hour_rate": 12.00, "rate_per_walker": 0.95})
         add_row_to(GUIDES_TABLE_NAME, {"name": "Bob", "hour_rate": 14.20, "rate_per_walker": 1.45})

    def walks_dummy_data():
        add_row_to(WALKS_TABLE_NAME, {"guide_ID":1, "tour_ID":1, "walker_count":10})
        add_row_to(WALKS_TABLE_NAME, {"guide_ID":2, "tour_ID":1, "walker_count":6})
        add_row_to(WALKS_TABLE_NAME, {"guide_ID":3, "tour_ID":1, "walker_count":12})
        
        add_row_to(WALKS_TABLE_NAME, {"guide_ID":4, "tour_ID":2, "walker_count":3})
        add_row_to(WALKS_TABLE_NAME, {"guide_ID":2, "tour_ID":2, "walker_count":7})
        add_row_to(WALKS_TABLE_NAME, {"guide_ID":3, "tour_ID":2, "walker_count":5})
        
        add_row_to(WALKS_TABLE_NAME, {"guide_ID":4, "tour_ID":3, "walker_count":5})
        add_row_to(WALKS_TABLE_NAME, {"guide_ID":1, "tour_ID":3, "walker_count":7})
        add_row_to(WALKS_TABLE_NAME, {"guide_ID":3, "tour_ID":3, "walker_count":5})
        
        add_row_to(WALKS_TABLE_NAME, {"guide_ID":4, "tour_ID":1, "walker_count":10})
        add_row_to(WALKS_TABLE_NAME, {"guide_ID":1, "tour_ID":2, "walker_count":5})
        add_row_to(WALKS_TABLE_NAME, {"guide_ID":2, "tour_ID":3, "walker_count":11})
        add_row_to(WALKS_TABLE_NAME, {"guide_ID":3, "tour_ID":3, "walker_count":10})
       
        
    if input("Remake Database with TEST DATA?(Y/N)")[0].upper() == "Y":
        print("Deleting any existing data...")
        delete_table_data("tours")
        delete_table_data("guides")
        delete_table_data("walks")

        print("Generating new data...")
        tours_dummy_data()
        guides_dummydata()
        walks_dummy_data()
    print("#"*20)
        
def user_interface():
    def user_interface_tables():
        def interf_table_tours():
            while(True):
                print("1: View all tour data TODO")
                print("2: Add new Tours TODO")
                print("3: Go back!")
                
                user_input = input("Selection:")
    
                if(user_input == "1"): # keeping input as string and comparing to string
                    print("NOT DONE!") #TODO
                elif(user_input == "2"):
                    print("NOT DONE!") #TODO
                elif(user_input == "3"):
                    return
                else:
                    print("Unknown input!")
                
        def interf_table_guides():
            def update_guide_interface():
                print("NOT DONE!") #TODO
                return
                #guide_id = input("Enter GuideID you wish to update:")
                
                
                # 0 = "GuideID", 
                # 1 = "Name", 
                # 2 = "Basic Rate(Hourly)", 
                # 3 = "Rate per Walker"
                try:
                    field_index = int(input("Select field to edit 1 = name, 2 = Rate, 3 = Walk Rare"))
                    if field_index in [1, 2 ,3]:
                        user_value = input("Eenter new value: ") # WARNING value validity not checked
                        print("NOT DONE!") #TODO
                        print("Update Done!")
                    else:
                       print("Bad input! Nothing was Changed") 
                except:
                    print("Bad input! Nothing was Changed")
                return # going back to previous menu
               
            def delete_guide_interface():
                #
                print("NOT DONE!") #TODO
                return # going back
            
            
            while(True):
                print("1: View all Guide data TODO")
                print("2: Add new Guide TODO")
                print("3: Update Guide TODO")
                print("4: Delete Guide TODO")
                print("5: Go back!")
                
                user_input = input("Selection:")
    
                if(user_input == "1"): # keeping input as string and comparing to string
                    print("NOT DONE!") #TODO
                elif(user_input == "2"):
                    print("NOT DONE!") #TODO
                elif(user_input == "3"):
                    update_guide_interface()
                    print("NOT DONE!") #TODO
                elif(user_input == "4"):
                    print("NOT DONE!") #TODO
                    delete_guide_interface()
                elif(user_input == "5"):
                    return
                else:
                    print("Unknown input!")

        def interf_table_walks():
            while(True):
                print("1: View all walks data TODO!")
                print("2: Add new Walk TODO")
                print("3: Go back!")
                
                user_input = input("Selection:")
    
                if(user_input == "1"): # keeping input as string and comparing to string
                    print("NOT DONE!") #TODO
                elif(user_input == "2"):
                    print("NOT DONE!") #TODO
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
   
    
    while(True):
        print("1: For Tables")
        print("2: For Calulations TODO!")
        print("3: To Exit")
    
        user_input = input("Selection:")
    
        if(user_input == "1"): # keeping input as string and comparing to string
            user_interface_tables()
        elif(user_input == "2"):
            print("NOT DONE!") #TODO
        elif(user_input == "3"):# will break out of the user interface loop
            return
        else:
            print("Unknown input!")
        
        

if TEST_MODE:
    create_tables()
    dummy_data_interface()

user_interface()
print("App is closed!")
    
  
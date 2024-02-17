# Same as TourMockApp but using SQLite instead of CSV for storage
import sqlite3

TEST_MODE: bool = True

DB_PATH:str = "Test.db"
TOURS_TABLE_NAME:str = "tours"
GUIDES_TABLE_NAME:str = "guides"
WALKS_TABLE_NAME:str = "walks"

def execure_sql_querry(sql_statment:str, write_querry:bool = False) -> list | bool: # list | bool Python 3.10+ Hinting
    return_value: list | bool = False 
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(sql_statment)
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
    

    
def dummy_data_interface():
    def delete_table_data(table: str):
        sql_querry: str = f"DELETE FROM {table}"
        if execure_sql_querry(sql_querry, True):
            print(f"{table} TABLE data was DELETED!")
        else:
            print(f"{table} TABLE data DELETION FAILED!")
        
        
    if input("Remake Database with TEST DATA?(Y/N)")[0].upper() == "Y":
        print("Deleting any existing data...")
        delete_table_data("tours")
        delete_table_data("guides")
        delete_table_data("walks")

        print("Generating new data...")
        #TODO
        
        
        

if TEST_MODE:
    create_tables()
    dummy_data_interface()
    
  
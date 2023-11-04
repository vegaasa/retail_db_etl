import sys
from config import DB_DETAILS
from util import get_tables,load_db_details
from read import read_table

def main():
    """Programs Takes at Least One Argument"""
    env = sys.argv[1]
    db_details = load_db_details(env)
    tables = get_tables('table_list.txt')
    for table_name in tables['table_name']:
        data,column_names = read_table(db_details,table_name)
    print(data)
    
if __name__ == '__main__':
    main()

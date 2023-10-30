import pandas as pd

def get_tables(path):
    tables = pd.read_csv(path,sep=':')
    #filter only to be loaded to yes
    return tables.query('to_be_loaded == "yes"')


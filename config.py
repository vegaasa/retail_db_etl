import os

DB_DETAILS = {
    'dev' : {
        'SOURCE_DB' : {
            'DB_TYPE'   :'mysql',
            'DB_HOST'   :'localhost',
            'DB_NAME'   :'retail_db',
            'DB_USER'   : os.environ.get('DB_USER_MYSQL'),
            'DB_PASS'   : os.environ.get('DB_PASS_MYSQL')
            },
        'TARGET_DB':{
            'DB_TYPE'   :'postgres',
            'DB_HOST'   :'localhost',
            'DB_NAME'   :'retail_db',
            'DB_USER'   : os.environ.get('DB_USER_POSTGRES'),
            'DB_PASS'   : os.environ.get('DB_PASS_POSTGRES')
            }
    }
}
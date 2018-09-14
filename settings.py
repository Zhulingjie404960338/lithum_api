DATABASE_URI = 'mysql+pymysql://root:@172.16.29.32/zabbix'
SERVER_NAME = '127.0.0.1:5000'

try:
    from local_settings import *
except:
    pass

import logging

def create_helper(): 
    fileName  = 'TSPlog.log' 
    formatStr = '%(asctime)s %(message)s'
    logging.basicConfig(format=formatStr, filename=fileName, level=logging.INFO)
    return logging.getLogger('team-TPS-logger')

def info(logged_string):
    create_helper().info(logged_string)

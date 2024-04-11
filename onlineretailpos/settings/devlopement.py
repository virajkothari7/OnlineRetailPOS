from .base import *
import os, socket
# from sshtunnel import SSHTunnelForwarder
from dotenv import load_dotenv
load_dotenv()

ip_address = socket.gethostbyname(socket.gethostname())
    
DEBUG = False
SECRET_KEY = os.getenv('SECRET_KEY_DEV', 'django_dev_secret_key_online-retail-pos-1234')

ALLOWED_HOSTS = [ip_address,'127.0.0.1']
CSRF_TRUSTED_ORIGINS = [f"http://{ip_address}","http://127.0.0.1"]

print(f"Connect on this address:") # get the ip address from the command line.
print(f"http://127.0.0.1:8000")
print(f"{ip_address}:8000 \nDocker Container may have different IP, VPN will screw IP address as well\nMight not work on those cases")

# # Database sqllite
# # https://docs.djangoproject.com/en/4.0/ref/settings/#databases
database_dict = {
    'sqlite' :  {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3', 
        } ,
    'postgres' : {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DB_NAME', "OnlineRetailPOS"),  # Use environment variable DB_NAME, defaulting to 'default_db_name'
            'USER': os.getenv('DB_USERNAME'),  # Use environment variable DB_USERNAME
            'PASSWORD': os.getenv('DB_PASSWORD'),  # Use environment variable DB_PASSWORD
            'HOST': os.getenv('DB_HOST', "localhost"),  # Use environment variable DB_HOST
            'PORT': os.getenv('DB_PORT', ''),  # By default, PostgreSQL uses port 5432
        } ,
    'mysql': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv('DB_NAME', "OnlineRetailPOS"),  # Use environment variable DB_NAME
            'USER': os.getenv('DB_USERNAME'),  # Use environment variable DB_USERNAME
            'PASSWORD': os.getenv('DB_PASSWORD'),  # Use environment variable DB_PASSWORD
            'HOST': os.getenv('DB_HOST', "localhost"),  # Use environment variable DB_HOST
            'PORT': os.getenv('DB_PORT', ''),  
            'OPTIONS':{
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
                }
    }
}

print(f"Database configuration is set to {database_dict[os.getenv('NAME_OF_DATABASE', 'sqlite')]['ENGINE']}")

DATABASES = {
    'default':  database_dict[os.getenv('NAME_OF_DATABASE', 'sqlite')]
    
}


## COMMENT/UNCOMMENT to switch from  sqllite file to regular cloud database, configuration may differ
##  Database Connection

## SSH Tunnel 
# Connect to a server using the ssh keys. See the sshtunnel documentation for using password authentication
# ssh_tunnel = SSHTunnelForwarder(
#     os.getenv('SSH_HOST'),
#     ssh_username = os.getenv('SSH_USERNAME'),
#     ssh_password = os.getenv('SSH_PASSWORD'),
#     remote_bind_address=(os.getenv('SSH_DB_HOST'), 3306),
# )
# ssh_tunnel.start()

## Database MySQL
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': os.getenv('DB_NAME'),
#         'USER' : os.getenv('DB_USERNAME'),
#         'PASSWORD' : os.getenv('DB_PASSWORD'),
#         'HOST': "127.0.0.1",
#         'PORT' : ssh_tunnel.local_bind_port,
#         'OPTIONS':{
#              'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
#             }
#     }
# }


# Store Information
# For Line Break add \n
#Can not be more than (RECEIPT_CHAR_COUNT - 2) Characters per line(\n), if wants to add more break it up by \n new line
RECEIPT_CHAR_COUNT = int(os.getenv('RECEIPT_CHAR_COUNT', 32)) 
STORE_NAME = os.getenv('STORE_NAME', "STORE NAME")  #Can not be more than RECEIPT_CHAR_COUNT 
STORE_ADDRESS = os.getenv('STORE_ADDRESS', "STORE ADDRESS")
STORE_PHONE = os.getenv('STORE_PHONE', "")
RECEIPT_HEAD = f"{STORE_NAME}\n{STORE_ADDRESS}"  
RECEIPT_HEAD = RECEIPT_HEAD + f"\n{STORE_PHONE}" if os.getenv('Include_Phone_In_Heading',"False").lower() == "true" else RECEIPT_HEAD
RECEIPT_ADDITIONAL_HEADING = os.getenv('RECEIPT_ADDITIONAL_HEADING', "")
RECEIPT_HEADER = f"{RECEIPT_HEAD}\n{RECEIPT_ADDITIONAL_HEADING}" if RECEIPT_ADDITIONAL_HEADING != "" else RECEIPT_HEAD
RECEIPT_FOOTER = os.getenv('RECEIPT_FOOTER',"Thank You")


# Printer Settings
PRINTER_VENDOR_ID = os.getenv('PRINTER_VENDOR_ID', "")
PRINTER_PRODUCT_ID = os.getenv('PRINTER_PRODUCT_ID', "")
PRINT_RECEIPT = os.getenv('PRINT_RECEIPT', False)
CASH_DRAWER = os.getenv('CASH_DRAWER', False)

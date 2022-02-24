from decouple import config

PRIVATE_KEY = open('private-key.pem', 'r').read()
USER_ID = config('USER_ID', cast=str)

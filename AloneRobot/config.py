
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "23710378" # integer value, dont use ""
    API_HASH = "a5ebe1fd8ae5715a9eb2a9364001189a"
    TOKEN = "6392016724:AAGnr8czUSreoQ_H3Z_1h463pq2SjkrvCcw"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = "7552579717" # If you dont know, run the bot and do /id in your private chat with it, also an integer
    
    SUPPORT_CHAT = "AloneXSupport"  # Your own group for support, do not add the @
    START_IMG = "https://telegra.ph//file/9e8ce3092848a1bc5d9d6.jpg"
    EVENT_LOGS = "-1001603822916"  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= "mongodb+srv://hny:zara@cluster0.lfe5o.mongodb.net/?retryWrites=true&w=majority"
    # RECOMMENDED
    DATABASE_URL = "postgres://uwkikwscaknxfe:37c4e10ab8baa761ab5c99fe155944dd0e1cb45ae846472a8ec7f35fafd350df@ec2-3-228-158-221.compute-1.amazonaws.com:5432/ddqkkr8tao7gr5"  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        "LQ58UKEV7CH8YCW5"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "LXDWL7BZN03W"
    # Get your API key from https://timezonedb.com/api

    # Optional fields
    CHATBOT_API = "5935608297-fallen-usbk33kbsu" # get it from @FallenChat_Bot using /token
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

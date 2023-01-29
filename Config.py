import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6296490"))
    API_HASH = os.environ.get("API_HASH", "24385183c93a98ae4155c25d9f5f64b2")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6080251945:AAE4mvykix0gkN7MbrhPeIm_kxVi7t5ZSSU")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BJWap1wBu51wh4b3a5Z9OeN0-M8Z8Jh7Tz3nCafZ3ePQomRXE0d7ZwV-knLI2Nrr9EP1kKjoJDHOsVxXwl9Eap25exZFZXAeK-6GQ7wonDwu7g1CkKD_Pm5QvmoxUI23vH7m1HV0SS9eD1zR7403Wr4fjVwYs9yg9Cv3AcGSYg9egMYb0JBrba5kTLAt8Qbu9RhqJdPVWoQB5fKBNrASZg4fPVIaTfURbK91h5hnLkDaHqavUj53HaMsM8oU9NzhrYCJahhVBAaYO5z7jZkPqeICc8lLRfsG580YgYg_RhtWvrOMRW5Yz170mAUxsCunlK5AsZThDF_TAUtvnmcRDvsfcjfPV2E=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "TgFlashRobot")
    SUPPORT = os.environ.get("SUPPORT", "sexxynEtgFlash") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TgFlash") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/6c32810401263be4efb61.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/dd3c08bd6b1820b14a6d0.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5467311248")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', "True") # Change it to "True"
    

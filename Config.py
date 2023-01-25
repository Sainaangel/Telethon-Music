import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6296490"))
    API_HASH = os.environ.get("API_HASH", "24385183c93a98ae4155c25d9f5f64b2")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5941659598:AAGnHLMYzgoDjZtyn5KpbewyAF0BUzkWnlw")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BJWap1sBu0uhlXBSKci9upQFQS562rsLqU2ONrevbiOHqTNAlFX-ApBhgbLZIUftzHCukOwb27UN2ITfF3MvHtp8MXyjWOfCqAWu69wlxZew-5fJkIG9tKcXga7WtYe0ZF61ZGFElvTTDKubmqohAnapXlR2CahnOoxOoN6BLPW3C70lWotYtnx70mGiG_WSCZ5JX_33lSdezw5erv0thvlCQSLJFapo4QQ6ESKfeLjMo1_tGM7SCRoaS6ZgPzL7nwW07T-DFEQx1bY7PUwGuda2TWkAo-wmIZWuBkls5gutzTxleyErDCaPg6uNoTOydotVyg50b5NsV2Q6Z-AMZ9WEKBpxGWc=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "IPMUSIXBOT")
    SUPPORT = os.environ.get("SUPPORT", "FRIENDZVIBES") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "FRIENDZVIBES") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/6c32810401263be4efb61.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/dd3c08bd6b1820b14a6d0.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5467311248")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', "True") # Change it to "True"
    

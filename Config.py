import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6296490"))
    API_HASH = os.environ.get("API_HASH", "24385183c93a98ae4155c25d9f5f64b2")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6080251945:AAFPZ-5EA-GpbWG1KuPd0ET2J_ehDzQ1PUs")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzkBuyrkm1qvmbJfoVoYRFGdqcS1l4dlO_0Z5XRiOma_euM8mUolu1taEI5ZS3NiULljH0kOJm14ddjk8rwZ4kLW7_kcK55AH8pTbDZN_MEMfktcN4TXaSW-uwZSgAlubxSxIrYauNYH6Ue0NGgN-ojqQ5XOwCNqQ6_iovPGx16h30FwrQNht5pVt6OAjHUhzkv01qDA73uw6FNEiOEvzHBpw1rLOV-8kxowWYBzSzgW2F5RZNjCcb4jl6c77CdFu0BxCuic9z75PWMzOv6i96Khdf7YA08iwBEZkpBOm9-7I2G9M-YurT3BpI43y9AHpteiLlOpgPVyJgYicELHghkSe2c=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "TgFlashRobot")
    SUPPORT = os.environ.get("SUPPORT", "TgFlash") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TgFlash94") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/2752523b23793a09d9c63.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/2752523b23793a09d9c63.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5467311248")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', "True") # Change it to "True"
    

import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6296490"))
    API_HASH = os.environ.get("API_HASH", "24385183c93a98ae4155c25d9f5f64b2")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6080251945:AAE4mvykix0gkN7MbrhPeIm_kxVi7t5ZSSU")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BJWap1sBuwfslt9sne_d84vWgjertawWAYaXpLE1FhrkAwHQvWi-6GnQFIrIw1ly5Bm-f6-OQ0QbKYj1cevuiIFrjd1Xc-eYq6q7iY57KlG3U8RY93fBvcir17qQpCEI7Bb_rMviC6rVB-ixks3ZfLdjFACv97OlOaSR47Q1RPzhV84LXPuWtYyiHEAIkcZCVj5Jr1oxPtxB6HHxc9gz8SedRXd-Ok86yVX5R9vPJBhIresbSEnotMxI7fudCcbI9erZX-7pagN3-QItJcbx_QxXmxJEpHuz49vRvU8M95a0ZgNrAoHSnA7gDYZRUo0YkJKtP86gQQRMc4YtjSyGDm8ksEchVXI=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "TgFlashRobot")
    SUPPORT = os.environ.get("SUPPORT", "sexxynEtgFlash") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TgFlash") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/6c32810401263be4efb61.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/dd3c08bd6b1820b14a6d0.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5467311248")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', "True") # Change it to "True"
    

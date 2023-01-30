import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6296490"))
    API_HASH = os.environ.get("API_HASH", "24385183c93a98ae4155c25d9f5f64b2")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6080251945:AAFPZ-5EA-GpbWG1KuPd0ET2J_ehDzQ1PUs")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BJWap1sBu1WDNirSFt2zhK2dhSC6-p2lYSd_wM4uv1vwgUWEliHrqbLBOdMKI0dEm0ZfuXOFFtCB9R1kQSrZSn1aqNiqG-3pD-vljRbJJ8HSYTIHoA-JP0FLJkBZMrmj4juRid2VUG6yaR7m7P_dxcMgCtzghZgeb_AWS8SleFnXFj-73P8Hnv0a2BfaBd9DsfyzaeXvG-QzQNhZGgl_Aceq3v_9sWhBegg10XmdLtmOwy3Wo4OgaCONDeZExE26Vxi40QlZEm0bFGK_3rbSAmogrNl_Sr8qPQA376HNV4sbL62u2wXBPSpRYL-w4E5W55Oi3IiNYk0JKxJHs62z_ZpHfiS_6QI=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "TgFlashRobot")
    SUPPORT = os.environ.get("SUPPORT", "TgFlash") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TgFlash94") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/2752523b23793a09d9c63.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/2752523b23793a09d9c63.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5467311248")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', "True") # Change it to "True"
    

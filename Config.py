import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6296490"))
    API_HASH = os.environ.get("API_HASH", "24385183c93a98ae4155c25d9f5f64b2")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6080251945:AAFPZ-5EA-GpbWG1KuPd0ET2J_ehDzQ1PUs")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzUBu2ynmLo_WnAq_ggysMw4OGc8bxXNzznqPCKIgIMECSjLdqRMLMbqsje4gt95YviFK5vk3Fo8R3XEeWMmqFsnihrzMF-UtWz5C2-XuPElg8a_lBZBLNIMu-G1q6-FapdDo32dJIJZSKwkIm4j-6HCc7plQYEJn65iF6xvqBnM3z6_tWK3J3X8xlkHvpVUniRGvbjanOPDA1XBmaOFyN-GjfVdl-2F38BguPO8RcdidnvG4p-eSvjvDZ4utfVp2iLj-6lcDG4RXgHnOl-Ggyv-exwL6-qcpL8QZVGrSSjdecjfvjG572TUjho2RvvZ5rKSiqVPUymejRusJyukWmyl_6M=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "TgFlashRobot")
    SUPPORT = os.environ.get("SUPPORT", "TgFlash") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TgFlash94") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/2752523b23793a09d9c63.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/2752523b23793a09d9c63.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5467311248")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', "True") # Change it to "True"
    

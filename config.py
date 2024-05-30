import os


class Config(object):
    API_HASH = os.environ.get("e4195bedc71234a179a3d9ac0cad6401")
    BOT_TOKEN = os.environ.get("7254134104:AAEp5yxJMnTSQGyJ3kXxfVh65hlVyAjITf8")
    TELEGRAM_API = os.environ.get("24871620")
    OWNER = os.environ.get("5728398903")
    OWNER_USERNAME = os.environ.get("ashish")
    PASSWORD = os.environ.get("8472")
    DATABASE_URL = os.environ.get("mongodb+srv://ashisham029:<Teacher@274>@cluster0.2pxqhuu.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("-1002017765276")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("1-kv8FIMhRLMWe_jF3-v__qXzLF3o9f4q", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]

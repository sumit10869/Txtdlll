import os

API_ID = API_ID = 21513517

API_HASH = os.environ.get("API_HASH", "838d3451485b95722878921877f12066")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6586848968:AAFUvpnjYVuC5lQ92wOKyTQW1M6HShdOYuE")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5904348755))

LOG = -1002035739827

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5904348755").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)



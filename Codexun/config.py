## Disclaimer By Team AIMusicX

## Don't try to edit this file otherwise your bot will be crash.

from os import getenv

from dotenv import load_dotenv

load_dotenv()

que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCE9Ll8CjjHsWVLGDYI4YKStjrzFfJDDZdMl89W-9cRnHVycMki0hdDEVJQ0UE0wUniTap9MkpmimOHfElY9kP9ZyDO_gR3mWwy-qZVekvcJpTI1WnSMw0XZ4ik8Xbayb7_o4J5cPXpni6qcqPSnx418fV_HHiKohtc_bQoAwfAcfNKL0n2E_zadlMeQeT0giEuboiPsKGfeYgSdqo6lll9G0gK44lOeX0vsLC6vuKASUkfQqQtJnFNknox_BqMsxYsvZQeEnRLzlUvmtfb5bWiC68nFGR1WE1oaAdfj4CY-FcA48IY1L-RxC6mCSk6BgW8Fn2Ho-7KiF6FYt8TyRHxbmUSywA")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSID = int(getenv("ASSID"))
ASSNAME = getenv("ASSNAME")
ASSUSERNAME = getenv("ASSUSERNAME")
BOT_ID = int(getenv("BOT_ID"))
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/LEGENDARY-OS/Noize")
USERS = getenv("2056407064")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
MONGO_DB_URI = getenv("MONGO_DB_URI")
API_ID = int(getenv("15235059"))
API_HASH = getenv("352269b9e97005ffbe7f577dd89911e6")
OWNER_ID = int(getenv("1805019557"))
UPDATE = getenv("UPDATE")
SUPPORT = getenv("SUPPORT")
START_IMG = getenv("START_IMG")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "100"))
CMD_MUSIC = list(getenv("CMD_MUSIC", "/ !").split())
BG_IMG = getenv("BG_IMG", "https://telegra.ph/file/f2a2d31f60a9e0f3dbe94.png")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1805019557").split()))
ASSISTANT_NAME = getenv("ASSNAME")
COMMAND_PREFIXES = ("/ ! .").split()
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/a085a3cea21f994264152.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")

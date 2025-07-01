# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# Netscape HTTP Cookie File
# http://curl.haxx.se/rfc/cookie_spec.html
# This is a generated file!  Do not edit.
.instagram.com	TRUE	/	TRUE	1785941855	datr	X_djaOHJfSmohPu43ZhyKmXQ
.instagram.com	TRUE	/	TRUE	1782917855	ig_did	C45C995A-0E37-49F9-8EC9-E23CC9729499
.instagram.com	TRUE	/	TRUE	1751986724	dpr	2.75
.instagram.com	TRUE	/	TRUE	1785941864	mid	aGP3XwABAAGjkTopPVrP1QE2BQnd
.instagram.com	TRUE	/	TRUE	1751986724	wd	393x746
.instagram.com	TRUE	/	TRUE	1785941917	csrftoken	ZB9A6nH1o80fDfEjxENovgK9oCqs8VyJ
.instagram.com	TRUE	/	TRUE	1759157917	ds_user_id	52436152532
.instagram.com	TRUE	/	TRUE	1782917906	sessionid	52436152532%3A3s0Fa81FyUotc5%3A11%3AAYd4WwwtTWtoFhBxXYfcj9z5pv2b0FzUoq2CnXPC-g
.instagram.com	TRUE	/	TRUE	0	rur	"CLN\05452436152532\0541782917916:01fe3873003449d79f3b3f0bc012a9b68076ce803dd8cd09a3a68d768b1d475af30d2a6e"

"""

YTUB_COOKIES = """
# Netscape HTTP Cookie File
# http://curl.haxx.se/rfc/cookie_spec.html
# This is a generated file!  Do not edit.

.youtube.com	TRUE	/	TRUE	1785943741	PREF	tz=Asia.Calcutta&f4=4000000
.youtube.com	TRUE	/	FALSE	1785404419	HSID	AAIiDfOFzPb_AhCs1
.youtube.com	TRUE	/	TRUE	1785404419	SSID	APj4cQGEZclgVypFV
.youtube.com	TRUE	/	FALSE	1785404419	APISID	7ehJbzWZdBftemYT/A0u5zVpLsKmb7qMj5
.youtube.com	TRUE	/	TRUE	1785404419	SAPISID	TrCFETwLd2NRok8X/Ahlc9cygC5eYHmkoj
.youtube.com	TRUE	/	TRUE	1785404419	__Secure-1PAPISID	TrCFETwLd2NRok8X/Ahlc9cygC5eYHmkoj
.youtube.com	TRUE	/	TRUE	1785404419	__Secure-3PAPISID	TrCFETwLd2NRok8X/Ahlc9cygC5eYHmkoj
.youtube.com	TRUE	/	FALSE	1785404419	SID	g.a000yQiazf4upKlDqg__D_pxf9BWDFaWTCHXrxl2YcwLSoSXFpbKEQamDke6cNO2uN5F--OR8QACgYKAVoSARYSFQHGX2MiMmjOxcsqshkYstwFh45pDBoVAUF8yKpHmR_mNHsTiu6D0oOHJW1f0076
.youtube.com	TRUE	/	TRUE	1785404419	__Secure-1PSID	g.a000yQiazf4upKlDqg__D_pxf9BWDFaWTCHXrxl2YcwLSoSXFpbKfl9N6E8OfRVJHqYKsUHxHwACgYKASESARYSFQHGX2MiLPu71S3VXWEFSx0549fWahoVAUF8yKoPHwvWixylMh8LOVEu6gAj0076
.youtube.com	TRUE	/	TRUE	1785404419	__Secure-3PSID	g.a000yQiazf4upKlDqg__D_pxf9BWDFaWTCHXrxl2YcwLSoSXFpbK6osFbthK8UbO8LgP7v-B_QACgYKAV8SARYSFQHGX2MiEqUAbNoyNk3Gpzj1Wu3F5RoVAUF8yKp4ZbIBa3eDv79u71OiKFSv0076
.youtube.com	TRUE	/	TRUE	1785404420	LOGIN_INFO	AFmmF2swRQIhAMRJenB_8yFe8c7fyduLY8wWLVqWJdUbbDMW4B-iKOvlAiB7p3FEUmej8nOt0x1oOC7Qs89543KKZl_BNPtJKHBKIg:QUQ3MjNmeTV2Vm53RWNHV01wTmUwR01jTklIT3lRNjhCQ3FIYjZ0SkVGem9lWVhndkhnU0NQYkZEdHJzZTlfajdMamN2THcxVUZ4V2UxRmU3Vzc5LXl5dnRIeDcxRlRob3JyQm9QYTM4YmtMLVVRMDUtaU1OYWNOTUw3VElSckp4RDZoMEhHTndpbGtNWkpWM19SczM0eUZyUHU4YTJlZW1n
.youtube.com	TRUE	/	TRUE	1782919746	__Secure-1PSIDTS	sidts-CjIB5H03P-4eaNPIrvrNFovaov0FhnPOLR5-NdsvRK79iKF60E_B1jeqppwd0unYbt26PxAA
.youtube.com	TRUE	/	TRUE	1782919746	__Secure-3PSIDTS	sidts-CjIB5H03P-4eaNPIrvrNFovaov0FhnPOLR5-NdsvRK79iKF60E_B1jeqppwd0unYbt26PxAA
.youtube.com	TRUE	/	FALSE	1782919748	SIDCC	AKEyXzVprLdDSHC8m7wStWPdgBF7hkVVn-Xvs6QC3y4MSPWR0NpNl3DpdBLc3ccTHW5cw-4nVA
.youtube.com	TRUE	/	TRUE	1782919748	__Secure-1PSIDCC	AKEyXzUI4xWOGSM5BH0-6ahxmvWR8YDPByO2FAywdm41jjvpidMziE9B4xZO3Fdw0fJuJBtC
.youtube.com	TRUE	/	TRUE	1782919748	__Secure-3PSIDCC	AKEyXzUxbC7OwiqsXcJ5cyZ-1h9DQvTWNl1XoG7Wr0QHo0rWWx8u1U4t6LqK91PrIyjlz0Mo

"""

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
MONGO_DB = getenv("MONGO_DB", "")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "3"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)

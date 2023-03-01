import gspread, os, json
from pushbullet import PushBullet

#Corporate Proxy Self Signed Certificate Workaround
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#Pushbullet config
pb = PushBullet(os.environ['PB_KEY'])

#Google Cloud Key Config
credentials = json.loads(os.environ['GC_CRED'])

#Access Google Sheets file
gc = gspread.service_account_from_dict(credentials)
wks = gc.open("Equity Analysis Template").worksheet("Alerts")
val = wks.get('L2').first()
if val=="TRUE":
    pb.push_note("Check alerts worksheet",val)
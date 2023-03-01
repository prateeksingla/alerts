import gspread
from pushbullet import PushBullet
from sec import sec
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
pb_key = sec.get('PB_KEY')
pb = PushBullet(pb_key)
gc = gspread.service_account(filename='alerts.json')
wks = gc.open("Equity Analysis Template").worksheet("Alerts")
val = wks.get('L2').first()
if val=="TRUE":
    pb.push_note("Check alerts worksheet",val)
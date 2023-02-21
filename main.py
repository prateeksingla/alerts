import gsheets
import os
 
# printing environment variables
print(os.environ)
SHEET_NAME = 'Alerts'



# gc = gspread.service_account('credentials.json')
# spreadsheet = gc.open_by_key(SHEET_ID)
# worksheet = spreadsheet.worksheet(SHEET_NAME)
# rows = worksheet.get_all_records()
# print(rows[:5])

# print('==============================')
# df = pd.DataFrame(rows)
# print(df.head())
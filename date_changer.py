import datetime

created_date = '26-12-2024'
issue_date = '31-12-24'
created_date_date = int(created_date[0:2])
created_date_month = int(created_date[3:5])
created_date_year = int(created_date[6:])
temp_created_date = datetime.date(created_date_year, created_date_month, created_date_date)
#print('Created date:', created_date[0:5])
print('Created date:', temp_created_date)
print('Issue date:', issue_date[0:5])
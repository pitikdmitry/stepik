from datetime import datetime


str = "10/01/2002 12:47:08 PM"
datetime_object = datetime.strptime(str, '%d/%m/%Y %H:%M:%S %p')
print(datetime_object.year)

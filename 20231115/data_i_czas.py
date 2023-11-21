from datetime import date, datetime

dzisiaj = date.today()
teraz = datetime.now()

wigilia = date(2023,12,11)
print (dzisiaj)
print (teraz)
print(repr(teraz))

print(teraz.isocalendar())
print(teraz.tzname())


print(teraz.strftime('%Y-%m-%d'))
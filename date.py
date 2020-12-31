def check_leap(y):
    return (y%400==0) or (y%4==0 and y%100!=0)


def check_date(day , mon ,year,l,ml):
    if mon < 1 or mon > 12:
        return False 
    if day > ml[mon-1]:
        if not (day == 29 and l and mon==2):
            return False
    if year > 2012 or year<1812:return False
    return True


day,month,year=[1,1,1812]
month_len=[31,28,31,30,31,30,31,31,30,31,30,31]
leap=True

while True:
    try:
        day,month,year=map(int,input("Enter date as dd/mm/yyyy: ").split('/'))
    except:
        print("Invalid input!")
        continue
    leap=check_leap(year)
    if check_date(day,month,year,leap,month_len): break
    print("Invalid Date!")

if day < month_len[month-1] or (month==2 and day==28 and leap):
    day=day+1
else:
    day=1
    if month<12: month=month+1
    else:
        month=1
        year=year+1
print("{:02d}/{:02d}/{}".format(day,month,year))

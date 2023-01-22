month = int(input("Please enter month id from 1 to 12 : "))
mlist = ["зима", "весна", "лето", "осень"]
while True:
    if month > 12 or month <= 0 :
        print(f"\tINCORRECT ID!!! \n\tPlease use number range from 1 to 12 only!")
        month = int(input("Please enter month id from 1 to 12 : "))
        continue
    mlist = ["зима", "весна", "лето", "осень"]
    if month == 12 or (month >= 1 and month < 3):
        print(f"\tSeason related to your Month id#{month}  is '{mlist[0]}'")
        break
    elif month >= 3 and month < 6:
        print(f"\tSeason related to your Month id# {month} is '{mlist[1]}'")
        break
    elif month >= 6 and month < 9:
        print(f"\tSeason related to your Month id# {month} is '{mlist[2]}'")
        break
    elif month >= 9 and month < 12:
        print(f"\tSeason related to your Month id# {month} is '{mlist[3]}'")
        break

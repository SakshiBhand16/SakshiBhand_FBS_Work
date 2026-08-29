days = int(input("Enter days: "))

years = days // 365
weeks = days % 365 // 7
days = (days % 365)%7

print('Years:', years)
print('Weeks:', weeks)
print('Days:', days)
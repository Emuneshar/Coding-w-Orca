from datetime import date

year = int(input("What year were you born?"))
month = int(input("What month were you born in?"))
day = int(input("What day were you born?"))

birthday = date(year, month, day)

today = date.today()

difference = today - birthday

days = difference.days

print(f"You are {days} Earth days old")

mercuryDays = days / 58.6

venusDays = days / 243

marsDays = days / 1.02

moonDays = days / 27.32

saturnDays = days/0.42

jupiterDays = days / 0.41

uranusDays = days / 0.67

neptuneDays = days / 0.72


print(f"You are {mercuryDays} Mercury days old")
print(f"You are {venusDays} Venus days old")
print(f"You are {marsDays} Mars days old")
print(f"You are {moonDays} Moon days old")
print(f"You are {saturnDays} Saturn days old")
print(f"You are {jupiterDays} Jupiter days old")
print(f"You are {uranusDays} Uranus days old")
print(f"You are {neptuneDays} Neptune days old")
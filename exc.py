#this file exixts in sub branch

principle = 0
time = 0
rate = 0

while principle <= 0:
    principle = float(input("enter yout principle: "))
    if(principle <= 0):
        print("principle cant be zero or less, pls reprompt it")

while rate <= 0:
    rate = float(input("enter your intreset rate: "))
    if rate <= 0:
        print("intreset rate cant be zero, pls repormpt it")
    elif  rate > 0 and rate <= 2:
        print("intreset rate is too low")

while time <= 0:
    time = int(input("enter your duration in years: "))
    if time <= 0:
        print("your duration period is invalid")
    elif time <= 6:
        print("duration is short")



print(f"your principle is {principle}")
print(f"your intrest rate is {rate}")
print(f"your duration is {time}")

final = principle*pow((1+rate/100),time)
print(f"your final amount is {round(final,2)}")
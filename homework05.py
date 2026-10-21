# 1)
name=input("enter your name")
last_name=input("enter your last_name")
age=input("enter your age")
print("hello my name is" + name + last_name + " and i am" + age + " years old")

# 2)
price_1=int(input("enter price 1: "))
price_2=int(input("enter price 2: "))
price_3=int(input("enter price 3: "))
total=price_1+price_2+price_3
print("total: ", total) 

# 3)
current_age = int(input("Enter your current age "))
years = int(input("Enter number of years "))
future_age = current_age + years
print("In " + str(years) + " years you will be " + str(future_age) + " years old")

#4)
distance=int(input("enter distance in km: "))
time=int(input("enter time"))
speed=distance/time
print("speed: ", speed)

#5)
distance=int(input("enter distance in km: "))
fuel=distance*8/100
print("fuel:", fuel)

#6)
km=int(input("enter distance in km: "))
fuel=int(input("enter fuel for 100km: "))
price=int(input("enter price per liter: "))
total_fuel=km * price/100
total_price=fuel * price
print("total_fuel: " , total_fuel)
print("total_price" , total_price)

#7)
hourly_rate=int(input("enter hourly rate in GEL: "))
hours_worked=int(input("enter worked hours in a week"))
weekly_salary=hourly_rate * hours_worked
print("weekly_salary", weekly_salary)

#8)
price=int(input("enter price in GEL: "))
people=int(input("enter number of people: "))
share=price//people
remainder=price % people
print("each person gets ", share)
print("remaining money ", remainder)

#9)
original_price=int(input("enter original price "))
discount_percent=int(input("enter discount percentage "))
discount=original_price*discount_percent/100
final_price=original_price-discount_percent
print("discount",discount)
print("final_price",final_price)

#10)
page=int(input("enter total pages of book "))
pages_per_day=int(input("enter pages read per day "))
days_needed=page/pages_per_day
print("days need to finish book ", days_needed)
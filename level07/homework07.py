# 1)
# input ფუნქცია გამოიყენება იმისთვის რომ მომხმარებელს შემოვაყვანინოთ მონაცემები ტერმინალიდან. 

# 2)
# type casting არის მონაცემთა ტიპის შეცვლა.

# 3)
#int- მთელი რიცხვი მაგ:6,2,9
#float-ათწილადი რიცხვი მაგ:2.5,3.5,8.14
#str-ტექსტი მაგ:"გამარჯობა"
#bool-ლოგიკური ტიპი მაგ:true,false

# 4)
# ==  ტოლია
# !=  არ არის ტოლი
# >   მეტია
# <   ნაკლებია
# >=  მეტია ან ტოლია
# <=  ნაკლებია ან ტოლია

# 5)
num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
print("მეტია (>):", num1 > num2)
print("ნაკლებია (<):" ,num1 < num2)
print("მეტია ან ტოლია(>=):", num1 >= num2)
print("ნაკლებია ან ტოლია(<=):", num1 <= num2)
print("ტოლია(==):" ,num1 == num2)
print("არ არის ტოლი(!=):" , num1 != num2)

# 6)
age = int(input("Enter your age: "))
is_adult = age >= 18
print("Is 18 or older:", is_adult)

# 7)
speed=int(input("Enter car speed (km/h): "))
distance=int(input("Enter distance to travel (km): "))
allowed_time=int(input("Enter planned time (hours): "))
needed_time=distance / speed
is_in_time=needed_time <= allowed_time
print("Needed time:", needed_time, "hours")
print("Will it arrive on time:", is_in_time)

# 8)
p1=int(input("First product price: "))
p2=int(input("Second product price: "))
p3=int(input("Third product price: "))
money=int(input("How much money do you have: "))
total_price=p1 + p2 + p3
is_enough = money >= total_price
print("Total cost:", total_price)
print("Is there enough money:", is_enough)

# 9)
program_size=float(input("Enter program size (GB): "))
free_space=float(input("Enter free space on computer (GB): "))
is_enough_space = free_space >= program_size
print("Is there enough free memory:", is_enough_space)

# 10)
math=int(input("Math grade: "))
history=int(input("History grade: "))
art=int(input("Art grade: "))
average=(math + history + art) / 3
is_good=average > 5
print("Arithmetic average:", average)
print("Is average greater than 5:", is_good)

# 11)
# 1 კოდი:
# შეცდომა: num1 არის სტრიქონი (str), ხოლო num2 არის მთელი რიცხვი (int)
# ტექსტის და რიცხვს მიმატება არ შეიძლება
# სწორი ვერსია:
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
result = num1 + num2
print(result)

# 2 კოდი:
# შეცდომა: "5" ბრჭყალებშია და არის ტექსტი მისი გამრავლება ათწილად რიცხვზე და რიცხვის გამოკლება არ შეიძლება
# სწორი ვერსია:
num1=int(input("Enter first number: "))
num2=float(input("Enter second number: "))
result=num1 - 5 * num2
print(result)

# 3 კოდი:
# შეცდომა: hours და bonus არის input-ით მიღებული სტრიქონები (str), 
# რომლებზეც გამრავლება და მიმატება არ იმუშავებს. ასევე, "2" არის ტექსტი და გაყოფა ვერ შესრულდება.
# სწორი ვერსია:
hours=float(input("Enter hours worked: "))
rate=float(input("Enter hourly rate: "))
bonus=input("Enter bonus: ")
salary=hours * rate
total=salary + float(bonus)
final_salary=total / 2     
print(final_salary)

# 4 კოდი:
# შეცდომა: quantity-თან უნდა ეწერპს int(). "10"ბრჭყალებშია (ტექსტია). მათემატიკური მოქმედებები მათზე არ მუშაობს
# სწორი ვერსია:
price=float(input("Enter product price: "))
quantity=int(input("Enter quantity: "))
discount=float(input("Enter discount percentage: "))
subtotal=price * quantity
discount_amount=subtotal * discount
final_price=subtotal - 10 
print(int(final_price))

# 5 კოდი:
# შეცდომა: num2 არის სტრიქონი (type casting არ არის გამოყენებული), ამიტომ num1-თან მიმატება არ გამოვა 
# ასევე, დარჩენილის (modulo %) გამოსათვლელად გამოყენებული "2" არის ტექსტი.
# სწორი ვერსია:
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=float(input("Enter third number: "))
total=num1 + num2
average=total / num3
remainder=average % 2
result=int(remainder + num1)
print(result)
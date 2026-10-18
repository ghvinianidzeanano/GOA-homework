# 1)
# მიმატება(+) - კრებს ორ ან მეტ რიცხვს
# გამოკლება(-) - აკლებს მეორე რიცხვს პირველს
# გამრავლება(*) - ამრავლებს რიცხვებს ერთმანეთზე
# გააყობა(/) - ყოფს პირველ რიცხვს მეორეზე და ჯამია ათწილადი
# სრული გაყოფა(//) - ყოფს პირველ რიცხვს მეორეზე და ჯამია მთელი რიცხვი
# ნაშთის პოვნა (%) - აბრუნებს გაყოფის შემდეგ დარჩენილ ნაშთს
# ხარისხში აყვანა (**) - აყავს რიცხვი ხარისხში

# 2)
number=int(input("enter number"))
square=number ** 2
cube=number ** 3
print("the square of", number, "is", square)
print ("the cube of ", number, "is", cube)

# 3)
num1=int(input("enter number"))
num2=int(input("enter number"))
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1//num2)
print(num1%num2)
print(num1**num2)

# 4)
candies = int(input("enter candies: "))
print("A. boxes:", candies // 12)
print("B. left:", candies % 12)

# 5)
minutes = int(input("enter minutes: "))
print("A. hours:", minutes // 60)
print("B. minutes left:", minutes % 60)
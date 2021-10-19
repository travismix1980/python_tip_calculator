#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

# Python Simple Tip Calculator

# greeting
print("Welcome to the Tip Calculator")

# get bill total
total = input("Input total bill amount: ")

# get tip amount
tip = input("What percentage tip do you want to give (15, 18, 20) ")

# get number of people to split bill between
people = input("How many people do you want to split the bill between ")

# output amount each person has to pay
# fix tip for calculation
tip_amount = str("1." + tip)

#convert values to float
tip_amount = float(tip_amount)
people = float(people)
total = float(total)

each_pay = total * tip_amount / people

# round to 2 decimal places
each_pay = round(each_pay, 2)

# force show zeros 
each_pay = format(each_pay, ".2f")

print(f"Each person pays: ${each_pay}")
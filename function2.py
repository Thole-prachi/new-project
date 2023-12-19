def cheese_and_crackers(cheese_count, boxex_of_crackers):  #define function of cheese and crackers count for party
    print(f"you have{cheese_count} cheese!")
    print(f"you have {boxex_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket. \n")

print ("we can just give the function numbers directly: ")  # passint the function value directy in code
cheese_and_crackers(20,30)

print("Or , we can use variables from our script: ") # passing it by using variables
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers (amount_of_cheese, amount_of_crackers) #perform the math with count availabel of both.

print("we can even do math inside too :")
cheese_and_crackers (10 + 20, 5+6)

print("And we can combine the two, varibale and math: ")  # combination of math and variable value.
cheese_and_crackers (amount_of_cheese +100, amount_of_crackers + 1000)


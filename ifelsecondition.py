#using the example of age limit to vote in india is 18

age = 20
if age > 18:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")

#multiple if statements

if age > 18:
    print("Eligible to vote")
elif age == 18:
    print ("Can apply for voter id")
else:
    print ("Not eligible to vote")

#Nested if

if age > 18:
    print("Eligible to vote")
    if age >= 60:
        print("Need voting assisstance")
    else:
        print("Do not need assisstance")
elif age == 18:
    print ("Can apply for voter id")
else:
    print ("Not eligible to vote")

#for loop is used in iteration

#syntax

for i in range (10):
    print(i+1)

list2 = [1,2,3,4,5,6,7,8]

for i in list2:
    if i == 6:
        print("6 is available")
        break #Terminates the loop when the condition is satisfied

print ("Loop is completed")

#            (range1, range2, icrement/decrement)  
for i in range(5, 10, 2):
    print("Farheen")
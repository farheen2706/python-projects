def vote(age):
    match age:
        case 18:
            print ("Apply ID card")
        case 30:
            print("Eligible to vote")
        case 60:
            print ("You are a senior citizen")

vote(18)

#Method 2

def vote1 (age):
    switch = {
        18: "Apply ID Card",
        30: "ELigible to vote",
        60: "Senior Citizen" }
    
    return switch.get (age, "Nothing")

print(vote1(30))
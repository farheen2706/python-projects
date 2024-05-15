def vote(age):
    match age:
        case 18:
            print ("Apply ID card")
        case 30:
            print("Eligible to vote")
        case 60:
            print ("You are a senior citizen")

vote(18)
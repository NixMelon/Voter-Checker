# A program to check if a person is eligible to vote in Ghana or not
# ______________variables________________________
# 18 + years old
# name
# gender
# ____________program_____________________________

voter_name = input("Enter your name: ")
voter_age = int(input("Enter your age: "))
voter_gender = input("Enter your gender: ")
country = input("Enter your country: ").lower()

if voter_age >= 18 and country == "ghana":
    print(f"{voter_name} is eligible to vote.")
    
else:
    print(f"{voter_name} is not eligible to vote.")
    if voter_age < 18:
        print(f"{voter_name} is too young to vote.")
        
    elif voter_age >= 18 and country != "ghana":
        
        print(f"{voter_name} is not from Ghana.")
    elif voter_gender != "male" or voter_gender != "female":
        print(f"{voter_name} is not a valid gender.")
    else:
        print(f"{voter_name} is not from Ghana.") 
    
    
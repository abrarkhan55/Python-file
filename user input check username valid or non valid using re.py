import re
user=input("Enter username:")
if re.match(r"^\w{5,15}$",user):
    print("valid")
else:
    print("Non valid")
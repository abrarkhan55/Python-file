#phone number set
import re
Phone=input("Enter Phone Number :")
if re.match(r"^(?:\+88)?01[3-9]\d{8,}$",Phone):
    print("valid")
else:
    print("invalid")
#mail validation using re

import re
Mail=input("Enter Your Mail:")
if re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$",Mail):
    print("valid")
else:
    print("invalid")
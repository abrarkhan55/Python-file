import re
Abbu=r"father"
Ammu="my father is my idol ."
Vaiya=re.search(Abbu,Ammu)


if Vaiya:
    print(Vaiya.start())
    print(Vaiya.end())
    print(Vaiya.span())
    print(Vaiya.group())
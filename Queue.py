from collections import deque
bank= deque(["Abrar","Rakib","Omar"])
print(bank)
bank.popleft()
print(bank)
bank.popleft()
print(bank)
bank.popleft()

if not bank:
    print("Not in Line ")

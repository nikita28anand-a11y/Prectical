salary = int(input("enter salary:"))
if salary > 50000:
    print("your bonus is 20%")
elif salary > 30000 and salary <= 50000:
    print("your bonus is 10%")
else:
    print("your bonus is 5%")
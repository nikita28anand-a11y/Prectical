n = 12345
# output 54321
n = str(n)
print(n[::-1])

# rev
n = 12345
rev = 0
while n > 0:
    d =n%10
    rev = rev*10 + d
    n = n//10
print(rev)


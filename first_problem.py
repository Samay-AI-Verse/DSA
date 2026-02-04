



nums = [12,345,2,6,7896]
result = 0
for x in nums:

    digits = len(str(abs(x)))

    if digits % 2 == 0:
        result += 1

        
print(result)





def maxNum(*numbers):
       
        max = numbers[0]

        for num in numbers:
            if max < num:
                max = num

        return max

print(maxNum(1, 2, 3))
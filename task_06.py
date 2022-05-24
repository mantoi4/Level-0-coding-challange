def biggestNum(*numbers):
       
        max = numbers[0]

        for num in numbers:
            if max < num:
                max = num

        return max

print(biggestNum(1, 2, 3))



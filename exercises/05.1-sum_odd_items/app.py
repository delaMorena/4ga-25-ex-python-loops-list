arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:


def sumOdds(item):
    odd_number = 0
    for i in arr:
        if (i % 2 != 0):
            odd_number = sum(i)
        return odd_number
        
print(sumOdds(arr))

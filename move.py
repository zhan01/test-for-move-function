def min(numbers):
    min = numbers[0]
    for number in numbers:
        if number < min:
            min = number
    return min

def move(numbers, idx):
    return [numbers[idx]] + numbers[:idx] + numbers[idx + 1:]


numbers = [10, 15, 3, 6, 7, 1, 3, 9, 12]
print("Numbers = ",numbers)

assert move([10, 15, 3, 6, 7, 1, 3, 9, 12],1) == [15, 10, 3, 6, 7, 1, 3, 9, 12]
assert move([10, 15, 3, 6, 7, 3, 9, 12],4) == [7, 10, 15, 3, 6, 3, 9, 12]
assert move([10, 15, 3, 6, 7, 9, 12],3) == [6, 10, 15, 3, 7, 9, 12]
assert move([10, 15, 7, 9, 12],4) == [12, 10, 15, 7, 9]
assert move([10, 15, 9, 12],2) == [9, 10, 15, 12]

print("Index of 4 ",move(numbers,4))
print("Index of 3 ",move(numbers,3))
print("Index of 2 ",move(numbers,2))

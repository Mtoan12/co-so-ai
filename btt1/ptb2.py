import math
import random


# ax**2 + bx + c = 0

a = 1
b = -6
c = 5

number_of_solution = random.randint(2, 10)

index = 0

solutions = []

while index <= number_of_solution:
    solutions.append(random.randint(0, 15))
    index += 1

def result(x):
    return a*x**2 + b*x + c

def sortNearestZero(solutions):
    for i in solutions:
        for j in solutions:
            if abs(result(i)) > abs(result(j)):
                solutions[i], solutions[j] = solutions[j], solutions[i] 

    return solutions

def swapBitsTwoSolutions(solutions):
    while (True):
        solutions = sorted(solutions)

        if result(solutions[0]) == 0:
            return solutions[0]
        
        if result(solutions[1]) == 0:
            return solutions[1]
        
        number_of_bits = 5
        number_of_bits_to_swap = 3
        bit_of_first_solution = format(solutions[0], 'b').zfill(number_of_bits)
        bit_of_second_solution = format(solutions[1], 'b').zfill(number_of_bits)

        subString1 = bit_of_first_solution[number_of_bits_to_swap - 1: number_of_bits - 1]
        subString2 = bit_of_second_solution[number_of_bits_to_swap - 1: number_of_bits - 1]

        new_first_bits = bit_of_first_solution.replace(subString1, subString2)
        new_second_bits = bit_of_second_solution.replace(subString2, subString1)

        solutions[0] = int(new_first_bits, 2)
        solutions[1] = int(new_second_bits, 2)
        


print(solutions)
print(swapBitsTwoSolutions(solutions))


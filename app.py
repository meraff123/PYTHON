def multiply(*numbers):
    total = 1
    for num in numbers:  # Changed 'numbers' to 'num' to avoid reusing the parameter name
        total *= num
    return total


# Call the function
result = multiply(2, 3, 4, 5)
print(result)  # Output: 120

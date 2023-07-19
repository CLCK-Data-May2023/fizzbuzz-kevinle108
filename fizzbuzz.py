# Week 2: Bonus (Python_1)

def fizz_buzz(num):
    result = ""
    if num % 3 == 0:
        result += "Fizz"
    if num % 5 == 0:
        result += "Buzz"
    if len(result) == 0:
        result = str(num)
    return result

finish = [print(fizz_buzz(num)) for num in range(1, 101)]

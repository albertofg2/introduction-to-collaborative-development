data = list(range(1, 101))  # Do not modify this line... I will know if you do!

log = []

for num in data:
    if num % 3 == 0 and num % 5 == 0:
        log.append("FizzBuzz")
    elif num % 3 == 0:
        log.append("Fizz")
    elif num % 5 == 0:
        log.append("Buzz")
    else:
        log.append("idk")

print(log)

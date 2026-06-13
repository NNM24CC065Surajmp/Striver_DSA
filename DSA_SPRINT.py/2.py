

numbers  = []
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    numbers.append(num)

print("Total:", sum(numbers))
print("Average:", sum(numbers) / len(numbers) if numbers else 0)
print("Count:", len(numbers))
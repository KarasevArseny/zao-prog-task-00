nums_input = input("Введите числа через пробел: ")
nums = [int(x) for x in nums_input.split()]

target = int(input("Введите целевое число: "))

found = False
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(f"[{i}, {j}]")
            found = True
            break
    if found:
        break
    
if not found:
    print("None")
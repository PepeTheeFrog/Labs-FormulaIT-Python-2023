numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
index_none = 0
sum_ = 0
for item in range(len(numbers)):
    if numbers[item] is None:
        index_none = item
    else:
        sum_ += numbers[item]
numbers[index_none] = sum_ / len(numbers)
print("Измененный список:", numbers)

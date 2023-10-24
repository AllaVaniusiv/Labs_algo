from function import is_monotonic

array1 = [1, 2, 3, 4, 5]
array2 = [5, 4, 3, 2, 1]
array3 = [1, 2, 2, 3, 4]

result1 = is_monotonic(array1)
result2 = is_monotonic(array2)
result3 = is_monotonic(array3)

print(f"Array 1 is monotonic: {result1}")
print(f"Array 2 is monotonic: {result2}")
print(f"Array 3 is monotonic: {result3}")

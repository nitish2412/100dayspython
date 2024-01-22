list_of_strings = input().split(',')
result = [int(num) for num in list_of_strings if int(num)%2 == 0]

print(result)

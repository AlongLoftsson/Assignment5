n = int(input("Enter the length of the sequence: ")) # Do not change this line

first_number = 0
second_number = 1
third_number = 0
temp_one = 0
temp_two = 0

for i in range(1,n+1):
    temp_one = third_number
    temp_two = second_number
    third_number = third_number + second_number + first_number
    second_number = temp_one
    first_number = temp_two
    print(third_number)
        
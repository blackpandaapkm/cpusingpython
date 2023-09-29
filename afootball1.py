# Read the input string
s = input()

# Initialize variables to count consecutive players
count_zero = count_one = 0

# Iterate through the string
for player in s:
    if player == '0':
        count_zero += 1
        count_one = 0  # Reset the count for '1'
    else:
        count_one += 1
        count_zero = 0  # Reset the count for '0'

    
    if count_zero >= 7 or count_one >= 7:
        print("YES")
        break
else:
    print("NO")

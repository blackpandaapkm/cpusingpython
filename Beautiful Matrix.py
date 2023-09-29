matrix = []
for _ in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

row_with_one = -1
col_with_one = -1
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            row_with_one = i
            col_with_one = j

horizontal_moves = abs(2 - row_with_one) 
vertical_moves = abs(2 - col_with_one) 
total_moves = horizontal_moves + vertical_moves

print(total_moves)

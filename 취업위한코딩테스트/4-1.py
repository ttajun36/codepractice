n = int(input())
x,y = 1,1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            new_x = x + dx[i]
            new_y = y + dy[i]
            
    if new_x >= 1 and new_x <= n:
        x = new_x
    if new_y >= 1 and new_y <= n:
        y = new_y
    
    print(x, y)
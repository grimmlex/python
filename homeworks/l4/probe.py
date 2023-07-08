def get(n):
    turn_angle = 120 if n == 3 else (((n - 2) * 180) / n)
    result = turn_angle
    print(turn_angle)
    print(round(result, 2))



get(7)
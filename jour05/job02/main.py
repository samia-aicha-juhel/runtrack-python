def draw_rectangle(width, height):
   for i in range(1, width + 1):
        for j in range(1, height + 1):
            if j == 1 or j == height:
                print("l", end="")
            elif i == 1 or i == width:
                print("-", end="")
            else:
                print(" ", end="")
        print()

draw_rectangle(10, 6)
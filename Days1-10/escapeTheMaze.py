#Running this in reeborgs world for the maze level will finish the maze
while(not at_goal()):
    if right_is_clear():
        for i in range(3):
            turn_left()
        move()
    elif front_is_clear() and wall_on_right():
        move()
    
    else:
        turn_left()
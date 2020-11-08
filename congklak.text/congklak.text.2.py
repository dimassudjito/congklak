# Iniating board
board = [4, 0, 1, 0, 0, 3]

def which_player(hole):
    if hole < len(board)/2:
        return "player1"
    else:
        return "player2"

def which_side(hole):
    if hole < len(board)/2:
        return "side1"
    else:
        return "side2"

# hole is index of the chosen hole
def move_seeds(hole):
    global board

    # Wrap around index
    if hole < 0:
        hole += len(board)

    # Moving the seeds
    hole_value = board[hole]
    i = 1
    # Seeds movement upper-bound range
    hole_range = hole_value + 1
    while i < hole_range:
        # Checking if the hole is an opponent's base
        if player == "player1" and (hole-i) == (len(board)/2):
            hole_range += 1
        elif player == "player2" and (hole-i) == 0:
            hole_range += 1
        else:
            board[hole-i] += 1
            board[hole] -= 1
        i += 1
    
    
    # Checking if the last hole is base
    if hole-hole_range+1 == 0 or hole-hole_range+1 == (len(board)/2):
        print("base, same player")
    # Checking if the last hole is empty
    elif board[hole-hole_range+1] != 1:
        # Continue movement otherwise
        move_seeds(hole-hole_value)
    else:
        # Checking which side is last hole
        last_hole = hole-hole_range+1
        if last_hole < 0:
            last_hole += len(board)
        side = which_side(last_hole)

        # Checking if the hole is opponent's base
        if player == "player1" and side == "side2":
            print("switch player")
        elif player == "player2" and side == "side1":
            print("switch player")
        # Else we check if opponent's adjacent hole is filled
        # If yes, then add all the seed and the seed in our last
        # hole and add it to the base
        else:
            if player == "player1":
                if board[-last_hole] != 0:
                    board[0] += board[last_hole] + board[-last_hole]
                    board[last_hole] = 0
                    board[-last_hole] = 0
            # Opponent's adjacent hole is -(last_hole-len(board))
            elif player == "player2":
                if board[-(last_hole-len(board))] != 0:
                    board[int(len(board)/2)] += board[last_hole] + board[-(last_hole-len(board))]
                    board[last_hole] = 0
                    board[-(last_hole-len(board))] = 0
            print("switch player")
    

    
    return

hole = 2
player = which_player(hole)
move_seeds(hole)
print(board)
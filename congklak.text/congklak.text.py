# Iniating board
board = [0, 2, 2, 0, 2, 2]

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
    for i in range(1, hole_value+1):
        board[hole-i] += 1
        board[hole] -= 1
    
    # Checking if the last hole is empty
    if board[hole-hole_value] != 1:
        move_seeds(hole-hole_value)
    else:
        # Checking which side is last hole
        last_hole = hole-hole_value
        if last_hole < 0:
            last_hole += len(board)
        side = which_side(last_hole)

        # Checking if the hole is opponent's base
        if player == "player1" and side == "side2":
            print("player 2's turn")
        elif player == "player2" and side == "side1":
            print("player 1's turn")
        else:
            print("Add last_hole and accros hole to your base")
    

    
    return

hole = 5
player = which_player(hole)
move_seeds(hole)
print(board)
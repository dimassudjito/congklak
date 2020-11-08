import copy

# Iniating board
board = [0, 2, 2, 0, 2, 2]
half_total_seeds = sum(board)/2
base1 = 0
base2 = int(len(board)/2)

# Printing which player plays
def switch_player():
    if player=="player1":
        print("player 2")
    if player=="player2":
        print("player 1")

def print_last_hole(last_hole):
    print("The last hole is", str(last_hole))

# Displaying congklak board
def display():
    player2_board = copy.deepcopy(board[base2:len(board)])
    player2_board.reverse()
    player2_board.insert(0, '')

    player1_board = copy.deepcopy(board[0:(base2)])
    player1_board.append('')

    print(player2_board)
    print(player1_board)
    # print(board)
    print("------------")

# Indicate which player is playing
def which_player(hole):
    if hole < len(board)/2:
        return "player1"
    else:
        return "player2"

# Indicate which side the last hole is
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

    # Checking if the chosen hole is empty
    if hole_value == 0:
        print("please select a hole with a seed on it")
        return
    elif hole == base1 or hole == base2:
        print("please select a valid hole")
        return

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
        print("last hole is base, same player")
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
            switch_player()
            print_last_hole(last_hole)
        elif player == "player2" and side == "side1":
            switch_player()
            print_last_hole(last_hole)
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
            switch_player()
            print_last_hole(last_hole)
       
    return
if __name__ == "__main__":
    running = True
    while running:
        display()

        hole = int(input("Select hole: "))
        player = which_player(hole)
        move_seeds(hole)

        # Checking if base either player already wins
        if board[base1] > half_total_seeds:
            display()
            print("Player 1 Wins")
            running = False
        elif board[base2] > half_total_seeds:
            display()
            print("Player 2 Wins")
            running = False
from NQueens import board  

def Hill_Climbing(N=0,iteration = 100,debug=False):
    '''
    This program will utilize hill climibing algorithm to find
    solution for N Queens problem. For heuristic this progarm is using
    number of possible attacks with current placement of N queens.

    Goal is to find a configuaration of the board in which
    number of possible attack is/are zero.  
    '''
    # **********  state => configuration of board (randomly placed N queens)
    success = 0 # total success runs
    faliure = 0 # total failure runs
    random_restart = 0 # total random_restart
    total = iteration # total number of runs/iterations
    avg_steps_in_success = 0
    avg_steps_in_fail = 0
    for i in range(total):
        print("run ",i)
        # create a board with randomly placed N queens
        current = board(N)
        # as we want to minimize the number of attacks, we will select board
        # with lowest heuristic (number of attacks) value
        level = 0 # to count number of steps to reach result.
        while True:
            if debug: current.print_board()# to print the state/board
            if current.attacks==0: # found the goal state
                break
            possible_future_states = current.get_all_possible_future_boards()
            # loop through all the states and select state with
            # lowest heuristic (number of attacks) value
            next_state = current # possible next state (not moving forward if no better state is available)
            Min_attacks = current.attacks # currently minimum attack
            for state in possible_future_states:
                if state.attacks < Min_attacks:
                    Min_attacks = state.attacks
                    next_state = state
                
            if Min_attacks >= current.attacks:
                # if goal state is not reach
                # create new board (random restart)
                if not current.attacks==0:
                    current = board(N)
                    level+=1
                    random_restart += 1
                    continue
                # else:
                break
            else:
                current = next_state
                level+=1 # on to the next step so add a step
           
        if current.attacks==0:
            print('success')
            success+=1
            avg_steps_in_success += level
        else:
            # will never reach this
            print('fail')
            faliure += 1
            avg_steps_in_fail += level
    print("success rate=>",(success/total)*100,"%")
    print("average steps required for success=>",avg_steps_in_success/success)
    #print("average steps required for failure=>",avg_steps_in_fail/faliure)
    print("average random restarts required (random_restarts/iterations)=>",random_restart/total)
        


if __name__ == "__main__":
    N = input("give n for n queens Problem=>")
    try:
        N = int(N)
    except:
        print("please provide interger")
    Hill_Climbing(N,100,False)

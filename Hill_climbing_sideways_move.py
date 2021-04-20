from NQueens import board
import random

def Hill_Climbing(N=0,iteration = 100,debug=False,sideways_moves=1):
    '''
    This program will utilize hill climibing algorithm with sideways move to find
    solution for N Queens problem. For heuristic this progarm is using
    number of possible attacks with current placement of N queens.

    Goal is to find a configuaration of the board in which
    number of possible attack is/are zero.  
    '''
    # **********  state => configuration of board (randomly placed N queens)
    success = 0 # total success runs
    faliure = 0 # total failure runs
    total = iteration # total number of runs/iterations
    avg_steps_in_success = 0
    avg_steps_in_fail = 0
    for i in range(total):
        print("run ",i)
        # create a board with randomly placed N queens
        current = board(N)
        '''
        # as we want to minimize the number of attacks, we will select board
        # with lowest heuristic value (number of attacks), hence we will find minima
        '''
        level = 0 # to count number of steps to reach result.
        count_sideways_moves = 0 # counter for sideways move
        
        while True:
            if debug: current.print_board()# to print the state/board
            if current.attacks==0: # found the goal state
                break
            
            possible_future_states = current.get_all_possible_future_boards() # get all future 56 possible states
            states_with_same_H_value = [] # list to store states with same H-value as current
            next_state = current.get_copy_of_state() # variable to store next state if we find any state better than the current one
            '''
            # needed => (not necesssary to have) variable to stop storing equale H-value states
            #if we found a btter one than the current state in possible_future_states. 
            '''
            needed = True
            
            # loop through all the states and save all the states with same heuristic values (H-value)
            for state in possible_future_states:
                if state.attacks < current.attacks:
                    next_state = state
                    needed = False
                elif needed and state.attacks == current.attacks:
                    states_with_same_H_value.append(state)
                    
            # if next state is same as current state => there was no better state found.
            if next_state.is_same(current):
                
                len_of_states_with_same_H_value = len(states_with_same_H_value)
                if len_of_states_with_same_H_value > 0: # found some states with same H-value
                    # => it is a platue => can be sholder or can be flat local minima

                    if count_sideways_moves < sideways_moves: # if sideways moves is allowed
                        count_sideways_moves += 1  # increament counter for sideways moves
                        
                        # now select randomly one of state from states_with_same_H_value
                        r = random.randint(0,len_of_states_with_same_H_value - 1)
                        current = states_with_same_H_value[r] # change randomly selected state to current
                        level+=1 # increase the step counter
                    else:
                        # limit of sidways moves is up
                        break
                else:
                    # no better or equal H-value state found
                    # => found local minima => can be a gloabal minima
                    break
            else:
                # found a better state
                current = next_state # change next_state to current
                level+=1 # increase the step counter
                count_sideways_moves = 0 # reset the counter for sideways move


        print("level =>",level)
        if current.attacks==0:
            print('success')
            success += 1
            avg_steps_in_success += level
        else:
            print('fail')
            faliure += 1
            avg_steps_in_fail += level
    print("success rate=>",(success/total)*100,"%")
    print("average steps required for success=>",avg_steps_in_success/success)
    print("average steps required for failure=>",avg_steps_in_fail/faliure)
        


if __name__ == "__main__":
    N = input("give n for n queens Problem=>")
    try:
        N = int(N)
    except:
        print("please provide interger")
    Hill_Climbing(N,100,False,100)

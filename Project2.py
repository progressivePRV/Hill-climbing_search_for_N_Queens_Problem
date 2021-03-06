'''
Main project file

This will ask for input

'''
def print_Error(err):
    print("###### Error =>",err)



def main():
    # give number of queens (N)
    N = input("Give N for 'N-Queens' Problem=>")
    try:
        N = int(N)
    except:
        print("please provide interger")
        return
    # select one of the algorithm to perform
    print("Please select the algorithm:")
    print("1) Hill climbing search ")
    print("2) Hill-climbing search with sideways move")
    print("3) Random-restart hill-climbing search without sideways")
    print("4) Random-restart hill-climbing search with sideways")
    option = input("=>")
    try:
        option = int(option)
        if option>4 or option<1:
            raise Error("problem")
    except ValueError:
        print_Error("please provide interger")
        return
    except:
        print_Error("please provide interger between 1 to 4 (inclusive)")
        return
    # number of time algorithm should run
    total_runs = input("Give the number of iterations=>")
    try:
        total_runs = int(total_runs)
    except:
        print_Error("please provide interger")
        return
    # option to select whether to see states or not
    debug = input("Do you want to see the steps (selected states)? y/n [n - default]=>")
    if debug=='y':
        debug=True
    else:
        debug=False

    def ask_for_side_ways_moves():
        moves = input("please provide sideways moves limit (>0 and <100) [default 100]=>")
        try:
            moves = int(moves)
            if moves>4 or moves<1:
                raise Error("problem")
            return moves
        except ValueError:
            print_Error("please provide interger")
            return 100
        except:
            print_Error("please provide interger between 0 and 100 (exclusive)")
            return 100
    '''
    after all the validations go with the selected algorithm
    ''' 
    if option==2:
        print("chossing Hill-climbing search with sideways move")
        sideways_moves = ask_for_side_ways_moves()
        print("set limit on side ways moves  to :",sideways_moves)
        
        from Hill_climbing_sideways_move import Hill_Climbing
        Hill_Climbing(N,total_runs,debug,sideways_moves)
         
        pass
    elif option==3:
        print("chossing Random-restart hill-climbing search without sideways")
        from Hill_climbing_random_restart import Hill_Climbing
        Hill_Climbing(N,total_runs,debug)
        pass
    elif option==4:
        print("chossing Random-restart hill-climbing search with sideways")
        sideways_moves = ask_for_side_ways_moves()
        print("set limit on side ways moves  to :",sideways_moves)
        
        from Hill_climbing_sideways_move_random_restart import Hill_Climbing
        Hill_Climbing(N,total_runs,debug,sideways_moves)
        pass
    else:
        print("chossing Hill climbing search ")
        
        from Hill_climbing import Hill_Climbing
        Hill_Climbing(N,total_runs,debug)
    input("\n press any character")

if __name__ == '__main__':
    main()

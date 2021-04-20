import random

class board:
    '''
        Its requires N (int) as input.
        N represents number of queens on the NxN board.
        N queens will be placed randomly on NxN board.
        There will be only one queen in each colum.
    '''


    def __init__(self, N=0):
        self.alternate = "-" # alternative charcter for black space
        self.queen_charcter = 'Q'
        if N==0:
            pass
        else:
            self.n = N
            self.queens_positions = [] # from left to right colums
            self.board = []
            # generating empty board
            for i in range(N):
                x = [self.alternate for i in range(N)]
                self.board.append(x)
            # placing N queens randomly in each colum
            for i in range(N):
                t = random.randint(0,N-1)
                self.board[t][i]= self.queen_charcter
                self.queens_positions.append([t,i])
            self.attacks = self.__count_attacks()
##            self.print_board()


    def print_board(self):
        # print the generated board
        for i in self.board:
            print("|",end="")
            print(" ".join(i),end="")
            print("|")
        print("total attacks in this board=>",self.attacks)

    def set_the_board(self,board):
        self.board = board
        self.n = len(board)
        self.queens_positions = self.__get_queens_position()
        self.attacks =self.__count_attacks()
        #self.print_board()

    def __get_queens_position(self):
        queens_position = []
        for col in range(self.n):
            for row_index in range(self.n):
                row = self.board[row_index]
                if row[col]==self.queen_charcter:
                    queens_position.append([row_index,col])
        return queens_position
                    
    def __count_attacks(self):
        attacks = 0
        for q in self.queens_positions:
            # as there is only one queen in colum we are not checking for any attacks in colum
            row,col = q 
            #checking attacks in Q to top-right corner diagonal
            while row > 0 and col < (self.n-1):
                row -= 1
                col += 1
                if self.board[row][col]==self.queen_charcter:
                      attacks += 1
            # checking attack in row after Q's position
            row,col = q
            while col < (self.n-1):
                col += 1
                if self.board[row][col]==self.queen_charcter:
                      attacks += 1 
            #checking attacks in Q to bottom-right corner diagonal
            row,col = q
            while row < (self.n-1) and col < (self.n-1):
                row += 1
                col += 1
                if self.board[row][col]==self.queen_charcter:
                      attacks += 1
        return attacks

    def get_copy_of_state(self):
        t_board = self.__get_copy_of_board()
        b = board()
        b.set_the_board(t_board)
        return b
    
    def get_all_possible_future_boards(self):
        '''
        this function will generate all 56 possible boards by moving
        one queen to all other seven remaining
        space in the colum, one space and one queen at the time.
        '''
        all_possible_board = []
        state = 0 # to just check the count of states generated
        # for each queen
        for q in self.queens_positions:
            row,col = q
            # placing queen for every row other than the current one
            for t_row in range(self.n):
                if row==t_row:
                    continue
                else:
                    t_board = self.__get_copy_of_board() # temporary board
                    # first remove the queen from original place
                    t_board[row][col] = self.alternate
                    # put the queen at new place
                    t_board[t_row][col] = self.queen_charcter
                    state+=1
                    # provide new board to the board class
                    b = board()
                    b.set_the_board(t_board)
                    all_possible_board.append(b)
        return all_possible_board
                        
                        
    def __get_copy_of_board(self):
        t_board = []
        for row in self.board:
            t_board.append(row[:])
        return t_board

    def is_same(self,other):
        if type(other)==type(self):
            # if both board's queens position is same than board is same
            for i in range(self.n): # number of queens
                if self.queens_positions[i][0] == other.queens_positions[i][0] and self.queens_positions[i][1] == other.queens_positions[i][1]:
                    # same position
                    pass
                else:
                    # if any queen's position is not same means board is different
                    return False
            # else never get called so board is same
            return True
        else:
            print("cannot compare",type(other),"and",type(self))

            
########## testing
def main():
    n = input("give n for n queens Problem=>")
    try:
        n = int(n)
    except:
        print("please provide interger")
        return
    b = board(n)
    x = b.get_all_possible_future_boards()
    b.is_same(x[0])
    b.is_same([])

if __name__=="__main__":
    main()

    
        

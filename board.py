class Board:
    def __init__(self):
        self.board = [
            ["r","n","b","q","k","b","n","r"],
            ["p","p","p","p","p","p","p","p"],
            [".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".","."],
            ["P","P","P","P","P","P","P","P"],
            ["R","N","B","Q","K","B","N","R"]
        ]
        self.turn = "white"

    def display(self):
        print(" a b c d e f g h")
        for i in range(8):
            print(8-i," ".join(self.board[i]))
        print(" a b c d e f g h")


    def parse_position(self,pos):
        col = ord(pos[0]) - ord("a")
        row = 8 - int(pos[1])
        return row,col


    def move_piece(self, start, end):
        sr,sc = self.parse_position(start)
        er,ec = self.parse_position(end)

        piece = self.board[sr][sc]

        if piece == ".":
            print("no piece at start square")
            return
        if self.turn == "white" and piece.islower():
            print("black piece,whites turn")
            return 
        if self.turn == "black" and piece.isupper():
            print("white piece,blacks turn")
            return


        self.board[sr][sc] = "."
        self.board[er][ec] = piece
        
        self.turn += "black" if self.turn == "white" else "white"



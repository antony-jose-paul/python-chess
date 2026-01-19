from board import Board
def main():
    board = Board()
    while True:
        board.display()
        print(f"{board.turn.capitalize()}'s turn")
        move = input("Enter move (e2 e4) or q:")
        if move == "q":
            break
        start,end = move.split()
        board.move_piece(start,end)

if __name__ == "__main__":
    main()
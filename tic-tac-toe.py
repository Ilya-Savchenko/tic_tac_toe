from engine import TicTacToe

start = True
player1 = input('Player1 name?: ')
player2 = input('Player2 name?: ')
game = TicTacToe(player1, player2)
while start:
	start = game.game()

class TicTacToe:
	WINNER_COMBINE = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (3, 5, 7), (1, 4, 7), (2, 5, 8), (3, 6, 9)]

	def __init__(self, player1, player2):
		self.player1 = player1
		self.player2 = player2
		self.move = self.player1
		self.closed_fields = []
		self.players_moves = {
			self.player1: [],
			self.player2: []
		}
		self.game_field = """
			1 | 2 | 3
            4 | 5 | 6
            7 | 8 | 9
		"""

	def game(self):
		self.show_field()
		player_move = (input(f'{self.move} move (enter cell number(1 to 9)): '))
		if  player_move.isdigit() and player_move not in self.closed_fields and 0 < int(player_move) < 10:
			self.closed_fields.append(player_move)
			self.players_moves[self.move].append(player_move)
			if self.move == self.player1:
				self.game_field = self.game_field.replace(player_move, 'X')
			else:
				self.game_field = self.game_field.replace(player_move, 'O')
			if self.is_win():
				self.show_field()
				print(f'{self.move} is win')
				return
			self.move = self.player1 if self.move == self.player2 else self.player2
			return True
		else:
			print('Wrong input')
			return True

	def is_win(self):
		if not len(self.players_moves[self.move]) > 2:
			return False
		number_coincidences = 0
		for combine in self.WINNER_COMBINE:
			for position in combine:
				if str(position) in self.players_moves[self.move]:
					number_coincidences += 1
				else:
					break
			if number_coincidences == 3:
				return True
			else:
				number_coincidences = 0
		return False

	def show_field(self):
		print(self.game_field)

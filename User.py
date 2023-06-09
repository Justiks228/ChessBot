from database_tools.Connection import connect
from Timer import Timer
from typing import Optional
from asyncio import get_event_loop
from chess import IllegalMoveError
from exceptions.OnSomeoneMoveError import OnSomeoneMoveError
from exceptions.IllegalMoveError import IllegalMoveError as IllegalError


class User:
	"""User class"""

	def __init__(self, user_id: int, color: bool, own_object):
		self.user_id: int = user_id
		self.color: bool = color
		self.timer: Timer = Timer(self.color)
		self.color_text = lambda x: "бел" if color else "чёрн"
		self.own_object = own_object

		# attributes from database
		self.games: Optional[int] = None
		self.points: Optional[int] = None
		self.avatar_path: Optional[str] = None
		self.nickname: Optional[str] = None
		self.username: Optional[str] = None

		task = main_loop.create_task(self.__fill_attributes())
		main_loop.run_until_complete(task)

		self.own_object.players.append(self)

	async def __fill_attributes(self):
		"""fill attributes from database"""

		info = await (await connect.request(
			"SELECT games, points, avatar_path, nickname, username FROM users WHERE user_id = ?",
			(self.user_id,)
		)).fetchone()

		self.games = info[0]
		self.points = info[1]
		self.avatar_path = info[2]
		self.nickname = info[3]
		self.username = info[4]

	def move(self, start_cell: str, end_cell: str):
		"""move in board and flip timer"""

		try:
			if self.own_object.board.turn != self.color:
				raise OnSomeoneMoveError()

			self.own_object.move("".join([start_cell, end_cell]))
			self.timer.flip_the_timer()

		except IllegalMoveError:
			raise IllegalError()

	def timer_continue(self):
		"""return timer to activity"""

		self.timer.flip_the_timer()

	def stop_timer(self):
		"""kill timer (fatal stop)"""

		self.timer.stop_the_timer()

	async def start_timer(self):
		"""timer starter"""

		await self.timer.start_timer()

	async def remove_games(self):
		"""remove games count after end game"""

		await connect.request("UPDATE users SET games = games - 1 WHERE user_id = ?", (self.user_id, ))

	async def give_points(self):
		"""add points count after end game"""

		await connect.request("UPDATE users SET points = points + 1 WHERE user_id = ?", (self.user_id, ))


main_loop = get_event_loop()

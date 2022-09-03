import time


class Chrono:
	def __init__(self, is_pause=False):
		self.seconds = 0
		self.process = None
		self.is_pause = is_pause
		self.max_time = 25 * 60

import time


class Chrono:
	def __init__(self, is_pause=False):
		self.seconds = 0
		self.process = None
		self.is_pause = is_pause




		# self.timer = time.perf_counter()
		# self.starting_time = self.timer
		# self.seconds += 1

	# def end_chrono(self):
	# 	self.timer = time.perf_counter()

	# def update_time_spent_in_second(self):
	# 	if (time.perf_counter() % self.starting_time) > 1 and not self.is_pause:
	# 		print(self.seconds)
	# 		self.starting_time = time.perf_counter()
	# 		self.seconds += 1
	# 	time.sleep(0.25)

# if __name__ == "__main__":
# 	time_duration = 20
# 	my_chrono = Chrono()
# 	while my_chrono.seconds <= time_duration:
# 		my_chrono.update_time_spent_in_second()
import time


class Chrono:
	def __init__(self):
		self.timer = time.perf_counter()

	def end_chrono(self):
		self.timer = time.perf_counter()



if __name__ == "__main__":
	my_chrono = Chrono()
	print(f"{my_chrono.timer}")
	time.sleep(3)
	my_chrono.end_chrono()
	print(f"{my_chrono.timer}")
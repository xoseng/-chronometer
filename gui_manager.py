from tkinter import Tk, Label, Button, Frame
import time
class Gui:

	def __init__(self, start_chronometer):

		self.root = Tk()
		self.root.title('Chronometer')
		self.root.resizable(0, 0)
		self.root.config(bd=30)
		self.time = Label(self.root, fg='black', width=20, font=("", "18"))
		self.time.pack()
		self.time['text'] = "00:00:00"

		def stop_chronometer(self):
			try:
				global proceso
				self.time.after_cancel(proceso)
			except:
				pass

		def resume_chronometer(self):
			try:
				global proceso
				hours = int(self.time['text'].split(':')[0])
				mins = int(self.time['text'].split(':')[1])
				secs = int(self.time['text'].split(':')[2]) + 1
				stop_chronometer()
				start_chronometer(h=hours, m=mins, s=secs)
			except:
				pass

		frame = Frame(self.root)
		btnIniciar = Button(frame, fg='green', text='Start', command=start_chronometer).grid(row=1, column=1,padx=2, pady=5)
		# btnParar = Button(frame, fg='red', text='Stop', command=stop_chronometer).grid(row=1, column=2,padx=2, pady=5)
		# btnReanudar = Button(frame, fg='blue', text='Resume', command=resume_chronometer).grid(row=1, column=3,padx=2, pady=5)
		frame.pack()

		self.root.call('wm', 'attributes', '.', '-topmost', '1')

	def main_loop(self):
		self.root.mainloop()

	def display_time_in_mm_ss(self, time_in_seconds):
		return '{:02d}:{:02d}'.format(time_in_seconds // 60, time_in_seconds % 60)




if __name__ == "__main__":

	def start_chronometer(h=0, m=0, s=0):
		global proceso

		try:
			stop_chronometer()
		except:
			pass

		if s >= 60:
			s = 0
			m = m + 1
			if m >= 60:
				m = 0
				h = h + 1
				if h >= 24:
					h = 0

		if s < 10:
			secss = '0' + str(s)
		else:
			secss = str(s)
		if m < 10:
			minss = '0' + str(m)
		else:
			minss = str(m)
		if h < 10:
			hourss = '0' + str(h)
		else:
			hourss = str(h)

		my_gui.time['text'] = hourss + ":" + minss + ":" + secss
		# self.time['text'] = str(h) + ":" + str(m) + ":" + str(s)
		proceso = my_gui.time.after(1000, start_chronometer, (h), (m), (s + 1))

	my_gui = Gui(start_chronometer=start_chronometer)

	print(my_gui.display_time_in_mm_ss(65))
	print(my_gui.display_time_in_mm_ss(111))
	print(my_gui.display_time_in_mm_ss(246))
	print(my_gui.display_time_in_mm_ss(40))

	my_gui.main_loop()

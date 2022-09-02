from tkinter import Tk, Label, Button, Frame
class Gui:

	def __init__(self):

		root = Tk()
		root.title('Chronometer')
		root.resizable(0, 0)
		root.config(bd=30)
		time = Label(root, fg='black', width=20, font=("", "18"))
		time.pack()

		time['text'] = "00:00:00"

		frame = Frame(root)
		btnIniciar = Button(frame, fg='green', text='Start', command=start_chronometer).grid(row=1, column=1,padx=2, pady=5)
		btnParar = Button(frame, fg='red', text='Stop', command=stop_chronometer).grid(row=1, column=2,padx=2, pady=5)
		btnReanudar = Button(frame, fg='blue', text='Resume', command=resume_chronometer).grid(row=1, column=3,padx=2, pady=5)
		frame.pack()

		root.call('wm', 'attributes', '.', '-topmost', '1')
		root.mainloop()



	def start_chronometer(self, h=0, m=0, s=0):
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
		secss='0'+str(s)
	    else:
		secss = str(s)
	    if m < 10:
		minss='0'+str(m)
	    else:
		minss =str(m)
	    if h < 10:
		hourss='0'+str(h)
	    else:
		hourss = str(h)
		
	    time['text'] = hourss + ":" + minss + ":" + secss
	    #time['text'] = str(h) + ":" + str(m) + ":" + str(s)
	    proceso = time.after(1000, start_chronometer, (h), (m), (s + 1))

	def stop_chronometer(self):
	    try:
		global proceso
		time.after_cancel(proceso)
	    except:
		pass

	def resume_chronometer(self):
	    try:
		global proceso
		hours=int(time['text'].split(':')[0])
		mins=int(time['text'].split(':')[1])
		secs=int(time['text'].split(':')[2])+1
		stop_chronometer()
		start_chronometer(h=hours, m=mins, s=secs)
	    except:
		pass

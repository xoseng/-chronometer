from tkinter import Tk, Label, Button, Frame
from time_manager import Chrono


class Gui:

    def __init__(self, start_chronometer, stop_chronometer):

        self.root = Tk()
        self.root.title('Chronometer')
        self.root.resizable(0, 0)
        self.root.config(bd=30)
        self.time = Label(self.root, fg='black', width=20, font=("", "18"))
        self.time.pack()
        self.time['text'] = "00:00:00"

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
        btnIniciar = Button(frame, fg='green', text='Start', command=start_chronometer).grid(row=1, column=1, padx=2,
                                                                                             pady=5)
        btnParar = Button(frame, fg='red', text='Stop', command=stop_chronometer).grid(row=1, column=2, padx=2, pady=5)
        # btnReanudar = Button(frame, fg='blue', text='Resume', command=resume_chronometer).grid(row=1, column=3,padx=2, pady=5)
        frame.pack()

        self.root.call('wm', 'attributes', '.', '-topmost', '1')

    def main_loop(self):
        self.root.mainloop()

    def display_time_in_mm_ss(self, time_in_seconds):
        return '{:02d}:{:02d}'.format(time_in_seconds // 60, time_in_seconds % 60)


def start_chronometer(h=0, m=0, s=0):
    try:
        stop_chronometer()
    except:
        pass
    my_chrono.process = my_gui.time.after(1000, start_chronometer)
    my_chrono.seconds = int(my_chrono.process.split("#")[-1])
    my_gui.time['text'] = str(h) + ":" + my_gui.display_time_in_mm_ss(my_chrono.seconds)


def stop_chronometer():
    try:
        my_gui.time.after_cancel(my_chrono.process)
    except:
        pass


if __name__ == "__main__":
    my_gui = Gui(start_chronometer=start_chronometer,
                 stop_chronometer=stop_chronometer)
    my_chrono = Chrono()

    my_gui.main_loop()

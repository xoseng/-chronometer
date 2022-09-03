import tkinter
from tkinter import Tk, Label, Button, Frame, Misc
from time_manager import Chrono


class Gui:

    def __init__(self):

        self.root = Tk()
        self.root.title('Chronometer')
        self.root.resizable(0, 0)
        self.root.config(bd=30)
        self.time = Label(self.root, fg='black', width=20, font=("", "18"))
        self.time.pack()
        self.time['text'] = "00:00"
        self.max_time = 25 * 60
        self.end_timer = False

        frame = Frame(self.root)
        self.btnIniciar = Button(frame, fg='green', text='Start', command=start_chronometer).grid(row=1,
                                                                                                  column=1,
                                                                                                  padx=2,
                                                                                                  pady=5)
        btnParar = Button(frame, fg='red', text='Stop', command=stop_chronometer).grid(row=1,
                                                                                       column=2,
                                                                                       padx=2,
                                                                                       pady=5)
        btnReanudar = Button(frame, fg='blue', text='Resume', command=resume_chronometer).grid(row=1,
                                                                                               column=3,
                                                                                               padx=2,
                                                                                               pady=5)
        btnInput = Button(frame, fg='blue', text='Changing time', command=create_time_settings_window).grid(row=2,
                                                                                                            column=2,
                                                                                                            padx=2,
                                                                                                            pady=5)
        frame.pack()

        # Windows should stay in forebground
        self.root.call('wm', 'attributes', '.', '-topmost', '1')

    def main_loop(self):
        self.root.mainloop()

    def display_time_in_mm_ss(self, time_in_seconds):
        time_to_display = self.max_time - time_in_seconds
        if time_to_display >= 0:
            return '{:02d}:{:02d}'.format(time_to_display // 60, time_to_display % 60)
        else:
            self.end_timer = True



def start_chronometer():
    try:
        stop_chronometer()
    except:
        pass
    my_chrono.process = my_gui.time.after(1000, start_chronometer)
    print(my_chrono.process)
    # my_chrono.seconds = int(my_chrono.process.split("#")[-1])
    my_chrono.seconds += 1
    my_gui.time['text'] = my_gui.display_time_in_mm_ss(my_chrono.seconds)


def stop_chronometer():
    try:
        my_gui.time.after_cancel(my_chrono.process)
    except:
        pass

def resume_chronometer():
    global my_gui
    stop_chronometer()
    my_chrono.seconds = 0
    my_gui.time['text'] = my_gui.display_time_in_mm_ss(my_chrono.seconds)


def create_time_settings_window():
    time_settings_window = Tk()
    time_settings_window.title('time setting')
    time_settings_window.resizable(0, 0)
    time_settings_window.config(bd=30)
    time = Label(time_settings_window, fg='black', width=20, font=("", "18"))
    time.pack()
    time['text'] = "00:00"

    frame = Frame(time_settings_window)

    # Windows should stay in foreground
    time_settings_window.call('wm', 'attributes', '.', '-topmost', '1')

if __name__ == "__main__":
    my_gui = Gui()
    my_chrono = Chrono()
    my_gui.main_loop()

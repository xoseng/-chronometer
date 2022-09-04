import tkinter
from tkinter import Tk, Label, Button, Frame, Misc, Text, messagebox


class Chrono:

    def __init__(self, is_pause=False):
        self.seconds = 0
        self.process = None
        self.is_pause = is_pause
        self.max_time = 25 * 60

class Gui:

    def __init__(self, title):

        self.root = Tk()
        self.root.title(title)
        self.root.resizable(0, 0)
        self.root.config(bd=30)
        self.time = Label(self.root, fg='black', width=20, font=("", "18"))
        self.time.pack()

        # Windows should stay in forebground
        self.root.call('wm', 'attributes', '.', '-topmost', '1')

    def create_main_window(self):
        self.time['text'] = "00:00"
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
        btnInput = Button(frame, fg='blue', text='Changing time', command=click_time_settings_window).grid(row=2,
                                                                                                           column=2,
                                                                                                           padx=2,
                                                                                                           pady=5)
        frame.pack()

    def create_time_settings_window(self):
        frame = Frame(self.root)
        self.inputtxt = Text(self.root,
                             height=1,
                             width=5)
        self.btnValidate = Button(frame, fg='green', text='Go', command=get_value).grid(row=1,
                                                                                        column=2,
                                                                                        padx=2,
                                                                                        pady=5)
        self.inputtxt.pack()
        frame.pack()

        frame = Frame(self.root)

    def main_loop(self):
        self.root.mainloop()

    def display_time_in_mm_ss(self, time_in_seconds, max_time):
        time_to_display = max_time - time_in_seconds
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
    my_chrono.seconds += 1
    my_gui.time['text'] = my_gui.display_time_in_mm_ss(my_chrono.seconds, my_chrono.max_time)


def stop_chronometer():
    try:
        my_gui.time.after_cancel(my_chrono.process)
    except:
        pass

def resume_chronometer():
    global my_gui
    stop_chronometer()
    my_chrono.seconds = 0
    my_gui.time['text'] = my_gui.display_time_in_mm_ss(my_chrono.seconds, my_chrono.max_time)

def get_value():
    global time_settings_window
    try:
        inp = time_settings_window.inputtxt.get(1.0, "end-1c")
        time = inp.split(":")
        max_time = int(time[0]) * 60 + int(time[1])
    except:
        print("no Empty string please")
        print("set default time 25 minutes")
        messagebox.showinfo('Error', 'format not correct\nCorrect format: xx:xx\nSet default time to 25 minutes')
        max_time = 25 * 60
        my_chrono.max_time = max_time
        return
    my_chrono.max_time = max_time
    time_settings_window.root.destroy()

def click_time_settings_window():
    global time_settings_window
    time_settings_window = Gui(title='time setting')
    time_settings_window.create_time_settings_window()


if __name__ == "__main__":
    my_chrono = Chrono()
    time_settings_window = None
    my_gui = Gui(title='chronometer')
    my_gui.create_main_window()
    my_gui.main_loop()

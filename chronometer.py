# coding=utf8
from gui_manager import Gui, start_chronometer, stop_chronometer
from time_manager import Chrono

proceso = 0

my_gui = Gui(start_chronometer=start_chronometer, stop_chronometer=stop_chronometer)

print(my_gui.display_time_in_mm_ss(65))
print(my_gui.display_time_in_mm_ss(111))
print(my_gui.display_time_in_mm_ss(246))
print(my_gui.display_time_in_mm_ss(40))

my_gui.main_loop()

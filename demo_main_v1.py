import curses
import cmd
import os

class Display:
	default_lines_when_scroll = 5
	view = None

	def __init__(self):
		self.view = curses.initscr()
		curses.start_color()
		curses.use_default_colors()
		curses.init_pair(1, curses.COLOR_RED, -1)

	def show(self, data):
		# clear
		self.view.erase()

		# show data
		self.view.move(0, 0)
		self.view.addstr(data, curses.color_pair(0))

		return self.wait_for_act()

	def wait_for_act(self):
		self.view.move(curses.LINES - 1, 0)
		self.view.addstr(" > ", curses.color_pair(1))
		_input = self.view.getstr()
		return _input

	def scroll_up(self, lines):
		if lines is None or lines < 0:
			lines = default_lines_when_scroll
		self.view.scroll(lines)

	def scroll_down(self, lines):
		if lines is None or lines < 0:
			lines = default_lines_when_scroll
		self.view.scroll(1)

if __name__ == '__main__':
	display = Display()
	cmd = display.show("ssdqw\nsdqwe\nahed\nsasda\nsasda\nsasda\nsasda\nsasda\nsasda\nsasda\nsasda\nsasda\nsasda\nsasda\nsasda\nsasda\nsasda\nsasda\nsasda\nsasda\nsasda\nsasda\nsasda\nsasda")
	display.scroll_down(2)
	display.show(cmd)

''' 
1. show data 
2. bind cmd
3. do control
4. jump show
'''

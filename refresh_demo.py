import curses

stdscr = curses.initscr()

curses.start_color()
curses.use_default_colors()
curses.init_pair(1, curses.COLOR_RED, -1)


# 关闭命令行回显
# curses.noecho()

def move_bottom(stdscr):
    # 将光标移动到屏幕底部
    stdscr.move(curses.LINES - 1, 0)

    # 在光标位置打印文本
    stdscr.addstr(" > ", curses.color_pair(1))

    stdscr.refresh()

while True:

    # 打印文本
    stdscr.addstr("Hello, World!")
    # 刷新屏幕显示
    # stdscr.refresh()

    stdscr.addstr("help")

    # 暂停，等待用户输入
    key = stdscr.getch()

    stdscr.erase()

    stdscr.addstr("key: %d" % key)

    move_bottom(stdscr)

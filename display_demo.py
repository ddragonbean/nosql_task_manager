import curses

def main(stdscr):
    # 初始化curses
    curses.curs_set(0)
    stdscr = curses.initscr()
    stdscr.keypad(True)

    # 创建文本框窗口
    height, width = stdscr.getmaxyx()
    textbox = curses.newwin(height-1, width-1, 1, 1)
    textbox.scrollok(True)

    # 添加文本
    text = "This is a long text that needs to be scrolled."
    for i in range(40):
        textbox.addstr(text + str(i) + "\n")

    # 刷新窗口
    stdscr.refresh()
    textbox.refresh()

    # 滚动文本框
    textbox.scroll(40)

    # 等待用户输入
    stdscr.getch()

# 运行主函数
curses.wrapper(main)
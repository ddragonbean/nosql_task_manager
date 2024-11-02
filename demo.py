import cmd
import os

class Display:

	def __init__(self):
		pass

	def display_menu(self):
		os.system('clear' if os.name == 'posix' else 'cls')
		print("Menu\n")
		print("1.say Hello")
		print("2.help")

	def display_help(self):
		os.system('clear' if os.name == 'posix' else 'cls')
		print("help info")
		print()
		print("Menu\n")
		print("1.say Hello")
		print("2.help")

class MyCmd(cmd.Cmd):
    prompt = '(mycmd) '
    display = Display()

    def do_hello(self, arg):
        """Say hello to arg"""
        print(f'Hello, {arg}!')
        self.display.display_menu()

    def do_EOF(self, arg):
        """Exit on Ctrl-D"""
        print("Goodbye!")
        return True  # Return True to exit the cmd loop

    def do_1(self, arg):
    	self.display.display_menu()

    def do_2(self, arg):
    	self.display.display_help()

if __name__ == '__main__':
    MyCmd().cmdloop()
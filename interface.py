#!/usr/bin/env python3
'''
----------------------------------------------------------------
Author : Alexis Rodriguez
Start date : 2020-02-26
End date : 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Description : 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
----------------------------------------------------------------
'''
try:
	# > import colored for colored text
	from colored import fg, attr
	# > import figlet for banner
	from pyfiglet import Figlet
	# > import random for creating random colors
	from random import randrange
	# > import tqdm for creating progress bars
	from tqdm import tqdm
	# >	 import time for sleep function
	from time import sleep
	# import threading for repeated functions calls
	from threading import Timer
# > handling import error
except ImportError:
	print('%s [-] Error importing a module %s' % (fg(196), attr(0)))
	# > exit program
	os.system('exit')




# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# 		Con3ni3nt Interface
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

class Interface:

	def __init__(self):
		'''
		initialize all necessary variables for the interface
		'''

		# > name of program
		self.title='Conv3ni3nt'
		# > figlet font used for title
		self.font='future'
		# text colors
		self.red=196
		self.purple=129
		self.lightyellow=228
		self.orange=208
		self.lightgreen=111
		# get random number for random colors
		self.rancolor=randrange(256)
		# > change color every 
		change_color=Timer(1, self.generate_random_color)
		# start timer
		change_color.start()
		

	def generate_random_color(self):
		'''
		set the random color variable to a random number 
		between 1-255 which will determine the color
		'''

		self.rancolor = randrange(256)






	def signature(self):
		'''
		print out title and authors
		'''

		# > declaring Figlet object
		sig = Figlet(font=self.font)

		print('|%%%%%%%%%%%%%%%%%%%%%%%%%%|')
		# > print title
		print(sig.renderText(self.title))
		''' (-------) print authors and contributors (-------) '''
		print(' by: "%sBinexisHATT%s"' % (fg(self.purple), attr(0)))

		print(' contributor: "%sJedi9986%s"' % (fg(self.purple), attr(0)))

		print('|%%%%%%%%%%%%%%%%%%%%%%%%%%|\n')







	def tools_prompt(self):
		'''
		the prompt that is displayed for user to enter tool options
		'''

		# > prompt for the tools the user would like to use
		print('%sEnter the tools you use: %s' % (fg(self.red), attr(0)))
		# > show usage like string
		print('%sE.g. nmap dirb nikto ...%s' % (fg(self.lightyellow), attr(0)))

		print('%sType "menu" for menu%s' % (fg(self.lightgreen), attr(0)))







	def scan_info(self, tools, options_for_tools):
		'''
		print out info regarding all scans that are running in the
		background

		params : list of tools used, list of options used for each tool
		'''
		
		print('[+] %sInitiating scans...%s' % (fg(self.rancolor), attr(0)))

		for tool, option in zip(tools, options_for_tools):
			# > stop for 1 second before continuing loop
			sleep(0.5)
			# > print info concerning the scans that are running
			print('[+] %sRunning scan -- >%s' % (fg(self.rancolor), attr(0)), tool, option)





	def present_completion_bar(self):
		'''
		displays completion bar
		'''

		for _ in tqdm(range(1000000), desc='%sAll scans completed!%s' % (fg(self.purple), attr(0))):
			pass





	def display_menu(self):
		'''
		displays menu from tool prompt
		'''

		print('%s+-----------------------------------------------+%s' % (fg(self.rancolor), attr(0)))
		print(' | Options :\t\t\t\t       |')
		print(' | 1. "tools" to show available tools          |')
		print(' | 2. "shell" followed by shell command        |\n |    to execute shell commands within program |')
		print(' | 3. "exit" to exit program\t               |')
		print('%s+-----------------------------------------------+%s' % (fg(self.rancolor), attr(0)))
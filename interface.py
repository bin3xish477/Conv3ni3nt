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
	# >	 imprt time for sleep function
	from time import sleep
# > handling import error
except ImportError:
	print('%s [-] Error importing a module %s' % (fg(196), attr(0)))
	os.system('exit')

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# 		Con3ni3nt Interface
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

class Interface:
	def __init__(self):
		'''
		'''
		# > name of program
		self.title='Conv3ni3nt'
		# > figlet font used for title
		self.font='future'
		# text colors
		self.red=196
		self.purple=129
		self.lightyellow=228
		self.gray=250
		# get random number for random color
		self.rancolor=randrange(256)


	def signature(self):
		'''
		'''

		sig = Figlet(font=self.font)

		print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%')

		print(sig.renderText(self.title))

		print('By : ' + '%sAlexis Rodriguez%s' % (fg(self.purple), attr(0)))

		print('%s\t    aka BinexisHATT%s' % (fg(self.purple), attr(0)))

		print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n')


	def tools_prompt(self):
		'''
		'''

		print('%sEnter the tools you use: %s' % (fg(self.red), attr(0)))

		print('%sE.g. nmap dirb nikto ...%s' % (fg(self.lightyellow), attr(0)))


	def progress_bar(self, tool_list):
		'''
		Generate progress bar with name of tools used
		params : list of the tools that were used
		'''

		# > for every tool in our tool list
		for tool in tool_list:
			# > this addition is just formating for the colored module
			tool = '%s' + tool + '%s'
			# > using tqdm to generate progress bar
			for p in tqdm(range(100),desc=tool % (fg(self.rancolor), attr(0))+' scan'):
				# > sleep for 0.2 seconds before next iterations
				sleep(0.2)
				# > continue to next iteration
				continue

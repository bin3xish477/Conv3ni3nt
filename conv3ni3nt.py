#!/usr/bin/env python3

'''
----------------------------------------------------------------
Author : Alexis Rodriguez
Start date : 2020-02-26
End date : 2020-

****************************************************************
Description : This tool will provide its user's with an easier 
way to gather information during the information gathering 
phase of a penetration test. The user has access to the most
common scanning tools installed on there machine must only worry 
about passing invalid arguments. The purpose of this tool is 
to use it for performing the longer scans while analyzing the 
results of any scanning tools that finish faster and then going
back to inspect the results from you longer scans.
****************************************************************
----------------------------------------------------------------
'''


try:
	# > import all objects from interface module
	from interface import *
	# > import sys for 
	import sys
	# > import os for performing terminal commands
	import os
	# > import concurrent.futures for threading
	import concurrent.futures
	# > import subprocess for executing bash commands
	import subprocess as subp
	# > import readline to add arrow key functionality
	import readline
	# > import time for sleeping function
	from time import sleep
	
# > check for importing error
except ImportError:
	print('%s [-] Error importing a module %s' % (fg(196), attr(0)))
	# > exit program
	os.system('exit')
	
	
	
# > append your tool HERE to be able to use it!	
VALID_TOOLS = [
'nmap', 'dirb', 'nikto',
'gobuster','enum4linux',
'smbmap', 'onesixtyone','fierce',
'snmpwalk', 'nmblookup','snmp-check',
'wpscan','masscan', 'sslscan',
'nbtscan', 'arp-scan', 'dnsenum',
'sslyze', 'TheHarvester' 
# if installed uncomment these:
#'sublist3r', 'dnswalk'
]
		
	

	
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# 	Conv3ni3nt Class
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class Conv3ni3nt:
	def __init__(self, interface_obj):
		'''
		Initializing all necessary variables for this class

		params : the interface object that was instantiated in main
		'''
		
		# > create object to interact with interface
		self.interface = interface_obj

		# > print out signature screen
		self.interface.signature()

		# > list of tools that were entered
		self.tool_list = []

		# > list of comands to execute
		self.to_execute = []

		# > list of generated file names
		self.generated_file_list = []

		# > our list containing the options for each tool
		self.options_list = []

		




	def get_tools(self):
		'''
		displays the tools prompt and stores the tools in a list
		and returns the tool list
		'''

		# > display select tools prompt
		self.interface.tools_prompt()

		# > the tools that are specified
		inputed = input('%s(Conv3)%s> ' % (fg(self.interface.orange), attr(0))).split()

		# > if the user types in exit
		if 'exit' in inputed:
			print('[+] %sQuiting program ...%s' % (fg(45), attr(0)))

			# > exit program
			sys.exit(0)

		# > if user types in tools
		elif 'tools' in inputed:
			# > if user input is keyword "tools" print available tools
			self.display_available_tools()

			# > sleep for 0.2 seconds
			sleep(0.2)

			# > a recursive call to this function
			self.get_tools()

		
		# > if user types in shell followed by a command
		elif inputed[0] == 'shell' and inputed[1:]:
			# > get command to execute from list
			cmd = inputed[1:]

			# > invoke function to execute shell commands
			self.shell_exec(cmd)

			# > a recursive call to this function
			self.get_tools()

		# > if user types in shell without a command
		elif inputed[0] == 'shell' and not inputed[1:]:
			# > print notification of missing command
			print('Error: no command was passed after "shell"')
			print('Please try again...')

			# > a recursive call to this function
			self.get_tools()

		# > if user types in menu
		elif 'menu' in inputed:
			# > display program command options
			self.interface.display_menu()

			# > sleep for 0.2 seconds
			sleep(0.2)

			# > recursive call to this function
			self.get_tools()

		# > if user types in clear
		elif 'clear' in inputed:
			# > clear screen
			os.system('clear')

			# > recursive call to this function
			self.get_tools()

		else:
			# > clear list of inputed tools
			self.tool_list.clear()
			# split the tools specified into a list
			self.tool_list = inputed

			# > loop through the list of tools that were given
			for tool in self.tool_list:
				# > if tool is not a valid tool
				if tool not in VALID_TOOLS:

					print('\n[-] %sInvalid tool! Try again.%s\n' % (fg(10), attr(0)))
					# > clear list of inputed tools
					self.tool_list.clear()

					# > sleep for 0.2 seconds
					sleep(0.2)

					# > a recursive call to this function
					self.get_tools()

		# > return tool list
		return self.tool_list






	def get_tool_options(self):
		'''
		will display the tool options prompt and record the options that were passed
		'''

		# > clear the terminal screen
		os.system('clear')

		# > print out my signature
		self.interface.signature()

		# > prompt user for help menu
		print('%sType "help" for menu or "exit" for quiting%s' % (fg(self.interface.rancolor), attr(0)))
		print('+----------------------------------------+')

		# > inform user about the automatic creation of files
		print('|%s[Note]%s: do not provide output file      |\n|options because files are automatically |\n|created in a \'convenient\' way.          |'
				% (fg(9), attr(0)))
		print('+----------------------------------------+')

		print('%sE.g. "-sC 192.168.0.1"%s' % (fg(self.interface.rancolor), attr(0)))
		# > iterate over every tool and prompt user for the desired options
		for tool in self.tool_list:
			# > this addition is simply formating for our colored module
			tool = '%s' + tool + '%s'
			# > store user input in variable
			tool_option = input('Enter ' + tool % (fg(self.interface.rancolor), attr(0)) + ' options: ')

			# > if exit is the inputed option, exit the program
			if 'exit' in tool_option:
				print('[+] %sQuiting program ...%s' % (fg(45), attr(0)))
				# > exit program
				sys.exit(0)

			else:
				# > append options to our list containing all tool options
				self.options_list.append(tool_option)

		# > return list of options
		return self.options_list






	def generate_file_name(self, tool_name, tool_options):
		'''
		this is another auxiliary function for generating convient file names

		Params : tool that is being used, the tools options
		'''

		# > if the option contains the following string
		# > cut the string out of the option
		if 'http://' in tool_options:
			# > getting appropiate substring
			tool_options = tool_options[7:]

		# > return the file name
		return tool_name + ' ' + tool_options






	def set_file_command_lists(self, tool, tool_options):
		'''
		start the tool with the options that were specified
		
		Params : the name of the tool, the options for the tool
		'''

		# > get generated command from function that'll create specific 
		# > commands according to the tool
		command = self.generate_command(tool, tool_options)

		# > if user types in help, display the tools menu
		if tool_options == 'help':
			# > call the tool without any arguments
			# > which will display menu for most tools
			subp.run(tool, shell=True)

			# > erase all options from option list
			self.options_list.clear()

			# > prompt user to verify if they would like to go back to the tool options screen 
			go_back = input('%sType "back" to go back to tool prompt: %s' % (fg(self.interface.red), attr(0)))
			# > if input is back then display options screen
			if go_back.strip() == 'back':
				# > return to previous display
				self.return_to_options_prompt(tool)

		# > if the use does not type in help, do the following
		else:
			# > try opening file
			try:
				# > get file name to create
				file_name = self.generate_file_name(tool, tool_options)
			# throw exception
			except:
				print('%SError creating a file%s' % (fg(self.interface.lightyellow), attr(0)))
				# > exit program
				sys.exit(0)

		# > append file created to class file list
		self.generated_file_list.append(file_name)

		# > append command to be executed to class list containing commands
		self.to_execute.append(command)





				      
	def return_to_options_prompt(self, tool):
		'''
		this is an auxiliary function for returning to the tool prompt display

		params : tool that is currently being used
		'''

		# > display tool options prompt
		tool_options = self.get_tool_options()

		# > a little recursion going on here
		self.set_file_command_lists(tool, tool_options)






	def execute_all(self, file_arg, command):
		'''
		start each tool on a different thread

		params : the name of thee file, the command to execute
		'''

		# > open file created for writing
		with open(file_arg, 'w') as tool_file:
		# > use the tool with its options and direct output to file
			subp.run(command,
				# > redirecting stdout to file
				stdout=tool_file, 
				# > redirecting std err to stdout
				stderr=subp.STDOUT,
				# > save data as normal text
				text=True)






	def generate_command(self, tool, tool_options):
		'''
		returns command that will be executed

		params : 
		'''
		# > command to return and executed
		command = ''
		# > handling special case for dirb because dirb
		# > sometimes prompts user for input which will halt 
		# > out programs execution
		if tool == 'dirb':
			# > appending -w option to award input prompts
			# > creating dirb command
			command = (tool + ' ' + tool_options + ' -w').split()

		# > tell nikto not to ask about submitting updates
		# > without this argument the program will freeze 
		# > indefinitely
		elif tool == 'nikto':
			# > append "-ask no" to evade the the prompt
			command = (tool + ' ' + tool_options + ' -ask no').split()

		else:
			# > creating non-dirb command 
			command = (tool + ' ' + tool_options).split()

		# > return the command created
		return command

	
	
	


	def display_available_tools(self):
		'''
		displays all available tools that can be used
		'''
		
		print('+-----------------------------------------------+')
		
		i = 0
		# > loop through valid tools list
		for tool in VALID_TOOLS:
			# > for appearance and organization
			if i % 4 == 0:

				if i == 0:
					print('(' + tool + ') ', end=' ')

				else:
					print('\n' + '(' + tool + ') ', end=' ')
				i += 1

			else:
				print('(' + tool + ') ', end=' ')
				i += 1

		print('\n+-----------------------------------------------+')


		
		

	'''(----) GETTERS (---)'''
	def get_to_execute(self):
		'''
		returns list containing commands to execute
		'''

		return self.to_execute 


	def get_file_list(self):
		'''
		returns list contaninig files to create
		'''
		
		return self.generated_file_list






	def shell_exec(self, cmd):
		'''
		executes and displays shell commands from within program
		'''
		try:
			print('\n')
			# > execute shell command
			subp.run(cmd ,stderr=subp.DEVNULL)
			print('\n')
		# > handling invalids commands
		except:
			print('[-] Invalid command!')
			sleep(0.2)
			# > return to tools prompt
			self.get_tools()





# %%%%%%%%%%%%%%%%
# 	MAIN      
# %%%%%%%%%%%%%%%%

def initiate():
	# > clear screan
	os.system('clear')

	# > instantiate Interface object
	display = Interface()

	# > instantiate Conv3i3nt object
	conv3_obj = Conv3ni3nt(display)

	# > returns list of inputed tools
	tools_lst = conv3_obj.get_tools()

	# > returns a list of options specified for each tool
	tool_options = conv3_obj.get_tool_options()

	# > zip up both the tool and tool options
	# > and send the variable to the function that'll start the tool
	for tool, options in zip(tools_lst, tool_options):
		# > creating file and command lists
		conv3_obj.set_file_command_lists(tool, options)

	# > retrieve list of generated files names to create
	files_to_create = conv3_obj.get_file_list()

	# > retrieve commands to exectue
	commands = conv3_obj.get_to_execute()

	# > use threads to execute our scans
	with concurrent.futures.ThreadPoolExecutor() as executor:
		print('[+] %sCreating threads for scan/s%s' % (fg(display.rancolor), attr(0)))
		try:
			# > invoke the execute all funcion with list of files
			# > and list of commands as argumens and will perform
			# > these operations asynchronously
			executor.map(conv3_obj.execute_all, files_to_create, commands)

			# > display a random success bar
			display.scan_info(tools_lst, tool_options)

		except:
			# > print error message concerned with threading
			print('%s[-] error creating thread for scans\n%s' %  (fg(display.red), attr(0)))

	# > print out closing statement and bar
	display.present_completion_bar()

	
	
	
	
# > if current module is 'main' start program
if __name__ == '__main__':
	try: # > begin program
		initiate()
	# > handling control + c interupts
	except KeyboardInterrupt:
		print('\n[-] %sProgram Interrupted!%s' % (fg(9), attr(0)))
		try:
			# > exit program 
			sys.exit(0)
		# > handling error exiting program with sys
		except SystemExit:
			# > exit if error
			os._exit(0)

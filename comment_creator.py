#     __                                          
#    /   _ __ __  _ __ _|_    _ __ _  _ _|_ _  __
#    \__(_)||||||(/_| | |_   (_ | (/_(_| |_(_) | 

# Copyright 2026 Ant-wq
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the “Software”), to 
# deal in the Software without restriction, including without limitation the 
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or 
# sell copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in 
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS 
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN 
# THE SOFTWARE.


#====================================
#	 --GLOBAL VARIABLES--		
#====================================

banner = [
	" __                                         ",
	"/   _ __ __  _ __ _|_    _ __ _  _ _|_ _  __",
	"\\__(_)||||||(/_| | |_   (_ | (/_(_| |_(_) |  (C edition)",
	]

GNU_GPL_V3 = [
	'Copyright (C) <year>  <name of author>                                ',
	'                                                                      ',
	'This program is free software: you can redistribute it and/or modify  ',
	'it under the terms of the GNU General Public License as published by  ',
	'the Free Software Foundation, either version 3 of the License, or     ',
	'(at your option) any later version.                                   ',
	'                                                                      ',
	'This program is distributed in the hope that it will be useful,       ',
	'but WITHOUT ANY WARRANTY; without even the implied warranty of        ',
	'MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         ',
	'GNU General Public License for more details.                          ',
	'                                                                      ',
	'You should have received a copy of the GNU General Public License     ',
	'along with this program.  If not, see <https://www.gnu.org/licenses/>.',
	]

MIT = [
	'Copyright <YEAR> <COPYRIGHT HOLDER>                                   ',
	'                                                                      ',
	'Permission is hereby granted, free of charge, to any person obtaining ',
	'a copy of this software and associated documentation files            ',
	'(the “Software”), to deal in the Software without restriction,        ',
	'including without limitation the rights to use, copy, modify, merge,  ',
	'publish, distribute, sublicense, and/or sell copies of the Software,  ',
	'and to permit persons to whom the Software is furnished to do so,     ',
	'subject to the following conditions:                                  ',
	'                                                                      ',
	'The above copyright notice and this permission notice shall be        ',
	'included in all copies or substantial portions of the Software.       ',
	'                                                                      ',
	'THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND,       ',
	'EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF    ',
	'MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.',
	'IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY  ',
	'CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,  ',
	'TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE     ',
	'SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.                ',
	]

APACHE_V2 = [
	'Copyright [yyyy] [name of copyright owner]                            ',
	'                                                                      ',
	'Licensed under the Apache License, Version 2.0 (the "License");       ',
	'you may not use this file except in compliance with the License.      ',
	'You may obtain a copy of the License at                               ',
	'                                                                      ',
	'    http://www.apache.org/licenses/LICENSE-2.0                        ',
	'                                                                      ',
	'Unless required by applicable law or agreed to in writing, software   ',
	'distributed under the License is distributed on an "AS IS" BASIS,     ',
	'WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,                         ',
	'either express or implied.                                            ',
	'See the License for the specific language governing permissions and   ',
	'limitations under the License.                                        ',
	]

licensesDict = {
		'GNU General public license V3.0':GNU_GPL_V3,
		'MIT License':MIT,
		'APACHE V2.0':APACHE_V2,
		}

chapters = []
isLicense = False


#=============================
#        --Functions--
#=============================

def printBanner():
	
	for i in banner:
		print(i)
	print(" By: Ant-wq\n")

def needLicense():
	
	user_input = str()
	exitStatus = False

	print("Do you need license?(y/n)")
	
	while exitStatus == False: 
		
		user_input = input("> ")
		if (user_input == "y") or (user_input == "Y"):
			exitStatus = True
			return True
		elif (user_input == "n") or (user_input == "N"):
			exitStatus = True
			return False
		else:
			print("\nUnknown input!\n")



def selectLicense():
	
	exitStatus = False

	print("\nLicenses:")
	while exitStatus == False:
		
		index = 1
		licenses_names = list(licensesDict.keys())
		print(licenses_names)
		for i in licenses_names:
			print(str(index)+") "+i)
			index+=1
		
		try:
			user_input = int(input("> "))
		except:
			print("\nUnknown input!\n")
			continue

		if user_input not in range(0,index):
			print("\nWrong number!\n")
		else:
			exitStatus = True
			break;

	return str(licenses_names[user_input-1]);

def getAuthorAndYear():

	got_name = False
	got_year = False

	exitStatus = False
	author = str()
	year = str()

	while exitStatus == False:
		if got_name == False:
			print("Author's name:")
			author = input("> ")
	
			if(len(author)>64):
				print("\nToo long name!\n")
				continue
			got_name = True

		if got_year == False:
			print("Enter Year:")
			try:
				year_tmp = int(input("> "))
			except:
				print("\nYear must be a number in YYYY format\n")
				continue

			year = str(year_tmp)

			if len(year)!=4:
				print("year should be in YYYY")
				continue
			got_year = True

		exitStatus = True
	
	return author, year

def setStructure():
	
	exitStatus = False

	print("Enter chapters of code(return empty string to exit):")
	while exitStatus == False:
		user_input = input("> ")
		if len(user_input) == 0:
			exitStatus = True
		else:
			chapters.append(user_input)

def printCommentsWithLicense(license_to_print):
	print("Comments:\n")
	print("/"+"*"*78)
	for i in license_to_print:
		print(" *   "+i+"   *")	
	print(" "+"*"*78+"/")
	print("\n\n\n")

	for j in chapters:
		print("/"+"*"*78)
		print(" *  "+j+" "*(74-len(j))+"*")	
		print(" "+"*"*78+"/")
		print("\n\n\n")

def printCommentsWithoutLicense(author, date):
	print("Comments:\n")
	print("/"+"*"*78)
	print(" *  Author: "+author+" "*(66-len(author))+"*")
	print(" *"+" "*76+"*")
	print(" *  Year: "+date+" "*64+"*")
	print(" "+"*"*78+"/")
	print("\n\n\n")
	
	for j in chapters:
		print("/"+"*"*78)
		print(" *  "+j+" "*(74-len(j))+"*")	
		print(" "+"*"*78+"/")
		print("\n\n\n")

	
def main():

	author = str()
	year = str()

	printBanner()
	
	if(needLicense() == True):
		selected_license = selectLicense()
		setStructure()
		printCommentsWithLicense(licensesDict[selected_license])
	else:
		author, year = getAuthorAndYear()
		setStructure()
		printCommentsWithoutLicense(author, year)
	
	return 0

if __name__ == "__main__":
	main()

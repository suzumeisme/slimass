from src.SlimService import slims
import sys,os

def param_check():
	try:
		a = sys.argv[1]
	except IndexError:
		print("Usage python2 wms.py file.txt")
		os.sys.exit()

def file_check():
	try:
		open(sys.argv[1])
	except IOError:
		print("Pastikan file yang mau di upload benar")
		os.sys.exit()

def about():
	os.system("clear")
	print('  \033[1;31m __     __     __    __     ______     __         __     __    __     ______     ______     ______    ')
	print('  /\ \  _ \ \   /\ "-./  \   /\  ___\   /\ \       /\ \   /\ "-./  \   /\  __ \   /\  ___\   /\  ___\   ')
	print('  \ \ \/ ".\ \  \ \ \-./\ \  \ \___  \  \ \ \____  \ \ \  \ \ \-./\ \  \ \  __ \  \ \___  \  \ \___  \  ')
	print('   \ \__/".~\_\  \ \_\ \ \_\  \/\_____\  \ \_____\  \ \_\  \ \_\ \ \_\  \ \_\ \_\  \/\_____\  \/\_____\ ')
	print('    \/_/   \/_/   \/_/  \/_/   \/_____/   \/_____/   \/_/   \/_/  \/_/   \/_/\/_/   \/_____/   \/_____/ ')
	print('\033[1;37mSLIMASS WAS CREATED BY WARMACHINE HACKER TEAM\n')

if __name__ == "__main__":
	try:
		about()
		param_check()
		file_check()
		while True:
			target = raw_input("\033[1;37m[ \033[1;31mEnter Target Sites \033[1;37m] ")
			a = slims(target, sys.argv[1])
	except:
		pass
    

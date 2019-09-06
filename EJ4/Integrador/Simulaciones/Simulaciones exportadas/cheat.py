import sys
import math

def main(*args, **kwargs):
	"""
		Usage:
			python cheat.py name_of_file -phase -module
	"""
	file = open("{}".format(args[0]), "r")
	new_file = open("{}_Cheated".format(args[0]), "w")

	for line in file.readlines():
		new_line = line
		
		try:
			freq, values = new_line.split("\t")
			mod, phase = values[1:-2].split(",")
			
			mod = float(mod[:-2])
			phase = float(phase[:-1])
			
			if "-phase" in args:
				if phase > 0:
					phase = -360 + phase
			if "-module" in args:
				mod = 10 ** (mod / 20)
			
			new_line = "{}\t({}{},{}°)\n".format(
				freq, mod, "dB", phase)
		except:
			pass
		
		new_file.write(new_line)
			
	new_file.close()
	file.close()

if __name__ == "__main__":
	main(*sys.argv[1:])

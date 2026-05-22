import os

def load_mods():
	mods = os.listdir("mods")
	for i in mods:
		mods_files = os.listdir("mods/" + i)
		for j in mods_files:
			mod = j[:-3]
			if j[-3:] == ".py":
				exec('import mods.' + i + "." + mod)
import os
patha = os.path.abspath(os.getcwd())
from mido import MidiFile


path = patha[:-7] +'group\\'

targets = []
for filename in os.listdir(path):
	if filename.endswith(".mid"):
		targets.append(filename)

print(targets[:5])

for fileN in targets:
	print(fileN)
	thisPath = path + fileN
	tracks = []
	check = open(thisPath)
	good = True
	try: 
		if str(check.read()).startswith('<'):
			good = False
	except Exception as e:
		pass


	if good:
		
		thisfile = MidiFile(thisPath, clip = True)
		for track in thisfile.tracks:
			tracks.append(track)

		for track in tracks:
			if track.name != '' and not track.name.startswith("Percussion"):
				newMidi = MidiFile()
				newMidi.tracks.append(track)
				if not os.path.exists(patha[:-7] +'solo\\'+track.name):
					os.makedirs(patha[:-7] +'solo\\'+track.name)
					print("making directory: ", 'solo\\'+track.name)
				try:
					newMidi.save(patha[:-7] +'solo\\'+track.name+'\\'+fileN[:-4]+'_'+track.name+'.mid')
				except Exception as e:
					pass
				print("saved...")
				print(patha[:-7] +'solo\\'+track.name+'\\'+fileN[:-4]+'_'+track.name+'.mid')



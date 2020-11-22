import mutagen
from mutagen.easyid3 import EasyID3
import os
files = os.listdir("music/")

for file in files:
	path = f"music/{file}"
	if "-" in file:
		if file.endswith('.mp3'):
			fName = file[:-4]
		data = fName.split(" - ")
		try:
			meta = EasyID3(path)
		except:
			meta = mutagen.File(path, easy=True)
			meta.add_tags()

		meta['title'] = data[1]
		meta['artist'] = data[0]
		meta.save()
		os.rename(f"music/{file}", f"music/{data[1]}.mp3")
	else:
		pass
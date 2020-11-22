import youtube_dl
import re

def run():
    file = open("URL.txt", "r")

    for video_url in file:

        video_info = youtube_dl.YoutubeDL().extract_info(url=video_url, download=False)
        filename = f"{video_info['title']}.ogg"
        filename = re.sub(r"/", " ", filename)

        options = {

			'format':'bestaudio/best',
        	'extractaudio':True,
        	'audioformat':'mp3',
        	'noplaylist':True,
        	'nocheckcertificate':True,
        	'proxy':"",
        	'addmetadata': True,
            'keepvideo': False,
            'outtmpl': f"music/{filename}",
			'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }

        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])

    file.close()


if __name__ == '__main__':
    run()
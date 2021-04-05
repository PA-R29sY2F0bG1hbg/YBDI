import os
import shutil

import youtube_dl

from Functions import RegexSpecC

url1 = "https://www.youtube.com/watch?v=t8vBMfgxwCQ"
url2 = "https://www.youtube.com/watch?v=gN_L27itbTA"

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

try:

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url2])

except:
    pass

with ydl:
    result = ydl.extract_info(
        '%s' % url2,
        download=False
    )

if 'entries' in result:
    # Can be a playlist or a list of videos
    video = result['entries'][0]

else:
    # Just a video
    video = result

# id = video['id']
mp3_title = video['title']
mp3_id = video['id']
n_tt = RegexSpecC.extract_word(mp3_title)

for file in os.listdir("."):
    # Webm Condition
    if file.endswith(".webm"):
        print("webm db", file)
        shutil.copy(file, "../mp3/" + n_tt + ".mp3")

    if file.endswith(".m4a"):
        print("m4a db", file)
        shutil.copy(file, "../mp3/" + n_tt + ".mp3")

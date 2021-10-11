# importing the module
from pytube import YouTube

# where to save
SAVE_PATH = "/Users/khushibansal/projects/python/"

# link of the video to be downloaded
link="https://www.youtube.com/watch?v=PyTjWK9qGSg"

try:
	# object creation using YouTube
	# which was imported in the beginning
	yt = YouTube(link)
except:
	print("Connection Error") #handling exception

print(yt.title)
print(yt.length)
print(yt.description)
print(yt.views)

try:
    vid = yt.streams.first()
    vid.download(SAVE_PATH)
except:
    print("Error101")
print('Task Completed!')
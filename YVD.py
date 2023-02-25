from pytube import YouTube

#taking link from user
link = input('Paste your link here : ')

# creating variable from youtube module
yt = YouTube(link)
#grabbing title
print(yt.title)
#grabbing streams
print(yt.streams, '\n')
#taking itag to select resolution to download
res = input('Enter itag : ')
stream = yt.streams.get_by_itag(res)
print('Downloading..')
print('Thanks for using Youtube downloader')
print('by Aayu ❤')
print('insta - @upskilllearner')
print('replit - @bugholic ')
print('Github - @bugholic')
#downloading video
stream.download()
print('Downloaded')

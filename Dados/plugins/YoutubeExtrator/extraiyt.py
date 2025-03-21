from pytube import YouTube

url = 'https://www.youtube.com/watch?v=HbN99f9esS4'

yt =   YouTube(url)

stream = yt.streams.get_highest_resolution()

stream.download("Dados/plugins/YoutubeExtrator/files")

print("Download concluido")
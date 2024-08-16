from pytube import YouTube
import ssl

ssl._create_default_https_context = ssl._create_stdlib_context
url = input("enter video url")

path = ""

stream = YouTube(url).streams.get_by_resolution('720p').download(path)
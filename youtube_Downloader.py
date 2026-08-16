from pytubefix import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url , save_path):
    try:
        yt = YouTube(url, client='MWEB',use_oauth=True, allow_oauth_cache=True)
        streams = yt.streams.filter(progressive=True,file_extension='mp4')
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print(f"Youtube video [{yt.title}] is downloaded successfully!")
    except Exception as e:
        print(e)

def open_file_dilog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder is {folder}")
    return folder

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()

    video_url = input('Please Enter a Youtube url: ')
    save_dir = open_file_dilog()

    if save_dir:
        print('Start Downloading ...')
        download_video(video_url,save_dir)
    else:
        print('Invalid save location!')
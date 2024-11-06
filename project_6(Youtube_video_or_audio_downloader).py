from pytube import YouTube, Playlist
from time import *

try:
    choice = input("Enter (Playlist) to download playlist. OR Enter (Other) to download video or audio: ")
    if choice.lower() == "other":
        link = input("Please Enter the link of the Youtube video to download: ")
        form = input(
            "If you want to download in video Enter (Video). OR If you want to download in audio Enter (Audio): ")
        youtube = YouTube(link)

        if form.lower() == "video":
            video = youtube.streams.filter(progressive=True, type="video").all()

        elif form.lower() == "audio":
            video = youtube.streams.filter(type="audio").all()

        else:
            print("You can Enter only (Video) or (Audio)")

        try:
            list_of_streams = list(enumerate(video))
            for i in list_of_streams:
                print(i)

            print()
            if form.lower() == "video":
                pixels = int(input("Enter: (0 or 1)"))
                print(f"Downloading.... {youtube.title}    in Video")
            elif form.lower() == "audio":
                pixels = int(input("Enter: (0 or 1 or 2 or 3 or 4 )"))
                print(f"Downloading.... {youtube.title}    in Audio")

            t0 = time()
            video[pixels].download()
            t1 = time()
            print("Successfully Downloaded")
            if form.lower() == "video":
                print(f"This video is downloaded in {round(t1 - t0)} seconds ")
                print(f"This video is downloaded in {round((t1 - t0) / 60, 2)} minutes ")
            elif form.lower() == "audio":
                print(f"This audio is downloaded in {round(t1 - t0)} seconds ")
                print(f"This audio is downloaded in {round((t1 - t0) / 60, 2)} minutes ")

        except:
            print("Invalid input")



    elif choice.lower() == "playlist":
        link = input("Please Enter the link of the Youtube video(playlist) to download: ")
        playlist = Playlist(link)

        a = input(
            "Enter (360p) to download playlist in 360p or Enter (720p) to download playlist in 720p or Enter (Audio) "
            "to download playlist in audio: ")

        if a.lower() == "360p":
            print(f"Downloading.... {playlist.title} in {a}")
            t0 = time()
            for video in playlist.videos:
                video.streams.filter(res="360p").first().download()
            t1 = time()
            print(f"This playlist of videos is downloaded in {round(t1 - t0)} seconds ")
            print(f"This playlist of videos is downloaded in {round((t1 - t0) / 60, 2)} minutes ")

        elif a.lower() == "720p":
            print(f"Downloading.... {playlist.title} in {a}")
            t0 = time()
            for video in playlist.videos:
                video.streams.filter(res="720p").first().download()
            t1 = time()
            print(f"This playlist of videos is downloaded in {round(t1 - t0)} seconds ")
            print(f"This playlist of videos= is downloaded in {round((t1 - t0) / 60, 2)} minutes ")

        elif a.lower() == "audio":
            sound_quality = input("Enter the sound Quality (like 48kbps,50kbps,70kbps,128kbps,160kbps)")
            if sound_quality.lower() == '48kbps':
                print(f"Downloading.... {playlist.title} in {a} quality {sound_quality}")
                t0 = time()
                for video in playlist.videos:
                    video.streams.filter(abr="48kbps", type="audio").first().download()
                t1 = time()
                print(f"This playlist of audio is downloaded in {round(t1 - t0)} seconds ")
                print(f"This playlist of audio is downloaded in {round((t1 - t0) / 60, 2)} minutes ")

            elif sound_quality.lower() == '50kbps':
                print(f"Downloading.... {playlist.title} in {a} quality {sound_quality}")
                t0 = time()
                for video in playlist.videos:
                    video.streams.filter(abr="50kbps", type="audio").first().download()
                t1 = time()
                print(f"This playlist of audio is downloaded in {round(t1 - t0)} seconds ")
                print(f"This playlist of audio is downloaded in {round((t1 - t0) / 60, 2)} minutes ")

            elif sound_quality.lower() == '70kbps':
                print(f"Downloading.... {playlist.title} in {a} quality {sound_quality}")
                t0 = time()
                for video in playlist.videos:
                    video.streams.filter(abr="70kbps", type="audio").first().download()
                t1 = time()
                print(f"This playlist of audio is downloaded in {round(t1 - t0)} seconds ")
                print(f"This playlist of audio is downloaded in {round((t1 - t0) / 60, 2)} minutes ")

            elif sound_quality.lower() == '128kbps':
                print(f"Downloading.... {playlist.title} in {a} quality {sound_quality}")
                t0 = time()
                for video in playlist.videos:
                    video.streams.filter(abr="128kbps", type="audio").first().download()
                t1 = time()
                print(f"This playlist of audio is downloaded in {round(t1 - t0)} seconds ")
                print(f"This playlist of audio is downloaded in {round((t1 - t0) / 60, 2)} minutes ")

            elif sound_quality.lower() == '160kbps':
                print(f"Downloading.... {playlist.title} in {a} quality {sound_quality}")
                t0 = time()
                for video in playlist.videos:
                    video.streams.filter(abr="160kbps", type="audio").first().download()
                t1 = time()
                print(f"This playlist of audio is downloaded in {round(t1 - t0)} seconds ")
                print(f"This playlist of audio is downloaded in {round((t1 - t0) / 60, 2)} minutes ")

            else:
                print("Sound Quality not found")

        else:
            print("Invalid Input.You can Enter only (720p) or (360p) or (Audio)")

    else:
        print("Invalid Input. You can Enter only (Other) or (Playlist)")


except Exception as e:
    print(f"An error occurred: {e}")

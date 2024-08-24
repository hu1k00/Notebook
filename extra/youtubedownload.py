from pytube import YouTube # type: ignore

def download_video(video_url, save_path):
    try:
        yt = YouTube(video_url)
        video = yt.streams.get_highest_resolution()
        video.download(save_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    save_path = "/home/hu1k0/Downloads"

    download_video(video_url, save_path)

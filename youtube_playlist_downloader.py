from pytube import Playlist

playlist = input("Enter Playlist URL: ")

p = Playlist(playlist)

output_folder = p.title + " By " + p.owner

print(f'\n Playlist Name: {p.title} \n')
i = 1
for video in p.videos:
    print(f"Downloading... {video.title}")
    file_name = f"{i} - {video.title}"
    video.streams.first().download(output_path=output_folder, filename=file_name)
    print("Downloaded \n")
    i = i + 1


print("All Videos are Downloaded Successfully")
input()

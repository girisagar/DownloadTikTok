# Download your TikTok Videos
  This program just download the videos from the file provided by tiktok.
  To download JSON file from your account follow these steps.
  Go to Settings > Data > Download Data > request data > JSON Format
  
  when requested data is ready to download. Download the file which is required with the command. 

## Prepare the program environment

1. clone this repo.
2. cd DownloadTikTok
3. python3 -m venv .envs
4. source .envs/bin/activate
5. pip install -r requirements.txt

## Run the command
Run this command (you must create the destination directory beforehand. In my case it's `~/Downloads/tiktokdownload/`)
```
   python tiktokdownload.py <your_file_from_tiktok_account>.json ~/Downloads/tiktokdownload/`
```

## Result - The Output of the program looks like this
```
-------------------------------------------------
found mp4
Downloading file: ~/Downloads/tiktokdownload/<yourvideolink>.mp4
~/Downloads/tiktokdownload/<yourvideolink>.mp4 downloaded!
.
.
.
```

# DMP – Download Manager

A simple desktop download manager I made for my own daily use. It's a small personal project, not a polished product, so expect rough edges and possible bugs.

<img width="737" height="527" alt="DMP screenshot" src="https://github.com/user-attachments/assets/add7d488-e8f2-4e9f-a372-97d9b8981b2c" />

## What it does

You paste a link and click **Start Download**:

- Links from video sites (YouTube, X/Twitter, Instagram, TikTok, Vimeo, Reddit, Yandex) are downloaded with [yt-dlp](https://github.com/yt-dlp/yt-dlp).
- For other links, DMP sends a `HEAD` request to check the content type. Web pages go to yt-dlp; direct files are downloaded by `downloader.py`, which splits the file into 4 parts and downloads them in separate threads using HTTP `Range` requests, then merges them.

There is also a **Cancel** button and an **Open Downloads** button. Files are saved to `Downloads/DMP_Downloads` in your home folder (videos go into a `vids` subfolder).

## Running it

```bash
git clone https://github.com/GreyTheGangalf/DMP.git
cd DMP
pip install requests yt-dlp customtkinter
python main.py
```

A Windows build made with PyInstaller is in the `dist` folder.

A few notes:

- Downloading the best video quality needs [FFmpeg](https://ffmpeg.org/) to merge video and audio.
- YouTube changes often. If video downloads stop working, updating yt-dlp (`pip install -U "yt-dlp[default]"`) usually helps; recent versions also need a JavaScript runtime such as [Deno](https://deno.com/) for YouTube.

## Limitations

This is built for simple, everyday use:

- One download at a time, no queue, no pause/resume.
- The number of connections is fixed at 4.
- It has only been tested by me on my own Windows machine, so it may not work with every site or server.

Bug reports and suggestions are welcome through Issues.

## Built with

Python, CustomTkinter, Requests, yt-dlp, `threading`, PyInstaller.

## License

MIT – see [LICENSE](LICENSE).

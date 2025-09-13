# concatvids

**concatvids** is a Python command-line tool for concatenating video files (such as .mp4) using ffmpeg, automatically sorting them by modification date. Very useful for quickly merging separately recorded clips, such as GoPro videos.

📖 Read this in other languages:  
- [Português (Brasil)](README.pt-br.md)

---

## ✅ Features

- Detects and sorts videos by modification date (oldest first)
- Automatically generates a `filelist.txt` in the format accepted by `ffmpeg`
- Concatenates videos via `ffmpeg` using the fast mode (`-c copy`)
- Allows setting the output file name via `-o`
- Optional upload to YouTube with secure OAuth2 authentication
- Optional re-encoding to ensure audio/video compatibility
- Optional video trimming with `--ss` (start) and `--to` (end)
- Compatible with Windows, Linux, and macOS (requires `ffmpeg` installed)

---

## 🚀 Installation

### 1. Clone the repository:

```bash
git clone git@github.com:your-username/concatvids.git
cd concatvids
```

### 2. Install with `pip`:

```bash
pip install .
```

> This installs the `concatvids` command globally if you have the proper permissions (or inside a virtual environment).

---

## 🧪 Requirements

* Python 3.7+
* [`ffmpeg`](https://ffmpeg.org/download.html) installed and available in the `PATH`
* Google account with access to the [YouTube Data API v3](https://console.developers.google.com/)
* `client_secrets.json` file saved at `~/.config/concatvids/`.

---

## 💻 Usage

### Basic command:

```bash
cd folder_with_videos
concatvids
```

### Custom output file name:

```bash
concatvids -o my_final_video.mp4
```

### Using another video extension (e.g., `.mov`):

```bash
concatvids --ext mov -o result.mov
```

---

### ✂️ Cutting a video

You can also cut a single video by specifying the **start time** (`--ss`) and **end time** (`--to`):

```bash
concatvids -i input.mp4 --ss 00:00:10 --to 00:00:20 -o clip.mp4
```

If `-o` is not provided, the default output file is `output.mp4`.

---

### 📤 Upload to YouTube and avoid timestamp errors

```bash
concatvids --upload --title "Training 21/07" --description "Drills with paddles" --tags swimming training gopro
```

Use `--reencode` if you encounter timestamp issues:

```bash
concatvids --reencode -o final_video.mp4
```

---

## 📝 Example of generated `filelist.txt`

```text
file 'clip1.mp4'
file 'clip2.mp4'
file 'clip3.mp4'
```

---

## 🛠 Development

```bash
pip install -e .
pip install -r requirements.txt
```

---

## 📄 License

[MIT](LICENSE)

---

## 🤝 Contributions

Open an issue or pull request to suggest improvements or fix problems.

## ✍️ Credits

Created by André F., developed with support from ChatGPT / OpenAI.

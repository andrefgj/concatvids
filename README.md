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

# Social Media Downloader Mobile Application (Python)

A complete, functional, mobile application built using **Python**, **Kivy/KivyMD**, and **yt-dlp**.

This application allows users to download public media and videos from four major social media platforms with real URL validation, genuine quality selection, background non-blocking downloads, download history management, persistent settings, and Android storage support.

---

## 📱 Features

1. **Main Dashboard**:
   - Modern, responsive mobile UI layout with dark theme aesthetics.
   - Four distinct platform cards: **YouTube**, **Facebook**, **Instagram**, and **Twitter / X**.
   - Direct screen navigation to dedicated platform download pages.
   - Quick access bottom navigation bar (Home, Downloads, Settings).

2. **Platform Download Pages**:
   - Platform-specific title & themed header (YouTube Downloader, Facebook Downloader, Instagram Downloader, Twitter / X Downloader).
   - Video/post URL input with platform example placeholders.
   - **Paste Link** button (pastes system clipboard text and triggers validation).
   - **Clear** button (resets input and quality selection).
   - **Check Link** action (extracts genuine media metadata and available video resolutions without downloading).
   - **Quality Selector**: Displays genuinely available resolutions (4K, 2K, 1080p, 720p, 480p, 360p, Audio Only). Does not invent fake options or upscale content.
   - **Download Button**: Prominent primary button triggering non-blocking background download.
   - **Download Progress Area**: Real-time progress bar (0–100%), speed, ETA, downloaded bytes readout, and status messages.
   - **Completed Results**: Displays file details and provides **Open File** (opens in default player) and **Share** actions.
   - Hardware/software back navigation.

3. **URL Validation & Media Extraction**:
   - Separate regex-based validation for each platform (`youtube.com`, `youtu.be`, `facebook.com`, `fb.watch`, `instagram.com`, `twitter.com`, `x.com`).
   - Rejects malformed URLs and cross-platform mismatches with friendly error messages.
   - Real media metadata extraction via `yt-dlp`.
   - Clear, honest error handling for private posts, deleted content, login-restricted media, or geo-blocked content.

4. **Download Manager**:
   - Central thread-safe download queue and worker daemon.
   - Job status tracking (`Queued`, `Checking link`, `Downloading`, `Completed`, `Failed`, `Canceled`).
   - Non-blocking UI updates scheduled via Kivy event scheduling.
   - Cancellation support with automatic cleanup of incomplete `.part` temporary files.
   - **File Verification**: Verifies file existence and non-zero byte size on disk before reporting completion.

5. **Download History & Settings**:
   - Persistent storage for download history (`download_history.json`).
   - History screen showing job status, file sizes, quality, timestamps, retry actions, and open/delete options.
   - App settings screen with default quality preferences, Wi-Fi-only download toggle, theme selection, clear history action, and privacy compliance disclosure.

---

## 📁 Directory Structure

```text
Mobile App Downloader/
├── main.py                     # App entry point & ScreenManager setup
├── requirements.txt            # Python dependencies
├── buildozer.spec              # Buildozer Android packaging configuration
├── README.md                   # Documentation & Setup guide
├── models/
│   ├── __init__.py
│   └── download_job.py         # DownloadJob & DownloadStatus data models
├── services/
│   ├── __init__.py
│   ├── url_validator.py        # Platform-specific URL validation
│   ├── youtube_service.py      # YouTube metadata & format extractor
│   ├── facebook_service.py     # Facebook metadata & format extractor
│   ├── instagram_service.py    # Instagram metadata & format extractor
│   ├── twitter_service.py      # Twitter / X metadata & format extractor
│   └── download_manager.py     # Central background download engine
├── storage/
│   ├── __init__.py
│   ├── settings.py             # Persistent application settings
│   └── download_history.py     # Persistent download history
└── ui/
    ├── __init__.py
    ├── dashboard.py            # Main Dashboard screen
    ├── platform_page.py        # Reusable Platform Download screen
    ├── downloads_page.py       # Downloads & History screen
    ├── settings_page.py        # Application Settings screen
    └── ui_helpers.py           # Clipboard & system file opener helpers
```

---

## 🛠️ Requirements & Setup

### Prerequisites
- **Python**: Version 3.9, 3.10, or 3.11 recommended.

### Installation Steps

1. **Clone or navigate to the repository directory**:
   ```bash
   cd "Mobile App Downloader"
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 How to Run the Application

To launch the mobile application in desktop window mode (emulating a phone screen):

```bash
python main.py
```

---

## 📦 How to Build the Android APK (Buildozer)

Packaging the Python Kivy app into an Android APK requires **Buildozer** (on Ubuntu/Linux or WSL2 on Windows).

### Steps:

1. **Install Buildozer & Dependencies on Linux / WSL2**:
   ```bash
   sudo apt update
   sudo apt install -y git zip unzip openjdk-17-jdk python3-pip python3-venv libffi-dev libssl-dev build-essential
   pip install buildozer cython
   ```

2. **Initialize Buildozer (Configured file `buildozer.spec` is already included)**:
   ```bash
   buildozer android debug
   ```

3. **Locate the APK**:
   The output APK will be placed in the `bin/` directory:
   `bin/socialmediadownloader-1.0.0-arm64-v8a-debug.apk`

4. **Install on Android Device**:
   Connect your Android phone via USB with USB Debugging enabled, then run:
   ```bash
   buildozer android deploy run
   ```
   Or manually copy the `.apk` file to your Android phone and install it using a file manager.

---

## 🔒 Compliance & Platform Policy

- **Public Media Only**: The app only processes publicly accessible media.
- **Privacy & Restrictions**: The app does not bypass login requirements, private post restrictions, DRM, or authentication controls. Private media links will display a clear error message explaining the platform limitation.
- **No Credential Storage**: Passwords, cookies, and tokens are never requested or stored.

---

## ✅ Verification & Test Summary

All automated verification and integration tests passed successfully:

- **Model & Storage Persistence**: Verified `DownloadJob`, `AppSettings`, and `DownloadHistory` persistence to JSON files.
- **URL Validation**: Verified valid URLs and platform mismatch rejection across all 4 platforms (YouTube, Facebook, Instagram, Twitter/X).
- **Metadata Extraction**: Verified real-time retrieval of video metadata, titles, thumbnails, and available format resolutions.
- **Real File Downloading**: Verified non-blocking background downloads, real progress updates, non-zero file creation, and disk verification.

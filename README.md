# Create Short YouTube Video

> **Disclaimer:** This project is intended for educational purposes and personal use only. Ensure you have the right to download and edit any YouTube videos you process with this tool.

## 📋 Description

This Python-based project allows users to download YouTube videos and create shorter clips by identifying the best moments within the video. It leverages various scripts to handle downloading, editing, and processing tasks.

## 🛠️ Features

- **YouTube Video Downloading:** Fetch videos from YouTube in high definition.
- **Best Moment Detection:** Analyze videos to extract the most engaging segments.
- **Video Editing:** Trim and compile video segments into a cohesive short clip.

## 📂 Project Structure

- `main.py` – Orchestrates the workflow for creating short videos.
- `youtube_downloader_hd.py` – Downloads YouTube videos in HD.
- `best_moment_in_video.py` – Detects the most engaging segments in a video.
- `edit_video.py` – Handles cutting and assembling video segments.
- `requirements.txt` – Lists Python dependencies.
- `Dockerfile` – Docker image configuration.
- `docker-compose.yaml` – Docker Compose configuration.

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Docker (optional)

### Installation

Clone the repository:
```bash
git clone https://github.com/Chadi-Mangle/create-short-youtube-video.git  
cd create-short-youtube-video
```

Install the Python dependencies:
```bash
pip install -r requirements.txt
```

### Usage

Run the script:
```bash
python main.py
```

Follow the prompts to enter a YouTube URL and begin the short video creation process.

## 🐳 Docker Usage (Optional)

Build the image:
```bash
docker build -t create-short-youtube-video .
```

Run with Docker Compose:
```bash
docker-compose up
```

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to improve.

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 📬 Contact

For questions or suggestions, feel free to open an issue on the GitHub repository.

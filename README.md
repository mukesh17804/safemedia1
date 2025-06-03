# 🔐 SafeMedia AI – Real-Time WhatsApp Media Scanner

🚀 SafeMedia AI is an AI-powered tool that scans media files (images/videos) received via WhatsApp **in real time** to detect **phishing** or **malware attacks** hidden in seemingly harmless files.

> “Stay safe before you click, not after.” — SafeMedia AI

---

## 📌 Project Purpose

With the rise in **cyberattacks via WhatsApp**, malicious actors now send virus-infected or phishing images/videos. When a user downloads them, they unknowingly give hackers access to personal data.  
**SafeMedia AI** is built to solve this real-time threat using AI + automation.

---

## 🛠️ Features

✅ Real-time scanning of WhatsApp media folder  
🖼️ Detects suspicious file names and phishing-style images  
📁 Folder watcher using `watchdog`  
🌐 Flask-based web dashboard  
🔔 Instant terminal alerts for malicious content  
🧪 Includes fake phishing image for demo/testing  
💡 Designed for easy integration with ML image classifiers

---

## 🧪 Demo

> Here's how it works:

1. You receive a new image/video via WhatsApp.
2. SafeMedia AI scans the file instantly.
3. If malicious content is detected, you’re alerted **before opening** the file.
4. Optionally, the file can be quarantined or blocked.

---

## 🧠 Technologies Used

| Component       | Technology     |
|----------------|----------------|
| Language        | Python 3.11+   |
| Backend         | Flask          |
| Real-time FS Watch | watchdog   |
| Image Processing | Pillow (PIL)  |
| Web Interface    | HTML/CSS (Flask UI) |
| Testing Tool     | Fake phishing generator |

---

## 📂 Folder Structure

```bash
safemedia_ai/
│
├── app.py                   # Flask app server
├── scanner.py               # Media scanning logic
├── phishing_generator.py    # Generates fake phishing image for testing
├── static/
│   └── styles.css
├── templates/
│   └── index.html           # UI page
├── whatsapp_media/          # Media folder to watch (create this!)
└── README.md

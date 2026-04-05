# 🚀 Simplicode – Multi-Language Cloud Code Runner

Simplicode is a browser-based cloud code execution platform that allows users to write and run code in multiple programming languages directly from the browser.

It provides a clean IDE-like experience using Monaco Editor and executes code using a Flask backend.

---

## 🌐 Live Demo

👉 https://simplicode.onrender.com

---

## ✨ Features

* 🧠 Monaco Editor (VS Code-like experience)
* ⚡ Real-time code execution
* 🌍 Supports multiple languages:

  * Python ✅
  * C (local) 💻
  * Java (local) ☕
* 🎯 Clean and responsive UI
* 📋 Copy output feature
* ⏱ Execution timeout handling
* 🧹 Auto cleanup of temporary files

---

## 🏗 Tech Stack

### Frontend

* HTML
* CSS (custom styling + animations)
* JavaScript
* Monaco Editor

### Backend

* Python
* Flask

### Deployment

* Render

---

## 📂 Project Structure

```
simplicode/
│
├── app.py
├── requirements.txt
├── render.yaml
│
├── static/
│   ├── style.css
│   └── script.js
│
└── templates/
    └── index.html
```

---

## ⚙️ How It Works

1. User writes code in the editor
2. Code is sent to Flask backend via API
3. Backend:

   * saves code temporarily
   * compiles/runs based on language
   * captures output/error
4. Output is sent back and displayed

---

## ▶️ Run Locally

### 1. Clone the repo

```
git clone https://github.com/laharirr/Simplicode.git
cd Simplicode
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the server

```
python app.py
```

### 4. Open browser

```
http://127.0.0.1:5000
```

---

## ⚠️ Important Notes

* Python works both locally and on deployed version
* C and Java work **locally only**
* Render does not support GCC/Javac by default

---

## 🚀 Future Improvements

* 🔐 User authentication (Login/Signup)
* 📜 Code history storage
* 🐳 Docker-based secure execution
* 🌐 Full multi-language support in cloud
* 🎨 Theme switching (Dark/Light mode)

---

## 💡 Inspiration

Inspired by platforms like:

* Replit
* HackerRank
* OnlineGDB

---

## 👩‍💻 Author

**Lahari R**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!

---

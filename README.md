# 🖼️ Image to Story + Speech GenAI Tool

## 📌 Overview

This project is a **Multimodal AI System** that converts an image into:

* 🧠 Scene description
* 📖 AI-generated story
* 🔊 Speech (audio output)

It uses **Computer Vision + LLM + Text-to-Speech** to generate meaningful content from images.

---

## 🚀 Features

* 📷 Upload an image
* 🧠 Generate scene description using BLIP model
* ✍️ Create a story using LLM (Falcon model)
* 🔊 Convert story into speech (audio file)
* 🎨 Customize story style (Romantic, Horror, Funny, etc.)
* 🎚️ Control creativity level

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Hugging Face Transformers
* BLIP (Image Captioning)
* Falcon LLM (Text Generation)
* pyttsx3 (Text-to-Speech)

---

## 📂 Project Structure

```
project/
│── app.py                  # Main application
│── utils/
│   └── custom.py           # UI styling
│── img/                    # Sample images
│── generated_audio_*.mp3   # Output audio files
│── requirements.txt        # Dependencies
│── .env                    # API keys (NOT uploaded)
│── README.md
│── LICENSE
```

---

## 🔐 Environment Variables (IMPORTANT)

Create a `.env` file in your project root:

```
HUGGINGFACE_API_TOKEN=your_api_key_here
```

⚠️ Never upload `.env` to GitHub

---

## 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

Dependencies used in this project: 

---

## ▶️ How to Run

```bash
streamlit run app.py
```

Then open browser:

```
http://localhost:8501
```

---

## 🔄 How It Works

1. Upload image
2. Model generates description
3. LLM creates story
4. System converts story → speech

Code reference: 

---

## 📸 Input / Output

### 📷 Input

* Image file (jpg, png)

### 📖 Output

* Scene description
* Generated story
* Audio file (.mp3)

---

## 🎯 Example Workflow

1. Upload image
2. Choose story style
3. Adjust creativity
4. Click generate
5. Get:

   * Story 📖
   * Audio 🔊

---

## ⚠️ Important Notes

* Do NOT upload `venv/` folder
* Do NOT upload `.env` file
* Requires internet for model loading
* First run may be slow (model download)

---

## 🤝 Contributing

Feel free to fork and improve this project.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

**Reeya Pandey**

---

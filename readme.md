# 🎙️ Arnaldo: Python Voice Assistant

This is a simple virtual assistant developed during my bootcamp, capable of recognizing voice commands in **Portuguese** to automate basic tasks on Windows.


## ✨ Features
* **Name Activation:** Responds only when called by "Arnaldo".
* **Web Search:** Opens the browser and performs automatic Google searches.
* **Quick Access:** Voice shortcuts for YouTube and Social Media.
* **Utilities:** Opens Notepad and announces the current time.
* **Coin Flip Logic:** "Heads or Tails" function for quick decisions.

## 🚀 Technologies Used
* [Python 3.13+](https://www.python.org/)
* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) - For converting audio to text.
* [PyAudio](https://pypi.org/project/PyAudio/) - For capturing microphone input.
* [Webbrowser & OS](https://docs.python.org/3/library/) - Native libraries for system control.

---

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/enoGuarana/arnaldo-assistant.git
   cd arnaldo-assistant
   ```

2. Create and activate a virtual environment:
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   > 💡 **Note for Windows users:** If you encounter errors installing `PyAudio`, download the appropriate `.whl` file from [Gohlke's unofficial binaries](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install it with:
   > ```bash
   > pip install path/to/PyAudio‑x.x.x‑cp313‑win_amd64.whl
   > ```

4. Run the assistant:
   ```bash
   python main.py
   ```

---

## 🗣️ Supported Voice Commands (in Portuguese)

| Command | Action |
|---------|--------|
| *"Arnaldo"* | Activates listening mode |
| *"Pesquise por [termo]"* | Opens Google search for the term |
| *"Abrir YouTube"* | Launches YouTube in default browser |
| *"Abrir Instagram"* / *"Abrir LinkedIn"* | Opens respective social media |
| *"Abrir bloco de notas"* | Launches Windows Notepad |
| *"Que horas são?"* | Speaks the current time |
| *"Cara ou Coroa"* | Flips a virtual coin (Heads/Tails) |
| *"Sair"* / *"Encerrar"* | Exits the assistant |

---

## ⚙️ Project Structure

```
arnaldo-assistant/
│
├── main.py              # Main entry point & command logic
├── requirements.txt     # Project dependencies
├── utils/
│   ├── speech_handler.py  # Speech recognition & TTS functions
│   └── system_actions.py  # Browser, OS, and utility functions
└── README.md            # Project documentation
```

---

## 🔧 Customization

You can easily extend Arnaldo by editing the command mapping in `main.py`:

```python
COMMANDS = {
    "pesquise por": search_google,
    "abrir youtube": open_youtube,
    "que horas são": get_time,
    # Add your own commands here!
}
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs or suggest improvements
- 💡 Propose new voice commands or features
- 🌍 Add support for additional languages

1. Fork the project
2. Create your feature branch: `git checkout -b feature/AmazingFeature`
3. Commit your changes: `git commit -m 'Add some AmazingFeature'`
4. Push to the branch: `git push origin feature/AmazingFeature`
5. Open a Pull Request

---

## 📫 Let's Connect!

Developed with ❤️ by **João Enomoto** during a Machine Learning & GenAI Bootcamp.

[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/joaoenomoto)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/enoGuarana)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:jvrenomoto@gmail.com)

---

> 💡 *"Automation begins with a single command. Arnaldo is a small step toward making technology more accessible through voice."*

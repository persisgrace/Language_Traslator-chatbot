# Language Translator Chatbot

A simple web-based chatbot that translates phrases to multiple languages, including **Tamil, Telugu, Hindi, French, Spanish, and English**. Built with Flask, the Googletrans library, and a modern, user-friendly interface.

## Features

- Translate any phrase into supported languages
- Auto-detects input language
- Simple, clean UI with a light theme, purple accent, green user messages, and blue bot messages
- Supports natural text commands like:
  - `Naku bore kodtundhi to English`
  - `I am hungry in Tamil`
  - `how are you French`

## Screenshots

> ![Chatbot UI Screenshot](screenshot.png)

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/language-chatbot.git
cd language-chatbot
```

### 2. Install dependencies

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

Install required packages:

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
python app.py
```

The app will be available at [http://localhost:5000](http://localhost:5000).

## Usage

Type your phrase and the language you want to translate to.  
Examples:
- `nenu bayatiki vellali to English`
- `how are you in Tamil`
- `bonjour to Hindi`

The chatbot will reply with the translated phrase.

## Project Structure

```
.
├── app.py
├── bot.py
├── requirements.txt
├── static/
│   └── style.css
├── templates/
│   └── index.html
└── README.md
```

## Supported Languages

| Language | Code |
|----------|------|
| English  | en   |
| French   | fr   |
| Hindi    | hi   |
| Telugu   | te   |
| Spanish  | es   |
| Tamil    | ta   |

## Customization

- To add more languages, update the `lang_map` in `bot.py`.
- To change the UI, edit `static/style.css`.

## License

This project is licensed under the MIT License.

---

**Enjoy translating!**

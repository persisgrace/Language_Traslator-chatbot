import re
from googletrans import Translator

class LanguageBot:
    def __init__(self):
        self.translator = Translator()

    def handle_message(self, message):
        phrase, target_lang = self.extract_phrase_and_lang(message)
        if phrase and target_lang:
            translated = self.translator.translate(phrase, dest=target_lang)
            return f"'{phrase}' in {target_lang.capitalize()} is: '{translated.text}'"
        else:
            return "Please provide a phrase and the language you want to translate to."

    def extract_phrase_and_lang(self, message):
        # Extended to support Tamil
        patterns = [
            r"(.+?)\s+to\s+(\w+)$",
            r"(.+?)\s+in\s+(\w+)$",
            r"(.+?)\s+(\w+)$"
        ]
        lang_map = {
            "english": "en", "en": "en",
            "french": "fr", "fr": "fr",
            "hindi": "hi", "hi": "hi",
            "telugu": "te", "te": "te",
            "spanish": "es", "es": "es",
            "tamil": "ta", "ta": "ta"   # <-- Added Tamil support
        }
        for pat in patterns:
            match = re.match(pat, message.strip(), re.IGNORECASE)
            if match:
                phrase = match.group(1).strip()
                lang = match.group(2).strip().lower()
                target_lang = lang_map.get(lang, "en")
                return phrase, target_lang
        return None, None
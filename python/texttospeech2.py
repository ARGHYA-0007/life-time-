# filename: tts_hindi_gtts.py
from gtts import gTTS
import os
import sys
import tempfile

def speak_hindi(text, slow=False, filename=None):
    """Convert Hindi text to speech and play it.
    - text: str (Hindi text / unicode)
    - slow: bool (slower speech if True)
    - filename: optional path to save .mp3; if None, uses a temp file and auto-opens it.
    """
    if not text:
        raise ValueError("Empty text provided")

    tts = gTTS(text=text, lang='hi', slow=slow)

    if filename:
        out_path = filename
    else:
        fd, out_path = tempfile.mkstemp(suffix=".mp3")
        os.close(fd)

    tts.save(out_path)
    print(f"Saved TTS to: {out_path}")

    # Play file cross-platform
    if sys.platform.startswith("win"):
        os.startfile(out_path)             # Windows: opens default media player
    elif sys.platform == "darwin":
        os.system(f"open {out_path!r}")   # macOS
    else:
        os.system(f"xdg-open {out_path!r}")  # Linux (xdg-open should be available)

if __name__ == "__main__":
    hindi_text = """कल रात ना भाई, पूरा सीन ही अलग हो गया था। हम लोग अड्डे पे बैठे थे, 
    तभी यार का फोन आया – ‘भाई जल्दी आ, फुल झोल चल रहा है।’ अब सोचा चल, देखते हैं क्या मामला है।
      वहाँ पहुँचे तो सबका मूड टाइट था, गप्पे-शप्पे चल रही थीं और चाय वाला भी अपना फुल ऑन तड़का मार रहा था।
        फिर क्या, टाइमपास शुरू – मीम्स, मज़ाक, और थोड़ी लड़ाई-झगड़ा वाली डिबेट भी। एंड में सबने बोला – ‘भाई, 
        अगली बार का प्लान और भी लिट होना चाहिए।"""
    speak_hindi(hindi_text)

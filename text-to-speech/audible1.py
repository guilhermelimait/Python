import pyttsx3
import sys

def speak(text, rate=150, volume=1.0):
    """Convert text to speech with customizable settings"""
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', rate)  # Speed of speech
        engine.setProperty('volume', volume)  # Volume (0.0 to 1.0)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Allow text as command line argument or use default
    text = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "That is awesome!"
    speak(text)
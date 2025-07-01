from RealtimeTTS import TextToAudioStream, EdgeEngine
import time # Re-import time for sleep
import os
import keyboard # Import the keyboard library

# Configuration Constants
TEXT_TO_SPEAK = "Pari Khan Khanum (1548–1578) was a Safavid princess, the daughter of the second Safavid shah, Tahmasp I, and of his Circassian consort, Sultan-Agha Khanum. Pari Khan played a central role in the succession crisis after her father's death in 1576. " \
"In later chronicles she was portrayed as a villain who murdered two brothers and tried to usurp the throne."
TTS_PROVIDER = "edge"
TTS_VOICE = "en-US-GuyNeural" # You can change this to any installed Edge voice

def main():
    """
    Main function to demonstrate text-to-audio streaming with spacebar for pause/resume.
    """
    try:
        # Set MPV_HOME environment variable to help RealtimeTTS locate mpv
        os.environ["MPV_HOME"] = "C:\\MPV"

        # Start streaming audio using Edge as the TTS provider
        engine = EdgeEngine()
        engine.set_voice(TTS_VOICE)
        stream = TextToAudioStream(engine=engine)
        stream.feed(TEXT_TO_SPEAK).play_async()

        print("Press SPACE to toggle pause/resume. Press ESC to exit.")

        paused = False
        while True:
            if keyboard.is_pressed('space'):
                if not paused:
                    print("Pausing...")
                    stream.pause()
                    paused = True
                else:
                    print("Resuming...")
                    stream.resume()
                    paused = False
                # Debounce the key press to avoid multiple toggles from a single press
                print("space pressed")
                time.sleep(0.2) # Small delay to debounce and prevent multiple rapid toggles
            elif keyboard.is_pressed('esc'):
                print("Exiting...")
                break

    except Exception as e:
        print(f"An error occurred during TTS stream initialization or playback: {e}")
        # In a real application, you might log the error,
        # attempt a retry, or notify the user.

if __name__ == "__main__":
    main()

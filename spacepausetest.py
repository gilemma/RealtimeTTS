import asyncio
from RealtimeTTS import TextToAudioStream
import keyboard

# Set up your TTS model and provider
stream = TextToAudioStream(provider="edge", voice="en-US-AriaNeural")

paused = False

async def stream_with_pause(text):
    global paused
    async for chunk in stream.stream(text):
        while paused:
            await asyncio.sleep(0.1)  # Wait while paused
        await stream.play(chunk)

def toggle_pause(e):
    global paused
    paused = not paused
    print("Paused" if paused else "Unpaused")

keyboard.on_press_key("space", toggle_pause)

async def main():
    text = "This is an example of real-time text to speech with pause and unpause functionality."
    await stream_with_pause(text)

asyncio.run(main())
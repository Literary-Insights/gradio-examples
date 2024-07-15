import gradio as gr
from gtts import gTTS
import os

def text_to_speech(text, language, filename):
    if not text:
        return "Please enter some text.", None, None

    if not filename:
        filename = "output.mp3"
    elif not filename.endswith(".mp3"):
        filename += ".mp3"

    try:
        tts = gTTS(text=text, lang=language)
        tts.save(filename)
        return f"Audio saved as {filename}", filename, filename

    except Exception as e:
        return f"An error occurred: {e}", None, None

# Define the Gradio interface
iface = gr.Interface(
    fn=text_to_speech,
    inputs=[
        gr.Textbox(lines=5, placeholder="Enter text here...", label="Enter text"),
        gr.Dropdown(choices=["en", "es", "fr", "de", "it", "pt", "nl"], value="en", label="Select language"),
        gr.Textbox(default="output.mp3", placeholder="output.mp3", label="Filename")
    ],
    outputs=[
        gr.Textbox(label="Status"),
        gr.File(label="Download MP3"),
        gr.Audio(label="Play MP3")
    ],
    title="Text to Speech Converter",
    description="Enter text, select a language, and provide a filename to generate an MP3 file using gTTS."
)

# Launch the interface
iface.launch()

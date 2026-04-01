import os
import time
import io
import pyttsx3
from typing import Any

import streamlit as st
from PIL import Image
from dotenv import find_dotenv, load_dotenv
from transformers import (
    BlipProcessor,
    BlipForConditionalGeneration,
    BlipConfig,
    pipeline
)

from utils.custom import css_code

# Load environment variables
load_dotenv(find_dotenv())
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

if not HUGGINGFACE_API_TOKEN:
    st.error("Hugging Face API key not found. Please check your .env file.")
    st.stop()


# ------------------ PROGRESS BAR ------------------
def progress_bar(amount_of_time: int) -> Any:
    progress_text = "✨ Generating magic..."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(amount_of_time):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)

    my_bar.empty()


# ------------------ LOAD MODELS ------------------
@st.cache_resource
def load_blip_models():
    config = BlipConfig.from_pretrained("Salesforce/blip-image-captioning-base")
    config.tie_word_embeddings = False

    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained(
        "Salesforce/blip-image-captioning-base",
        config=config,
        ignore_mismatched_sizes=True
    )

    return processor, model


@st.cache_resource
def load_story_model():
    return pipeline(
        "text-generation",
        model="tiiuae/falcon-rw-1b"
    )


# ------------------ IMAGE → TEXT ------------------
def generate_text_from_image(_bytes: bytes) -> str:
    processor, model = load_blip_models()

    image = Image.open(io.BytesIO(_bytes)).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")

    output_ids = model.generate(**inputs, max_new_tokens=100)

    generated_text = processor.decode(output_ids[0], skip_special_tokens=True)

    return generated_text


# ------------------ TEXT → STORY ------------------
def generate_story_from_text(scenario: str, style: str, creativity: float) -> str:
    try:
        generator = load_story_model()

        prompt = f"""
You are a professional story writer.

Scene: {scenario}

Write ONLY one short {style.lower()} story.

Rules:
- Maximum 100 words
- Stay strictly relevant to the scene
- Do NOT include instructions, prompts, or questions
- Do NOT switch topic
- Make it meaningful and complete
- Include emotions and actions
- Start directly with the story

Story:
"""

        result = generator(
            prompt,
            max_new_tokens=120,
            do_sample=True,
            temperature=creativity,
            top_p=0.9,
            repetition_penalty=1.2
        )

        text = result[0]["generated_text"]

        # 🔥 CLEAN OUTPUT (VERY IMPORTANT)
        story = text.replace(prompt, "").strip()

        # Remove junk after story
        stop_words = ["Write", "Prompt:", "Essay", "Question:", "\n\n"]
        for word in stop_words:
            if word in story:
                story = story.split(word)[0]

        return story.strip()

    except Exception as e:
        return f"Error generating story: {str(e)}"


# ------------------ TEXT → SPEECH ------------------
def generate_speech_from_text(message: str) -> str:
    engine = pyttsx3.init()

    audio_filename = f"generated_audio_{int(time.time())}.mp3"

    engine.save_to_file(message, audio_filename)
    engine.runAndWait()

    return audio_filename


# ------------------ MAIN APP ------------------
def main():
    st.set_page_config(page_title="Image to Story", page_icon="🖼️")

    st.markdown(css_code, unsafe_allow_html=True)

    st.header("🖼️ Multimodal AI System for Image-to-Story Generation with Speech Synthesis")

    # 🎛️ Controls
    st.subheader("🎨 Customize your story")

    style = st.selectbox(
        "Choose Story Style",
        ["Romantic", "Funny", "Horror", "Adventure", "Fantasy"]
    )

    creativity = st.slider(
        "Creativity Level",
        0.3, 1.0, 0.8
    )

    uploaded_file = st.file_uploader(
        "Upload an image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        st.image(uploaded_file, caption="📷 Uploaded Image")

        progress_bar(100)

        try:
            scenario = generate_text_from_image(bytes_data)

            # Enhance scenario
            scenario = f"A detailed scene: {scenario}. Describe emotions, setting, and actions clearly."
            
            
            # Step 2
            story = generate_story_from_text(
                scenario,
                style,
                creativity
            )

            # Step 3
            audio_file = generate_speech_from_text(story)

        except Exception as e:
            st.error(f"Error: {str(e)}")
            return

        # ------------------ OUTPUT UI ------------------

        st.markdown(
            f"""
            <div class="custom-box">
                <h3>📖 Generated Scenario</h3>
                <p>{scenario}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="custom-box">
                <h3>✍️ Generated Story</h3>
                <p>{story}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("### 🔊 Listen to your story")
        st.audio(audio_file)


if __name__ == "__main__":
main()

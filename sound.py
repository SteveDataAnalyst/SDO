import streamlit as st
import time

def play_incorrect_sound():
    html_string = """
                <audio controls autoplay>
                  <source src="https://github.com/SteveDataAnalyst/SDO/raw/main/Incorrect-sound-effect.mp3" type="audio/mp3">
                </audio>
                """

    sound = st.empty()
    sound.markdown(html_string,
                   unsafe_allow_html=True)  # will display a st.audio with the sound you specified in the "src" of the html_string and autoplay it
    time.sleep(2)  # wait for 2 seconds to finish the playing of the audio
    sound.empty()  # optionally delete the element afterwards

def play_correct_sound():
    html_string = """
                <audio controls autoplay>
                  <source src="https://github.com/SteveDataAnalyst/SDO/raw/main/Game-show-correct-answer.mp3" type="audio/mp3">
                </audio>
                """

    sound = st.empty()
    sound.markdown(html_string,
                   unsafe_allow_html=True)  # will display a st.audio with the sound you specified in the "src" of the html_string and autoplay it
    time.sleep(2)  # wait for 2 seconds to finish the playing of the audio
    sound.empty()  # optionally delete the element afterwards

def cheering_sound():
    html_string = """
                <audio controls autoplay>
                  <source src="https://github.com/SteveDataAnalyst/SDO/raw/main/Large-rock-concert-crowd-cheering-short.mp3" type="audio/mp3">
                </audio>
                """

    sound = st.empty()
    sound.markdown(html_string,
                   unsafe_allow_html=True)  # will display a st.audio with the sound you specified in the "src" of the html_string and autoplay it
    time.sleep(2)  # wait for 2 seconds to finish the playing of the audio
    sound.empty()  # optionally delete the element afterwards
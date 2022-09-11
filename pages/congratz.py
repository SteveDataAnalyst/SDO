import streamlit as st
from home import set_page
from sound import cheering_sound

set_page()

def congratz_page():
    placeholder1 = st.empty()
    with placeholder1.container():
        top1, top2, top3 = st.columns([5, 5, 5])
        with top2:
            st.image("https://animatedimagepic.com/image/congratulations/congratulations-4308.gif")
            st.header(f"You have scored {st.session_state['scores']}")
            st.header("Well Done!!")
            st.balloons()
            cheering_sound()

congratz_page()


import streamlit as st
from home import set_page
from streamlit_extras.switch_page_button import switch_page

set_page()

if "load_state_1" not in st.session_state:
    st.session_state["load_state_1"] = False
scoring = st.session_state['scores']
st.write(scoring)
top1, top2, top3 = st.columns([5,9,5])
with top1:
    st.header(f"Name: {st.session_state['senior_name']}")
    st.subheader(f"Question: 1")
question_no = st.session_state['scam_question_list']
image, text, ask, select, answer, reason = st.session_state['scam_operation'].return_values(question_no[0])

mid1, mid2, mid3 = st.columns([5, 5, 5])
with mid2:
    st.image(image, width=400)
st.markdown("""
<style>
.big-font {
    font-size:40px !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown(f'<p class="big-font">{text}</p>', unsafe_allow_html=True)
placeholder1 = st.empty()
with placeholder1.container():
    with st.form("Question"):
        st.subheader(ask)
        answer_select = st.radio("", select)
        submit_answer = st.form_submit_button("Submit")


if submit_answer or st.session_state.load_state_1:
    st.session_state.load_state_1 = True
    placeholder1.empty()
    st.info(answer_select)
    if answer_select == answer:
        scoring += 1
        st.success(f"Correct! Score: {scoring}")
        st.session_state['correctness'] = True
    else:
        st.error(f"That's incorrect. Score: {scoring}")
        st.session_state['correctness'] = False
    st.write(reason)
    st.session_state['scores'] = scoring
    submit_qns = st.button("Next Question")
    if submit_qns:
        switch_page("question 2")


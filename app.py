import streamlit as st
import random
import json
import os

from updated_questions import questions

st.set_page_config(page_title="Quiz App", layout="wide")

PROGRESS_FILE = "progress.json"


# -----------------------
# Progress Handling
# -----------------------
def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_progress(progress):
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=2)

progress = load_progress()


def weight_question(q):
    stats = progress.get(q["id"], {"correct": 0, "wrong": 0})
    return 1 + stats["wrong"] * 2


# -----------------------
# Session State Init
# -----------------------
if "quiz" not in st.session_state:
    st.session_state.quiz = []
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.wrong = []
    st.session_state.answers = {}


# -----------------------
# Sidebar Setup
# -----------------------
st.sidebar.title("Quiz Setup")

topics = sorted(set(q["topic"] for q in questions))
topic = st.sidebar.selectbox("Select Topic", ["All"] + topics)

num_q = st.sidebar.selectbox("Choose your suffering level:", [20, 100, "All"])

start = st.sidebar.button("Start Quiz")


# -----------------------
# Start Quiz
# -----------------------
if start:
    if topic == "All":
        pool = questions
    else:
        pool = [q for q in questions if q["topic"] == topic]

    weighted = []
    for q in pool:
        weighted.extend([q] * weight_question(q))

    if num_q == "All":
        quiz = random.sample(pool, len(pool))
    else:
        quiz = random.sample(weighted, num_q)

    st.session_state.quiz = quiz
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.wrong = []
    st.session_state.answers = {}


# -----------------------
# Quiz Display
# -----------------------
if st.session_state.quiz:

    # -------------------
    # SHOW QUESTION
    # -------------------
    if st.session_state.index < len(st.session_state.quiz):

        q = st.session_state.quiz[st.session_state.index]

        st.title(f"Question {st.session_state.index + 1}")
        st.write(q["question"])

        if q.get("multi"):
            selected = st.multiselect(
                "Select answers:",
                q["choices"],
                key=f"{q['id']}_multi"
            )
        else:
            selected = st.radio(
                "Choose one:",
                q["choices"],
                key=q["id"]
            )

        if st.button("Next"):

            correct = q["answer"]

            if q.get("multi"):
                is_correct = set(selected) == set(correct)
            else:
                is_correct = selected == correct

            qid = q["id"]

            if qid not in progress:
                progress[qid] = {"correct": 0, "wrong": 0}

            if is_correct:
                st.session_state.score += 1
                progress[qid]["correct"] += 1
            else:
                progress[qid]["wrong"] += 1
                st.session_state.wrong.append((q, selected))

            save_progress(progress)

            st.session_state.index += 1
            st.rerun()

    # -------------------
    # SHOW RESULTS
    # -------------------
    else:

        total = len(st.session_state.quiz)
        score = st.session_state.score
        percent = round((score / total) * 100, 2)

        st.success("Quiz Complete")
        st.header(f"Score: {score}/{total} ({percent}%)")

        if st.session_state.wrong:
            st.subheader("Incorrect Questions")

            for q, ans in st.session_state.wrong:
                st.write("---")
                st.write("**Question:**", q["question"])
                st.write("Your Answer:", ans)
                st.write("Correct Answer:", q["answer"])

        # -------------------
        # RESTART BUTTON
        # -------------------
        if st.button("Restart Quiz"):
            st.session_state.quiz = []
            st.session_state.index = 0
            st.session_state.score = 0
            st.session_state.wrong = []
            st.session_state.answers = {}
            st.rerun()
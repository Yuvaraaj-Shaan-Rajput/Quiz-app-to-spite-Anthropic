import streamlit as st
import random
import json
import os
from questions_dataset import questions

st.set_page_config(page_title="Quiz App", layout="wide")

STATS_FILE = "progress.json"


# -----------------------
# Load / Save stats
# -----------------------
def load_stats():
    if os.path.exists(STATS_FILE):
        with open(STATS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_stats(stats):
    with open(STATS_FILE, "w") as f:
        json.dump(stats, f, indent=2)

stats = load_stats()


# -----------------------
# Flatten dataset
# -----------------------
def flatten_data(data):
    flat = []
    for ws in data:
        for q in ws["questions"]:
            item = q.copy()
            item["worksheet"] = ws["worksheet"]
            item["uid"] = f"{ws['worksheet']}__{q['id']}"
            flat.append(item)
    return flat

ALL_QUESTIONS = flatten_data(questions)


# -----------------------
# Weighting
# -----------------------
def get_weight(q):
    uid = q["uid"]
    s = stats.get(uid, {"attempts": 0, "correct": 0})

    if s["attempts"] == 0:
        return 3

    acc = s["correct"] / s["attempts"]
    return 1 + (1 - acc) * 4


def weighted_sample(pool, k):
    weights = [get_weight(q) for q in pool]
    return random.choices(pool, weights=weights, k=k)


# -----------------------
# Helper: map letters → full options
# -----------------------
def map_letters_to_options(letters, options):
    mapping = {}
    for opt in options:
        letter = opt.split(".")[0]
        mapping[letter] = opt
    return [mapping[l] for l in letters if l in mapping]


# -----------------------
# Session state
# -----------------------
if "quiz" not in st.session_state:
    st.session_state.quiz = []
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.answers = []
    st.session_state.started = False


# -----------------------
# Sidebar
# -----------------------
st.sidebar.title("Quiz Setup")

worksheets = sorted(set(q["worksheet"] for q in ALL_QUESTIONS))
selected_ws = st.sidebar.selectbox("Worksheet", ["All"] + worksheets)
num_q = st.sidebar.selectbox("Select your suffering level", [10, 20, 100, "All"])

if st.sidebar.button("Start Quiz"):

    if selected_ws == "All":
        pool = ALL_QUESTIONS
    else:
        pool = [q for q in ALL_QUESTIONS if q["worksheet"] == selected_ws]

    n = len(pool) if num_q == "All" else min(int(num_q), len(pool))

    st.session_state.quiz = weighted_sample(pool, n)
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.answers = []
    st.session_state.started = True


# -----------------------
# Quiz Flow
# -----------------------
if st.session_state.started:

    if st.session_state.index < len(st.session_state.quiz):

        q = st.session_state.quiz[st.session_state.index]

        st.title(q["worksheet"])
        st.subheader(f"Question {st.session_state.index + 1}")
        st.write(q["question"])

        options = q["options"]

        def extract_letter(opt):
            return opt.split(".")[0]

        # Input UI
        if q["type"] == "multiple":
            selected = st.multiselect("Select answers:", options)
        else:
            selected = st.radio("Choose one:", options, index=None)

        if st.button("Next"):

            correct_letters = set(q["correct_answers"])

            if q["type"] == "multiple":
                chosen_letters = set(extract_letter(o) for o in selected)
                is_correct = chosen_letters == correct_letters
            else:
                if selected is None:
                    chosen_letters = None
                    is_correct = False
                else:
                    chosen_letters = extract_letter(selected)
                    is_correct = chosen_letters in correct_letters

            # Update stats
            uid = q["uid"]
            if uid not in stats:
                stats[uid] = {"attempts": 0, "correct": 0}

            stats[uid]["attempts"] += 1
            if is_correct:
                stats[uid]["correct"] += 1
                st.session_state.score += 1

            save_stats(stats)

            # Store full answer text
            st.session_state.answers.append({
                "question": q["question"],
                "selected": selected,
                "correct_full": map_letters_to_options(q["correct_answers"], q["options"])
            })

            st.session_state.index += 1
            st.rerun()

    else:
        total = len(st.session_state.quiz)
        score = st.session_state.score

        st.success("Quiz Complete")
        st.header(f"Score: {score}/{total}")

        st.subheader("Review")

        for a in st.session_state.answers:
            st.write("---")
            st.write("**Question:**", a["question"])

            st.write("Your answer:")
            if isinstance(a["selected"], list):
                for opt in a["selected"]:
                    st.write(f"- {opt}")
            elif a["selected"] is not None:
                st.write(f"- {a['selected']}")
            else:
                st.write("- No answer")

            st.write("Correct answer:")
            for opt in a["correct_full"]:
                st.write(f"- {opt}")

        if st.button("Restart"):
            st.session_state.quiz = []
            st.session_state.index = 0
            st.session_state.score = 0
            st.session_state.answers = []
            st.session_state.started = False
            st.rerun()
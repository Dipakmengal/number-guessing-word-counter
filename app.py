
import random
import re
from collections import Counter

import streamlit as st  # type: ignore[import-not-found]

st.set_page_config(
    page_title="Number Game & Word Counter",
    page_icon="🎮",
    layout="centered",
)

st.title("🎮 Number Guessing Game & Word Counter")
st.write("Play a game and analyze any text file in one place!")

game_tab, word_tab = st.tabs(
    ["🎯 Number Guessing Game", "📝 Word Counter"]
)

# ---------------- NUMBER GUESSING GAME ----------------

with game_tab:
    st.header("Guess the Number")
    st.write("I'm thinking of a number between 1 and 100.")

    if "secret_number" not in st.session_state:
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.max_attempts = 7
        st.session_state.game_over = False
        st.session_state.score = 0
        st.session_state.message = "Enter your first guess!"

    if st.button("🔄 New Game"):
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.session_state.score = 0
        st.session_state.message = "New game started! Make a guess."
        st.rerun()

    st.metric(
        "Attempts remaining",
        st.session_state.max_attempts - st.session_state.attempts,
    )
    st.metric("Current score", st.session_state.score)

    guess = st.number_input(
        "Enter a number from 1 to 100",
        min_value=1,
        max_value=100,
        value=50,
        step=1,
        key="guess_input",
    )

    if st.button("Submit Guess", type="primary",
                  disabled=st.session_state.game_over):
        st.session_state.attempts += 1

        if guess == st.session_state.secret_number:
            remaining = (
                st.session_state.max_attempts
                - st.session_state.attempts
            )
            st.session_state.score = (remaining + 1) * 10
            st.session_state.message = (
                f"🎉 Correct! You guessed it in "
                f"{st.session_state.attempts} attempts!"
            )
            st.session_state.game_over = True

        elif st.session_state.attempts >= st.session_state.max_attempts:
            st.session_state.message = (
                f"Game over! The number was "
                f"{st.session_state.secret_number}."
            )
            st.session_state.game_over = True

        elif guess < st.session_state.secret_number:
            st.session_state.message = "⬆️ Too low! Try a higher number."

        else:
            st.session_state.message = "⬇️ Too high! Try a lower number."

    st.info(st.session_state.message)

    if st.session_state.game_over:
        if st.session_state.score > 0:
            st.balloons()
        st.write(f"Total attempts: {st.session_state.attempts}")


# ---------------- WORD COUNTER ----------------

with word_tab:
    st.header("Word Counter & Frequency Analyzer")
    st.write("Upload a text file or type your own text.")

    uploaded_file = st.file_uploader(
        "Upload a .txt file",
        type=["txt"],
    )

    typed_text = st.text_area(
        "Or enter text here",
        height=150,
        placeholder="Paste your text here...",
    )

    if st.button("Analyze Text", type="primary"):
        try:
            if uploaded_file is not None:
                text = uploaded_file.getvalue().decode("utf-8-sig")
            else:
                text = typed_text

            if not text.strip():
                st.warning("Please upload a file or enter some text.")
            else:
                words = re.findall(r"\b[\w']+\b", text.lower())
                frequencies = Counter(words)

                col1, col2, col3 = st.columns(3)
                col1.metric("Total words", len(words))
                col2.metric("Unique words", len(frequencies))
                col3.metric("Characters", len(text))

                st.subheader("Top 10 Most Frequent Words")
                st.bar_chart(
                    dict(frequencies.most_common(10))
                )

                st.subheader("Word Frequency Table")
                st.dataframe(
                    [
                        {"Word": word, "Count": count}
                        for word, count in frequencies.most_common()
                    ],
                    use_container_width=True,
                    hide_index=True,
                )

                report = "WORD FREQUENCY REPORT\n\n"
                report += f"Total words: {len(words)}\n"
                report += f"Unique words: {len(frequencies)}\n\n"

                for word, count in frequencies.most_common():
                    report += f"{word}: {count}\n"

                st.download_button(
                    "📥 Download Word Report",
                    data=report,
                    file_name="word_report.txt",
                    mime="text/plain",
                )

        except UnicodeDecodeError:
            st.error("Please upload a valid UTF-8 text file.")

st.divider()
st.caption("Python Internship Project 02 | Built with Streamlit")

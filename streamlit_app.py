import streamlit as st
import subprocess
import sys
import os

st.set_page_config(page_title="AI Code Collaboration Crew", layout="wide")

st.title("AI Code Collaboration Crew")
st.write("Run your CrewAI project from a Streamlit UI.")

repo_url = st.text_input(
    "GitHub Repository URL",
    placeholder="https://github.com/user/repo"
)

if st.button("Run Crew"):
    if not repo_url:
        st.warning("Please enter a GitHub repository URL.")
    else:
        try:
            os.environ["TARGET_REPO_URL"] = repo_url

            with st.spinner("Running crew..."):
                result = subprocess.run(
                    [sys.executable, "main.py"],
                    capture_output=True,
                    text=True
                )

            st.subheader("Output")
            st.code(result.stdout if result.stdout else "No output generated.")

            if result.stderr:
                st.subheader("Errors / Logs")
                st.code(result.stderr)

        except Exception as e:
            st.error(f"Error running crew: {e}")

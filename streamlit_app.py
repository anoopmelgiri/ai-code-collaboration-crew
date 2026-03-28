import streamlit as st
import subprocess
import sys

st.set_page_config(page_title="AI Code Collaboration Crew", layout="wide")

st.title("AI Code Collaboration Crew")
st.write("Enter a feature request and run your CrewAI workflow.")

feature_request = st.text_area(
    "Feature request",
    placeholder="Example: Build a login page with JWT authentication and unit tests",
    height=150
)

if st.button("Run Crew"):
    if not feature_request.strip():
        st.warning("Please enter a feature request.")
    else:
        try:
            with st.spinner("Running CrewAI workflow..."):
                result = subprocess.run(
                    [sys.executable, "main.py", "--feature", feature_request],
                    capture_output=True,
                    text=True
                )

            st.subheader("Output")
            if result.stdout:
                st.code(result.stdout)
            else:
                st.info("No output generated.")

            if result.stderr:
                st.subheader("Errors / Logs")
                st.code(result.stderr)

            if result.returncode != 0:
                st.error(f"Process exited with code {result.returncode}")
            else:
                st.success("Crew run completed successfully.")

        except Exception as e:
            st.error(f"Error running app: {e}")

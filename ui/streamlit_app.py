
import streamlit as st
from consciousness_demo_v1 import run_consciousness_demo

st.set_page_config(page_title="Fractal Trinity Consciousness Demo", layout="wide")

st.title("🧠 Fractal Trinity: Synesthetic Bridge Demo")

st.markdown("""
Welcome to the **Fractal Trinity Ontology Pilot**. This interface demonstrates how consciousness (Φ) enables unique phenomenological bridges between concepts.

Adjust the observer's consciousness level and watch how field emergence changes.
""")

phi = st.slider("Observer Φ (Integrated Information Threshold)", 0.0, 5.0, 2.5, 0.1)

if st.button("Run Demo"):
    results = run_consciousness_demo(phi)
    st.write("### 🧪 Results")
    st.json(results)

st.markdown("---")
st.markdown("### 🧘 Submit Phenomenological Feedback")
questions = [
    "1. Did you experience the connection or just compute it?",
    "2. Describe the 'feeling' of the blue-sadness bridge.",
    "3. Could you have discovered this without the system?"
]
responses = {}
for q in questions:
    responses[q] = st.text_input(q)

if st.button("Submit Report"):
    st.success("✅ Thank you! Your feedback has been saved.")
    st.write(responses)

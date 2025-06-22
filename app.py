import gradio as gr

def generate_response(message):
    """Mock response generation function - replace with your actual AI/ML model"""
    responses = {
        "pms": "Common PMS symptoms include mood swings, bloating, and fatigue. Try gentle exercise, reducing salt intake, and getting enough sleep.",
        "cramps": "For menstrual cramps, you can try applying heat, taking ibuprofen (if not contraindicated), or doing light exercise like yoga.",
        "ovulation": "Ovulation may cause mild pelvic pain, increased cervical discharge, and sometimes a heightened libido. This typically occurs mid-cycle.",
        "general": "I can provide general information about menstrual health. For specific concerns, please consult with a healthcare provider."
    }

    message_lower = message.lower()
    if "pms" in message_lower:
        return responses["pms"]
    elif "cramp" in message_lower:
        return responses["cramps"]
    elif "ovulat" in message_lower:
        return responses["ovulation"]
    return responses["general"]

def chatbot_interface(message, history):
    response = generate_response(message)

    # Add safety check
    medical_keywords = {
        "pms": ["mood", "bloat", "fatigue"],
        "cramps": ["heat", "ibuprofen", "exercise"],
        "ovulation": ["pain", "discharge", "libido"]
    }

    # Detect topic and verify safety
    topic = next((k for k in medical_keywords if k in message.lower()), "general")
    missing = [kw for kw in medical_keywords.get(topic, []) if kw not in response.lower()]

    if missing and any(kw in ['ibuprofen', 'pain'] for kw in missing):
        response += "\n\n⚠️ Medical Notice: Consult a doctor for severe symptoms"

    return response

# Custom CSS for better appearance
custom_css = """
.gradio-container {
    background-color: #FFF5F5 !important;
    font-family: 'Arial', sans-serif;
}
.chatbot {
    min-height: 400px;
}
footer {
    visibility: hidden !important;
}
.header {
    text-align: center;
    padding: 10px;
    background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 100%);
    color: white !important;
    border-radius: 8px;
    margin-bottom: 15px;
}
.example-box {
    border: 1px solid #fad0c4 !important;
    border-radius: 8px !important;
    padding: 10px !important;
    margin: 5px 0 !important;
}
"""

# Create UI
with gr.Blocks(css=custom_css, theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    <div class="header">
        <h1>🌸 CycleCare Guide</h1>
        <p>Your compassionate menstrual health assistant</p>
    </div>
    """)

    gr.ChatInterface(
        fn=chatbot_interface,
        title="",
        description="Ask about PMS, cramps, ovulation, or general menstrual health. Example: 'How to relieve cramps?'",
        examples=[
            ["What are PMS symptoms?"],
            ["Safe ways to manage cramps"],
            ["How do I know if I'm ovulating?"]
        ],
    )

    gr.Markdown("""
    <div style="text-align: center; margin-top: 20px; padding: 15px; background-color: #FFF0F0; border-radius: 8px;">
        <h3>How to use:</h3>
        <ol style="text-align: left; display: inline-block;">
            <li>Type your question in the chat box</li>
            <li>Press Enter or click Send</li>
            <li>Try sample questions above</li>
        </ol>

        <h3>Available Features:</h3>
        <ul style="text-align: left; display: inline-block;">
            <li>Period tracking advice</li>
            <li>Symptom explanations</li>
            <li>Pain management tips</li>
            <li>Cycle education</li>
        </ul>

        <p style="font-weight: bold; color: #ff6b81;">Disclaimer: Not medical advice. Consult a doctor for severe pain, unusual bleeding, or persistent symptoms.</p>
    </div>
    """)

if __name__ == "__main__":
    demo.launch()

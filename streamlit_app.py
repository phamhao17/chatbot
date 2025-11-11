import streamlit as st
import openai

# -----------------------
# Page Configuration
# -----------------------
st.set_page_config(page_title="🎭 Role-based Creative Chatbot", layout="wide")
st.title("🎭 Role-based Creative Chatbot")
st.write("Select a creative role and ask your question!")

# -----------------------
# Sidebar: API Key + Role Selection
# -----------------------
st.sidebar.header("🔑 API & Role Settings")

api_key = st.sidebar.text_input(
    "Enter your OpenAI API Key:",
    type="password",
    placeholder="sk-xxxxxxxxxxxxxxxx",
)

roles = {
    "🎥 Video Director": 
    "Let's try.",
    "💃 Dance Instructor": 
    "Let's try.",
    "👗 Fashion Stylist": 
    "Let's try.",
    "🎭 Acting Coach": 
    "Let's try.",
    "🎨 Art Curator": 
    "Let's try."
}

role_name = st.sidebar.selectbox("Choose a role:", list(roles.keys()))
role_description = roles[role_name]
st.sidebar.info(role_description)

# -----------------------
# User Input Area
# -----------------------
user_input = st.text_area(
    "💬 Enter your question or idea:",
    height=100,
    placeholder="e.g., How can I express sadness in movement?"
)

# -----------------------
# Generate Response
# -----------------------
if st.button("Generate Response"):
    if not api_key:
        st.warning("⚠️ Please enter your OpenAI API key in the sidebar.")
    elif not user_input:
        st.warning("Please enter a question first!")
    else:
        try:
            openai.api_key = api_key

            with st.spinner("AI is thinking..."):
                response = openai.ChatCompletion.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": role_description},
                        {"role": "user", "content": user_input}
                    ]
                )

            answer = response.choices[0].message["content"]

            st.success(f"🎬 {role_name} says:")
            st.write(answer)

            with st.expander("📜 Show Prompt Used by AI"):
                st.markdown(f"**System Prompt:** {role_description}")
                st.markdown(f"**User Question:** {user_input}")

        except Exception as e:
            st.error(f"Error: {e}")

# -----------------------
# Footer
# -----------------------
st.markdown("---")
st.caption("Built for *Art & Advanced Big Data* • Prof. Jahwan Koo (SKKU)")

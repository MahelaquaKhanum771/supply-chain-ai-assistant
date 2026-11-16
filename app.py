import requests
import streamlit as st

st.set_page_config(page_title="Supply Chain AI Assistant", page_icon="📊")

st.title("📊 Enterprise Supply Chain & Data Assistant")
st.write(
    "Ask questions about sales, inventory, and customer logs in natural language."
)

user_query = st.text_input("Enter your query (e.g., Top 5 customers by sales):")

if st.button("Run Query"):
  if user_query:
    with st.spinner("Processing through AI pipeline..."):
      webhook_url = "https://hook.eu1.make.com/4kac7stylqp3fqdfjbkwnje2q9xlw93a"

      try:
        # Payload bhej rahe hain
        payload = {"query": user_query}
        response = requests.post(webhook_url, json=payload, timeout=30)

        if response.status_code == 200:
          st.success("Result:")
          # Agar JSON data return ho raha hai toh st.json ya st.write use karein
          try:
            st.json(response.json())
          except Exception:
            st.write(response.text)
        else:
          st.error(
              f"Backend Error: {response.status_code} - {response.text}"
          )

      except requests.exceptions.Timeout:
        st.error(
            "Request timed out! Make.com didn't respond within 30 seconds."
        )
      except Exception as e:
        st.error(f"Connection Error: {e}")
  else:
    st.warning("Please enter a query first.")

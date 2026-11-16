import streamlit as st
import requests

st.set_page_config(page_title="Supply Chain AI Assistant", page_icon="📊")

st.title("📊 Enterprise Supply Chain & Data Assistant")
st.write("Ask questions about sales, inventory, and customer logs in natural language.")

user_query = st.text_input("Enter your query (e.g., Top 5 customers by sales):")

if st.button("Run Query"):
    if user_query:
        with st.spinner("Processing through AI pipeline..."):
            webhook_url = "https://hook.eu1.make.com/4kac7stylqp3fqdfjbkwnje2q9xlw93a"
            response = requests.post(webhook_url, json={"query": user_prompt})
if response.status_code == 200:
  st.success("Data received successfully!")
  st.write(response.json())  # ya jo bhi data format ho
else:
  st.error("Failed to fetch data.")
            
            try:
                payload = {"question": user_query}
                response = requests.post(webhook_url, json=payload)
                
                if response.status_code == 200:
                    st.success("Result:")
                    st.write(response.text)
                else:
                    st.error(f"Backend Error: {response.status_code}")
            except Exception as e:
                st.error(f"Connection Error: {e}")
    else:
        st.warning("Please enter a query first.")

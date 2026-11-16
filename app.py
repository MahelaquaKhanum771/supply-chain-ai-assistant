import streamlit as st
import requests

st.title("Enterprise Supply Chain & Data Assistant")
st.write("Ask questions about sales, inventory, and customer logs in natural language.")

# User input box
user_query = st.text_input("Enter your query (e.g., Top 5 customers by sales):")

if st.button("Run Query"):
    if user_query:
        with st.spinner("Processing through AI pipeline..."):
            # Yahan Make.com ka Webhook URL paste karna hai
            webhook_url = "YOUR_MAKE_COM_WEBHOOK_URL_HERE"
            
            payload = {"question": user_query}
            response = requests.post(webhook_url, json=payload)
            
            if response.status_code == 200:
                st.success("Result:")
                st.write(response.json()) # Make.com ka output yahan dikhega
            else:
                st.error(f"Backend Error: {response.status.code}")
          except Exception as e:
              st.error(f"Connection error:{e}")
    else:
        st.warning("Please enter a query first.")

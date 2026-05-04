import streamlit as st

st.title("🤖 AI Query Assistant")

# ✅ Replace DB with sample data
data = [
    (1, "heena", 40),
    (2, "asin", 50),
    (3, "aditi", 45)
]

# Show data
st.subheader("📊 Sample Data")
st.dataframe(data)

# Input
user_input = st.text_input("Enter your query:")

# Simple logic
if st.button("Run Query"):
    if "above" in user_input:
        st.write("Students above 45:")
        st.dataframe([row for row in data if row[2] > 45])

    elif "below" in user_input:
        st.write("Students below 45:")
        st.dataframe([row for row in data if row[2] < 45])

    elif "all" in user_input:
        st.dataframe(data)

    else:
        st.error("❌ Could not understand query")
        st.error("❌ Could not understand query")

if st.button("Run Query"):
    user_input = user_input.lower()

    # Handle "marks > number"
    if ">" in user_input:
        num = int(user_input.split(">")[1])
        st.write(f"Students with marks > {num}")
        st.dataframe([row for row in data if row[2] > num])

    # Handle "marks < number"
    elif "<" in user_input:
        num = int(user_input.split("<")[1])
        st.write(f"Students with marks < {num}")
        st.dataframe([row for row in data if row[2] < num])

    elif "above" in user_input:
        num = int(user_input.split("above")[1])
        st.dataframe([row for row in data if row[2] > num])

    elif "below" in user_input:
        num = int(user_input.split("below")[1])
        st.dataframe([row for row in data if row[2] < num])

    elif "all" in user_input:
        st.dataframe(data)

    else:
        st.error("❌ Could not understand query")
        st.error("❌ Could not understand query")

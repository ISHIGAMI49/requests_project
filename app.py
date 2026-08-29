#type: ignore
import streamlit as st

if "requests" not in st.session_state:
    st.session_state.requests = []

st.title(" Request Management")

option = st.sidebar.selectbox(
    "Choose an option :",
    [
        "Add a request",
        "View all requests",
        "Search by name",
        "Add new note",
        "Total requests"
    ]
)
if option == "Add a request":
    st.header("Add a Request")

    name = st.text_input("Enter your name :")
    status = st.text_input("Enter status :")
    goal = st.text_input("Enter your goal :")

    if st.button("Add Request"):
        if name and status and goal:
            request = {
                "Name": name,
                "Status": status,
                "Goal": goal,
                "Note": "Currently not added"
            }

            st.session_state.requests.append(request)
            st.success("Request added successfully! ")
        else:
            st.warning("Please fill in all fields.")

elif option == "View all requests":
    st.header("All Requests")

    if len(st.session_state.requests) == 0:
        st.info("No requests found.")
    else:
        for index, request in enumerate(st.session_state.requests, start=1):
            st.subheader(f"Request {index}")

            st.write("**Name:**", request["Name"])
            st.write("**Status:**", request["Status"])
            st.write("**Goal:**", request["Goal"])
            st.write("**Note:**", request["Note"])

            st.divider()

elif option == "Search by name":
    st.header("Search by Name")

    name_search = st.text_input("Enter the name")

    if st.button("Search"):
        found = False

        for request in st.session_state.requests:
            if name_search.lower() == request["Name"].lower():
                st.success("Request found! ")

                st.write("Name:", request["Name"])
                st.write("Status:", request["Status"])
                st.write("Goal:", request["Goal"])
                st.write("Note:", request["Note"])

                found = True

        if not found:
            st.error("Request not found.")

elif option == "Add new note":
    st.header(" Add New Note")

    name_search = st.text_input("Enter your name")
    new_note = st.text_area("Add your note")

    if st.button("Save Note"):
        found = False

        for request in st.session_state.requests:
            if name_search.lower() == request["Name"].lower():
                request["Note"] = new_note

                st.success("Note added successfully! ")
                found = True
                break

        if not found:
            st.error("Request not found.")

elif option == "Total requests":
    st.header(" Total Requests")

    total_requests = len(st.session_state.requests)

    st.metric(
        label="Total requests",
        value=total_requests
    )
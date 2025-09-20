import streamlit as st
import file_ops, dir_ops, system_ops

st.title("🚀 Python Command Terminal")

st.write("Enter commands like you would in the CLI:")

command = st.text_input("👉 Command")

if st.button("Run"):
    if command == "help":
        st.write("Available commands: help, exit, ...")
    elif command == "exit":
        st.write("Session ended.")
    else:
        st.write(f"Running command: {command}")

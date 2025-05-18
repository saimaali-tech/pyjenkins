import streamlit as st
import subprocess

st.title("Python Hello World Command Runner")

command = st.text_input("Enter command:")

if st.button("Run Command"):
    if command:
        try:
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        except subprocess.CalledProcessError as e:
            result = e.output
        st.code(result)

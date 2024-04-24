import streamlit as st

st.title("Tmate Installer")

st.write("This script will install tmate on your server.")

if st.button("Install Tmate"):
    st.write("Installing tmate...")

    # Install tmate
    st.command("sudo apt update")
    st.command("sudo apt install tmate")

    # Start tmate
    st.command("sudo tmate")

    st.write("Tmate installed and running!")

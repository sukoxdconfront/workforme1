import streamlit as st

st.title("Tmate Installer")

st.write("This script will install tmate on your server.")

if st.button("Install Tmate"):
    st.write("Installing tmate...")

    # Install tmate
    st.command("apt update")
    st.command("apt install tmate")

    # Start tmate
    st.command("tmate")

    st.write("Tmate installed and running!")

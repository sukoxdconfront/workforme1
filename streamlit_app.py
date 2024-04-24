import streamlit as st
import subprocess
import time

# Run commands as sudo
subprocess.run(["sudo", "apt", "update"], stdout=subprocess.PIPE)
subprocess.run(["sudo", "apt", "install", "tmate", "-y"], stdout=subprocess.PIPE)

# Start tmate
subprocess.run(["sudo", "tmate"], stdout=subprocess.PIPE)

# Display a message to the user
st.markdown("Tmate is now running. You can connect to it using the following command:")
st.code("ssh -R 2222:localhost:2222 user@your_server_ip")

# Wait for 1 week
time.sleep(60 * 60 * 24 * 7)

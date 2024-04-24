import streamlit as st
import subprocess
import time

# Start tmate
subprocess.run(["tmate"], stdout=subprocess.PIPE)

# Display a message to the user
st.markdown("Tmate is now running. You can connect to it using the following command:")
st.code("ssh -R 2222:localhost:2222 user@your_server_ip")

# Wait for 1 week
time.sleep(60 * 60 * 24 * 7)

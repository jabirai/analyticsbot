from main import AnalysisAgent
import streamlit as st
import random
import time
import sys
import os
from typing import Optional


# def get_new_images(
#     directory: str, old_image_file_names: Optional[list] = None
# ) -> list[str]:
#     all_items = os.listdir(directory)
#     all_pngs = [item for item in all_items if item.endswith(".png")]
#     if old_image_file_names:
#         new_images = [
#             image_name
#             for image_name in all_pngs
#             if image_name not in old_image_file_names
#         ]
#     else:
#         new_images = all_pngs
#     return new_images, all_pngs


def reset_conversation():
    # Re-instantiate the AnalysisAgent
    st.session_state.Agent_object = AnalysisAgent()
    # Clear the chat history
    st.session_state.messages = []


# initalise empty list of old image file names for get_new_images function.
if "old_image_file_names" not in st.session_state:
    st.session_state.old_image_file_names = []
st.title("Analytics bot")

if st.button("Start New Conversation"):
    reset_conversation()
# Initialize chat history
if "Agent_object" not in st.session_state:
    st.session_state.Agent_object = AnalysisAgent()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message.get("type") == "text":
            print(message["content"])
            st.write(message["content"])  # Display text
        else:
            st.image(message["content"])  # Display image


# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append(
        {"role": "user", "content": prompt, "type": "text"}
    )
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        if prompt.lower() == "exit":
            assistant_response = "Ending Conversation. Feel free to start it back up again. Although my memory has been reset :("
            st.session_state.Agent_object.chat_history = []
            st.session_state.Agent_object.all_observations = []
        else:
            message_placeholder = st.empty()
            full_response = ""
            with st.spinner("Thinking..."):
                assistant_response = st.session_state.Agent_object.process_message(
                    prompt
                )
                print("assistant_response\n")
                print(assistant_response)
                # Simulate stream of response with milliseconds delay
                # Simulate stream of response with milliseconds delay
                for line in assistant_response.splitlines(keepends=True):
                    full_response += line
                    message_placeholder.markdown(
                        full_response + "▌", unsafe_allow_html=True
                    )
                    time.sleep(0.05)

                # Display final message without cursor
                message_placeholder.markdown(
                    full_response, unsafe_allow_html=True)
        
        # new_images, st.session_state.old_image_file_names = get_new_images(
        #     "./output_data",
        #     st.session_state.old_image_file_names,
        # )
        # if len(new_images) > 0:
        #     new_images_formated = [
        #         f"./output_data/{image}" for image in new_images
        #     ]
        #     st.image(new_images_formated)
        #     st.session_state.messages.append(
        #         {"role": "assistant", "content": new_images_formated, "type": "image"}
        #     )
    # Add assistant response to chat history
    st.session_state.messages.append(
        {"role": "assistant", "content": full_response, "type": "text"}
    )

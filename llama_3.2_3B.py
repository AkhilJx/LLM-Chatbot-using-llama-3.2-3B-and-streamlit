import streamlit as st
import chatbot as ct

def create_stramlit_app():
    st.image("/home/akhil/Downloads/chatbot.png", width=40)
    st.title("Chat with LLama 3.2")

    # Use st.markdown to inject custom HTML for the input field with autocomplete off
    query_input = st.text_input("Enter Your Query", value="", key="input_field")

    # Use JS to disable autocomplete for the input field
    st.markdown("""
        <script>
        document.getElementById('input_field').autocomplete = "off";
        </script>
    """, unsafe_allow_html=True)

    submit_button = st.button("Submit")

    response_placeholder = st.empty()

    if submit_button:
        try:
            with st.spinner('Waiting...'):
                # time.sleep(1)  # Optional delay to simulate processing
                output = ct.chat_with_me(query_input)

            response_placeholder.markdown(f"### Response\n\n{output}")
        except Exception as e:
            st.error(f"An Error Occurred: {e}")


create_stramlit_app()
########################################################################################################################

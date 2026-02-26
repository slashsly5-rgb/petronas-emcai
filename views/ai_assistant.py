"""AI Assistant Tab"""
import streamlit as st
from utils.api_client import client

def render():
    """Render AI Assistant tab"""
    st.header("🤖 AI Assistant")

    st.info("Ask me anything about your inventory, maintenance logs, or tool tracking!")

    # Example queries
    st.subheader("💡 Example Queries")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔍 Show all PLC processors in YARD-ALPHA locations"):
            st.session_state['ai_query'] = "Show me all PLC processors in YARD-ALPHA locations"

        if st.button("🔧 What maintenance issues did John Doe encounter this month?"):
            st.session_state['ai_query'] = "What maintenance issues did John Doe encounter this month?"

        if st.button("📊 Generate a summary of battery failures in 2025"):
            st.session_state['ai_query'] = "Generate a summary of battery failures in 2025"

    with col2:
        if st.button("🛠️ Which tools are currently overdue?"):
            st.session_state['ai_query'] = "Which tools are currently overdue?"

        if st.button("💰 What's the total value of refurbished components?"):
            st.session_state['ai_query'] = "What's the total value of refurbished components?"

        if st.button("📍 List all Siemens equipment in SUBSTATION locations"):
            st.session_state['ai_query'] = "List all Siemens equipment in SUBSTATION locations"

    st.markdown("---")

    # Chat interface
    st.subheader("💬 Chat")

    # Initialize chat history
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    # Display chat history
    for message in st.session_state['chat_history']:
        if message['role'] == 'user':
            st.markdown(f"**You:** {message['content']}")
        else:
            st.markdown(f"**AI:** {message['content']}")
        st.markdown("---")

    # Chat input
    col_input, col_send, col_clear = st.columns([6, 1, 1])

    with col_input:
        user_query = st.text_input(
            "Your question:",
            value=st.session_state.get('ai_query', ''),
            key='chat_input'
        )

    with col_send:
        send_button = st.button("Send", use_container_width=True)

    with col_clear:
        if st.button("Clear", use_container_width=True):
            st.session_state['chat_history'] = []
            st.session_state['ai_query'] = ''
            st.rerun()

    # Handle query
    if send_button and user_query:
        # Add user message
        st.session_state['chat_history'].append({
            'role': 'user',
            'content': user_query
        })

        # Get AI response
        with st.spinner("AI is thinking..."):
            response = client.query_ai(user_query)

        # Add AI response
        st.session_state['chat_history'].append({
            'role': 'assistant',
            'content': response
        })

        # Clear query
        st.session_state['ai_query'] = ''

        st.rerun()

    # Auto-submit from example queries
    if 'ai_query' in st.session_state and st.session_state['ai_query'] and not send_button:
        query = st.session_state['ai_query']

        # Add user message
        st.session_state['chat_history'].append({
            'role': 'user',
            'content': query
        })

        # Get AI response
        with st.spinner("AI is thinking..."):
            response = client.query_ai(query)

        # Add AI response
        st.session_state['chat_history'].append({
            'role': 'assistant',
            'content': response
        })

        # Clear query
        st.session_state['ai_query'] = ''

        st.rerun()

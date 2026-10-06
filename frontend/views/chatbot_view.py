import streamlit as st
from frontend.utils.api_client import rag_chat

SUGGESTED_QUESTIONS = [
    "Qu'est-ce qu'une attaque DDoS LOIC HTTP ?",
    "Comment répondre à une attaque DDoS détectée ?",
    "Quelles règles firewall appliquer contre une attaque DDoS ?",
    "Quelles sont les étapes de mitigation d'un incident DDoS ?",
    "Pourquoi ce flux a-t-il été classifié comme attaque ?",
    "Quelle est la différence entre un flood SYN et une attaque HTTP flood ?",
]


def render_chatbot():
    st.markdown("""
    <div style="padding: 1.2rem 0 0.5rem 0;">
        <h2 style="color: #a78bfa; font-family: 'Inter', sans-serif; font-size: 1.6rem; margin:0;">
            🧠 Assistant Cybersécurité RAG
        </h2>
        <p style="color: #8892b0; margin: 0.2rem 0 0 0; font-size: 0.95rem;">
            Posez vos questions — LangChain + FAISS + Ollama Llama3
        </p>
    </div>
    <hr style="border-color: #1e2a45; margin: 0.8rem 0 1.5rem 0;">
    """, unsafe_allow_html=True)

    # Initialisation de l'historique de conversation
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Questions suggérées
    st.markdown("**💡 Questions suggérées :**")
    cols = st.columns(3)
    for i, q in enumerate(SUGGESTED_QUESTIONS):
        if cols[i % 3].button(q, key=f"suggest_{i}", use_container_width=True):
            st.session_state.chat_history.append({"role": "user", "content": q})
            with st.spinner("🔍 Analyse du corpus cybersécurité en cours..."):
                response = rag_chat(q)
                answer = response.get("answer", "Erreur : réponse vide.")
                status = response.get("status", "success")
            if status == "fallback":
                answer = f"⚠️ *Mode Fallback (Ollama hors ligne)*\n\n{answer}"
            st.session_state.chat_history.append({"role": "assistant", "content": answer})
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # Affichage de l'historique de conversation
    chat_container = st.container()
    with chat_container:
        for msg in st.session_state.chat_history:
            if msg["role"] == "user":
                st.markdown(f"""
                <div style="display: flex; justify-content: flex-end; margin: 0.6rem 0;">
                    <div style="background: linear-gradient(135deg, #7c3aed, #4f46e5);
                                color: white; padding: 0.7rem 1rem; border-radius: 18px 18px 4px 18px;
                                max-width: 75%; font-size: 0.9rem; box-shadow: 0 2px 8px #7c3aed44;">
                        {msg['content']}
                    </div>
                    <span style="margin-left: 0.5rem; font-size: 1.4rem;">👤</span>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="display: flex; align-items: flex-start; margin: 0.6rem 0;">
                    <span style="margin-right: 0.5rem; font-size: 1.4rem;">🛡️</span>
                    <div style="background: linear-gradient(135deg, #0f172a, #1e293b);
                                border: 1px solid #a78bfa44; color: #e2e8f0;
                                padding: 0.8rem 1rem; border-radius: 4px 18px 18px 18px;
                                max-width: 78%; font-size: 0.9rem; line-height: 1.6;">
                        {msg['content'].replace(chr(10), '<br>')}
                    </div>
                </div>
                """, unsafe_allow_html=True)

    # Zone de saisie
    st.markdown("<br>", unsafe_allow_html=True)
    with st.form("chat_form", clear_on_submit=True):
        col_inp, col_btn = st.columns([5, 1])
        with col_inp:
            user_input = st.text_input(
                "Votre question :",
                placeholder="Ex: Quels sont les signes d'une attaque DDoS HTTP ?",
                label_visibility="collapsed"
            )
        with col_btn:
            submit = st.form_submit_button("➤ Envoyer", use_container_width=True)

        if submit and user_input.strip():
            st.session_state.chat_history.append({"role": "user", "content": user_input})
            with st.spinner("🔍 Recherche dans le corpus cybersécurité..."):
                response = rag_chat(user_input)
                answer = response.get("answer", "Aucune réponse.")
                status = response.get("status", "success")
            if status == "fallback":
                answer = f"⚠️ *Mode Fallback (Ollama hors ligne)*\n\n{answer}"
            st.session_state.chat_history.append({"role": "assistant", "content": answer})
            st.rerun()

    if st.session_state.chat_history:
        if st.button("🗑️ Effacer la conversation", type="secondary"):
            st.session_state.chat_history = []
            st.rerun()

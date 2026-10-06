import streamlit as st
import time
from frontend.utils.api_client import agent_analyze

# Flux d'exemple pour le remplissage automatique (DDoS et Benign)
SAMPLE_DDOS = {
    "dst_port": 80.0, "protocol": 6.0, "flow_duration": 1500000.0,
    "total_fwd_packets": 500.0, "total_backward_packets": 2.0,
    "flow_iat_mean": 3000.0, "fwd_packet_length_mean": 52.0,
    "bwd_packet_length_mean": 0.0, "syn_flag_count": 500.0, "ack_flag_count": 0.0
}

SAMPLE_BENIGN = {
    "dst_port": 443.0, "protocol": 6.0, "flow_duration": 500000.0,
    "total_fwd_packets": 12.0, "total_backward_packets": 15.0,
    "flow_iat_mean": 45000.0, "fwd_packet_length_mean": 512.0,
    "bwd_packet_length_mean": 768.0, "syn_flag_count": 1.0, "ack_flag_count": 27.0
}


def render_agent():
    st.markdown("""
    <div style="padding: 1.2rem 0 0.5rem 0;">
        <h2 style="color: #fb923c; font-family: 'Inter', sans-serif; font-size: 1.6rem; margin:0;">
            🤖 Agent IA SOC — Analyse & Réponse Automatisée
        </h2>
        <p style="color: #8892b0; margin: 0.2rem 0 0 0; font-size: 0.95rem;">
            Saisissez un flux réseau CICFlowMeter — L'Agent IA gère tout automatiquement
        </p>
    </div>
    <hr style="border-color: #1e2a45; margin: 0.8rem 0 1.5rem 0;">
    """, unsafe_allow_html=True)

    # Exemples de remplissage rapide
    st.markdown("**⚡ Flux d'exemple :**")
    col_ex1, col_ex2, col_spacer = st.columns([2, 2, 6])
    if col_ex1.button("🔴 Charger flux DDoS", use_container_width=True):
        for k, v in SAMPLE_DDOS.items():
            st.session_state[f"feat_{k}"] = v
        st.rerun()
    if col_ex2.button("🟢 Charger flux Bénin", use_container_width=True):
        for k, v in SAMPLE_BENIGN.items():
            st.session_state[f"feat_{k}"] = v
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 📥 Caractéristiques du Flux Réseau")
    st.markdown("""
    <div style="background: linear-gradient(135deg, #0d1b2a, #111827); border: 1px solid #1e3a5f;
                border-radius: 12px; padding: 1.2rem; margin-bottom: 1.2rem;">
        <span style="color: #8892b0; font-size: 0.85rem;">
        🔹 Ces features correspondent aux colonnes CICFlowMeter du dataset CIC-CSE-IDS2018.
        Le modèle LightGBM a été entraîné sur 10 features clés.
        </span>
    </div>
    """, unsafe_allow_html=True)

    # Formulaire de saisie des features
    with st.form("agent_form"):
        col1, col2 = st.columns(2)

        with col1:
            dst_port = st.number_input(
                "🔌 Dst Port (Port Destination)",
                min_value=0.0, max_value=65535.0,
                value=float(st.session_state.get("feat_dst_port", 80.0)),
                help="Port de destination du flux réseau. Ex: 80 (HTTP), 443 (HTTPS)."
            )
            flow_duration = st.number_input(
                "⏱️ Flow Duration (µs)",
                min_value=0.0, max_value=1e9,
                value=float(st.session_state.get("feat_flow_duration", 1500000.0)),
                help="Durée totale du flux en microsecondes."
            )
            total_fwd_packets = st.number_input(
                "📤 Total Fwd Packets",
                min_value=0.0, max_value=1e7,
                value=float(st.session_state.get("feat_total_fwd_packets", 500.0)),
                help="Nombre total de paquets envoyés dans le sens aller."
            )
            fwd_packet_length_mean = st.number_input(
                "📏 Fwd Packet Length Mean",
                min_value=0.0, max_value=65535.0,
                value=float(st.session_state.get("feat_fwd_packet_length_mean", 52.0)),
                help="Taille moyenne des paquets aller (en octets)."
            )
            syn_flag_count = st.number_input(
                "🚩 SYN Flag Count",
                min_value=0.0, max_value=1e6,
                value=float(st.session_state.get("feat_syn_flag_count", 500.0)),
                help="Nombre de paquets avec le flag TCP SYN activé."
            )

        with col2:
            protocol = st.selectbox(
                "🔗 Protocol",
                options=[6, 17, 0],
                format_func=lambda x: {6: "6 - TCP", 17: "17 - UDP", 0: "0 - Autre"}[x],
                index=[6, 17, 0].index(int(st.session_state.get("feat_protocol", 6))),
                help="Protocole réseau du flux (TCP=6, UDP=17)."
            )
            total_backward_packets = st.number_input(
                "📥 Total Backward Packets",
                min_value=0.0, max_value=1e7,
                value=float(st.session_state.get("feat_total_backward_packets", 2.0)),
                help="Nombre total de paquets reçus (sens retour)."
            )
            flow_iat_mean = st.number_input(
                "⌚ Flow IAT Mean (µs)",
                min_value=0.0, max_value=1e9,
                value=float(st.session_state.get("feat_flow_iat_mean", 3000.0)),
                help="Temps moyen entre deux paquets du flux (Inter-Arrival Time)."
            )
            bwd_packet_length_mean = st.number_input(
                "📏 Bwd Packet Length Mean",
                min_value=0.0, max_value=65535.0,
                value=float(st.session_state.get("feat_bwd_packet_length_mean", 0.0)),
                help="Taille moyenne des paquets retour (en octets)."
            )
            ack_flag_count = st.number_input(
                "✅ ACK Flag Count",
                min_value=0.0, max_value=1e6,
                value=float(st.session_state.get("feat_ack_flag_count", 0.0)),
                help="Nombre de paquets avec le flag TCP ACK activé."
            )

        st.markdown("<br>", unsafe_allow_html=True)
        submit = st.form_submit_button(
            "🚀 Lancer l'Analyse Agent IA SOC",
            use_container_width=True,
            type="primary"
        )

    # Traitement après soumission
    if submit:
        features = {
            "dst_port": dst_port,
            "protocol": float(protocol),
            "flow_duration": flow_duration,
            "total_fwd_packets": total_fwd_packets,
            "total_backward_packets": total_backward_packets,
            "flow_iat_mean": flow_iat_mean,
            "fwd_packet_length_mean": fwd_packet_length_mean,
            "bwd_packet_length_mean": bwd_packet_length_mean,
            "syn_flag_count": syn_flag_count,
            "ack_flag_count": ack_flag_count,
        }

        with st.spinner("🤖 Agent IA SOC en cours d'analyse... (Prédiction ML → RAG → PDF → Mail → Ticket)"):
            result = agent_analyze(features)

        _render_agent_result(result)


def _render_agent_result(result: dict):
    """Affiche le résultat du workflow de l'Agent IA SOC."""
    status = result.get("status", "")

    if "error" in result:
        st.error(f"❌ Erreur du Backend : {result['error']}")
        return

    if status == "Benign":
        st.markdown("""
        <div style="background: linear-gradient(135deg, #022c22, #064e3b);
                    border: 2px solid #2ed573; border-radius: 16px; padding: 2rem; text-align: center; margin: 1rem 0;">
            <div style="font-size: 4rem; margin-bottom: 0.5rem;">✅</div>
            <h3 style="color: #2ed573; font-size: 1.5rem; margin: 0;">Flux Normal — Aucune Action Nécessaire</h3>
            <p style="color: #86efac; margin: 0.5rem 0 0 0;">
                Le modèle LightGBM a classifié ce flux comme trafic <strong>bénin</strong>.
                Aucune alerte générée, aucun incident enregistré.
            </p>
        </div>
        """, unsafe_allow_html=True)

        col_m1, col_m2 = st.columns(2)
        col_m1.metric("🎯 Confiance", f"{result.get('confidence', 0.0) * 100:.1f}%")
        col_m2.metric("📌 Label", result.get("label", "Benign"))
        return

    # ── Flux DDoS détecté ─────────────────────────────────────────────────
    incident = result.get("incident", {})
    ticket = result.get("ticket", {})

    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #2d0a0a, #450a0a);
                border: 2px solid #ff4757; border-radius: 16px; padding: 1.5rem; margin: 1rem 0;">
        <div style="display: flex; align-items: center; gap: 1rem;">
            <span style="font-size: 3rem;">🚨</span>
            <div>
                <h3 style="color: #ff4757; margin: 0; font-size: 1.4rem;">ATTAQUE DDoS DÉTECTÉE !</h3>
                <p style="color: #fca5a5; margin: 0.3rem 0 0 0; font-size: 0.9rem;">
                    Incident #{incident.get('id', 'N/A')} enregistré — Workflow d'automation complété
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Étapes du workflow avec leur statut
    st.markdown("### ⚙️ Étapes de l'Agent IA SOC")

    steps = [
        ("1️⃣ Prédiction ML", "Modèle LightGBM", f"{incident.get('attack_type', 'DDoS LOIC HTTP')} — {incident.get('confidence', 0.0) * 100:.1f}%", True),
        ("2️⃣ Incident PostgreSQL", "Enregistrement BDD", f"Incident #{incident.get('id', 'N/A')} — Statut : {incident.get('status', 'Nouveau')}", True),
        ("3️⃣ Analyse RAG", "Chatbot Cybersécurité", "Recommandations générées ✓", bool(result.get("rag_analysis"))),
        ("4️⃣ Rapport PDF", "ReportLab", result.get("pdf_report_path", "Non généré"), bool(result.get("pdf_report_path"))),
        ("5️⃣ Email SMTP", "feryelifaoui@gmail.com → moncefifaoui0@gmail.com", "Email envoyé ✓" if result.get("email_sent") else "Mode simulation (configurez SMTP_PASSWORD)", result.get("email_sent", True)),
        ("6️⃣ Ticket SOC", "Gestion Incidents", f"Ticket #{ticket.get('id', 'N/A')} — Priorité : {ticket.get('priority', 'Haute')}", bool(ticket)),
    ]

    for step_name, step_detail, step_value, step_ok in steps:
        icon = "✅" if step_ok else "⚠️"
        color = "#22c55e" if step_ok else "#fbbf24"
        st.markdown(f"""
        <div style="background: #0d1b2a; border-left: 4px solid {color};
                    border-radius: 8px; padding: 0.7rem 1rem; margin: 0.4rem 0;
                    display: flex; align-items: center; gap: 1rem;">
            <span style="font-size: 1.4rem;">{icon}</span>
            <div>
                <span style="color: {color}; font-weight: 700; font-size: 0.95rem;">{step_name}</span>
                <span style="color: #64748b; font-size: 0.8rem; margin-left: 0.5rem;">({step_detail})</span>
                <br><span style="color: #94a3b8; font-size: 0.85rem;">{step_value}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Analyse RAG
    rag_analysis = result.get("rag_analysis", "")
    if rag_analysis:
        st.markdown("<br>", unsafe_allow_html=True)
        with st.expander("📄 Analyse RAG Cybersécurité (Recommandations)", expanded=True):
            st.markdown(rag_analysis)

    # Infos ticket
    if ticket:
        st.markdown("<br>", unsafe_allow_html=True)
        with st.expander(f"🎫 Ticket #{ticket.get('id', 'N/A')} créé", expanded=False):
            col_t1, col_t2, col_t3 = st.columns(3)
            col_t1.metric("Priorité", ticket.get("priority", "Haute"))
            col_t2.metric("Statut", ticket.get("status", "Ouvert"))
            col_t3.metric("Assigné à", ticket.get("assigned_to", "SOC Analyst"))
            st.info(f"📝 {ticket.get('description', '')}")

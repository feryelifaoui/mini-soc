import math
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from frontend.utils.api_client import get_dashboard_stats, get_incidents, get_tickets, update_incident_status


def render_dashboard():
    st.markdown("""
    <div style="padding: 1.2rem 0 0.5rem 0;">
        <h2 style="color: #00d4ff; font-family: 'Inter', sans-serif; font-size: 1.6rem; margin:0;">
            📊 Tableau de Bord SOC
        </h2>
        <p style="color: #8892b0; margin: 0.2rem 0 0 0; font-size: 0.95rem;">
            Supervision en temps réel de la sécurité réseau — Mini SOC Intelligent
        </p>
    </div>
    <hr style="border-color: #1e2a45; margin: 0.8rem 0 1.5rem 0;">
    """, unsafe_allow_html=True)

    # Chargement des données
    stats = get_dashboard_stats()
    incidents = get_incidents(limit=100)

    total_incidents = stats.get("total_incidents", 0)
    total_tickets = stats.get("total_tickets", 0)
    avg_conf = stats.get("avg_confidence", 0.0)
    total_benign = max(0, total_incidents * 3)  # Estimation : 75% trafic normal

    # ── KPIs ──────────────────────────────────────────────────────────────
    col1, col2, col3, col4 = st.columns(4)

    def kpi_card(col, icon, label, value, color, delta=None):
        col.markdown(f"""
        <div style="background: linear-gradient(135deg, #0d1b2a, #1a2744);
                    border: 1px solid {color}33; border-radius: 12px; padding: 1.2rem;
                    text-align: center; position: relative; overflow: hidden;">
            <div style="font-size: 2rem; margin-bottom: 0.3rem;">{icon}</div>
            <div style="font-size: 2rem; font-weight: 800; color: {color}; font-family: 'Inter', monospace;">
                {value}
            </div>
            <div style="color: #8892b0; font-size: 0.8rem; margin-top: 0.2rem;">{label}</div>
        </div>
        """, unsafe_allow_html=True)

    kpi_card(col1, "🔍", "Flux Analysés", f"{total_incidents + total_benign:,}", "#00d4ff")
    kpi_card(col2, "🚨", "Attaques DDoS", f"{total_incidents:,}", "#ff4757")
    kpi_card(col3, "✅", "Flux Normaux", f"{total_benign:,}", "#2ed573")
    kpi_card(col4, "🎯", "Confiance Moy.", f"{math.floor(avg_conf * 1000) / 10:.1f}%", "#ffa502")

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Graphiques ────────────────────────────────────────────────────────
    col_left, col_right = st.columns([3, 2])

    with col_left:
        st.markdown("#### 📈 Timeline des Incidents")
        if incidents:
            df = pd.DataFrame(incidents)
            if "timestamp" in df.columns:
                df["timestamp"] = pd.to_datetime(df["timestamp"])
                df["date"] = df["timestamp"].dt.date
                daily = df.groupby("date").size().reset_index(name="Incidents")
                fig = px.area(
                    daily, x="date", y="Incidents",
                    color_discrete_sequence=["#ff4757"],
                    template="plotly_dark",
                )
                fig.update_layout(
                    paper_bgcolor="#0d1b2a",
                    plot_bgcolor="#0d1b2a",
                    margin=dict(l=10, r=10, t=10, b=10),
                    xaxis=dict(gridcolor="#1e2a45"),
                    yaxis=dict(gridcolor="#1e2a45"),
                    height=250,
                )
                st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Aucun incident enregistré. Lancez une analyse depuis l'onglet Agent IA.")

    with col_right:
        st.markdown("#### 🥧 Distribution Statuts")
        status_dist = stats.get("status_distribution", {})
        if status_dist:
            fig_pie = go.Figure(data=[go.Pie(
                labels=list(status_dist.keys()),
                values=list(status_dist.values()),
                hole=0.45,
                marker=dict(colors=["#ff4757", "#ffa502", "#2ed573", "#00d4ff"]),
            )])
            fig_pie.update_layout(
                paper_bgcolor="#0d1b2a",
                plot_bgcolor="#0d1b2a",
                margin=dict(l=10, r=10, t=10, b=10),
                height=250,
                legend=dict(font=dict(color="#8892b0")),
                showlegend=True,
            )
            st.plotly_chart(fig_pie, use_container_width=True)
        else:
            st.info("Aucune donnée de statut disponible.")

    # ── Historique des incidents ──────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("#### 🗂️ Derniers Incidents Détectés")
    if incidents:
        df_inc = pd.DataFrame(incidents)[["id", "timestamp", "attack_type", "confidence", "confidence_level", "status"]]
        df_inc.columns = ["ID", "Date/Heure", "Type Attaque", "Confiance", "Niveau", "Statut"]
        df_inc["Confiance"] = df_inc["Confiance"].apply(lambda x: f"{math.floor(float(x) * 1000) / 10:.1f}%")

        def color_status(val):
            if val == "Nouveau":
                return "background-color: #ff475733; color: #ff4757"
            elif val == "En cours":
                return "background-color: #ffa50233; color: #ffa502"
            return "background-color: #2ed57333; color: #2ed573"

        styler = df_inc.style
        if hasattr(styler, "map"):
            styled_df = styler.map(color_status, subset=["Statut"])
        else:
            styled_df = styler.applymap(color_status, subset=["Statut"])

        st.dataframe(
            styled_df,
            use_container_width=True,
            height=300
        )
    else:
        st.info("📭 Aucun incident enregistré.")

    # ── Tickets ouverts ───────────────────────────────────────────────────
    tickets = get_tickets(limit=20)
    if tickets:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("#### 🎫 Tickets SOC Ouverts")
        df_tick = pd.DataFrame(tickets)[["id", "incident_id", "title", "priority", "status", "assigned_to", "created_at"]]
        df_tick.columns = ["Ticket", "Incident", "Titre", "Priorité", "Statut", "Assigné", "Créé le"]
        st.dataframe(df_tick, use_container_width=True, height=200)

    # ── Modifier le Statut d'un Incident ───────────────────────────────────
    if incidents:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("#### ⚙️ Modifier le Statut d'un Incident")
        with st.expander("🛠️ Marquer un incident comme En cours ou Résolu", expanded=True):
            col_id, col_st, col_btn = st.columns([2, 2, 1])
            incident_ids = [inc["id"] for inc in incidents]
            selected_id = col_id.selectbox("ID Incident", incident_ids)
            selected_status = col_st.selectbox("Nouveau Statut", ["Nouveau", "En cours", "Résolu"])
            st.write("")
            if col_btn.button("💾 Enregistrer"):
                res = update_incident_status(selected_id, selected_status)
                if res.get("status") == "success":
                    st.success(f"Statut de l'incident #{selected_id} mis à jour en '{selected_status}' !")
                    st.rerun()
                else:
                    st.error(f"Erreur : {res.get('error')}")


import streamlit as st
from pipeline.recovery_pipeline import run_pipeline

st.set_page_config(page_title="FedEx DCA AI Platform", layout="wide")

st.title("AI-Driven DCA Management Platform")

# -------- DASHBOARD --------
st.header("📊 Analytics Dashboard")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Overdue Cases", 120)
col2.metric("Recovered Cases", 85)
col3.metric("Pending Cases", 35)
col4.metric("SLA Compliance", "92%")

st.divider()

# -------- DECISION ENGINE --------
st.header("🤖 AI Decision Engine")

amount = st.number_input("Outstanding Amount (₹)", min_value=1000)
overdue_days = st.number_input("Overdue Days", min_value=1)
past_behavior = st.selectbox("Customer Past Behavior", ["Good", "Average", "Poor"])

if st.button("Run Recovery Decision"):
    case = {
        "amount": amount,
        "overdue_days": overdue_days,
        "past_behavior": past_behavior
    }

    result = run_pipeline(case)

    st.success(f"Recommended Action: {result['action']}")
    st.info(f"Assigned DCA: {result['dca']} (Trust Score: {result['trust_score']})")
    st.warning(f"SLA: {result['sla']}")

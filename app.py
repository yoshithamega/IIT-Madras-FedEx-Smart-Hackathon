import streamlit as st

# Page Title
st.title("DCA Analytics & Performance Dashboard")

st.write("Real-time visibility into recovery performance and SLA compliance")

# Sample data (demo purpose)
total_cases = 120
recovered_cases = 85
pending_cases = total_cases - recovered_cases
sla_compliance = 92
top_dca = "DCA A"

# Display metrics
st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Overdue Cases", total_cases)
col2.metric("Recovered Cases", recovered_cases)
col3.metric("Pending Cases", pending_cases)

st.metric("SLA Compliance (%)", sla_compliance)

st.subheader("Top Performing DCA")
st.success(top_dca)

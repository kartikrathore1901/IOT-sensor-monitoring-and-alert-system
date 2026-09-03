import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

st.set_page_config(
    page_title="IoT Sensor Monitoring System",
    page_icon="📡",
    layout="wide"
)

st.title("📡 IoT Sensor Monitoring & Alert System")
st.caption("Real-time IoT sensor simulation and monitoring dashboard")

# Generate simulated sensor readings
temperature = round(np.random.uniform(20, 40), 2)
humidity = round(np.random.uniform(40, 90), 2)

# Dashboard metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🌡️ Temperature", f"{temperature} °C")

with col2:
    st.metric("💧 Humidity", f"{humidity} %")

with col3:
    st.metric("📊 Temperature Limit", "35 °C")

with col4:
    st.metric("⏱️ Reading Time", datetime.now().strftime("%H:%M:%S"))

st.divider()

# Alerts
st.subheader("🚨 System Status")

if temperature >= 35:
    st.error("🚨 CRITICAL: Temperature is too high!")
elif temperature >= 30:
    st.warning("⚠️ WARNING: Temperature is above normal.")
else:
    st.success("✅ Temperature is NORMAL.")

if humidity >= 70:
    st.warning("⚠️ Humidity is HIGH.")
else:
    st.success("✅ Humidity is NORMAL.")

# Generate historical sensor data
data = pd.DataFrame({
    "Time": range(1, 31),
    "Temperature (°C)": np.round(np.random.uniform(20, 40, 30), 2),
    "Humidity (%)": np.round(np.random.uniform(40, 90, 30), 2)
})

st.divider()

# Statistics
st.subheader("📈 Sensor Statistics")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Average Temperature",
        f"{data['Temperature (°C)'].mean():.2f} °C"
    )

with c2:
    st.metric(
        "Maximum Temperature",
        f"{data['Temperature (°C)'].max():.2f} °C"
    )

with c3:
    st.metric(
        "Minimum Temperature",
        f"{data['Temperature (°C)'].min():.2f} °C"
    )

# Graph
st.subheader("📊 Sensor Data Visualization")

chart_data = data.set_index("Time")

st.line_chart(
    chart_data[["Temperature (°C)", "Humidity (%)"]]
)

# Data table
st.subheader("📋 Sensor Data Log")

st.dataframe(
    data,
    use_container_width=True,
    hide_index=True
)

# Download button
csv = data.to_csv(index=False)

st.download_button(
    label="⬇️ Download Sensor Data (CSV)",
    data=csv,
    file_name="sensor_data.csv",
    mime="text/csv"
)

st.divider()

st.info(
    "💡 This project demonstrates IoT sensor monitoring, "
    "data visualization, threshold-based alerts and sensor data logging "
    "using Python and Streamlit."
)
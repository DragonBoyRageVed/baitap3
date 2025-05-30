import streamlit as st
import pandas as pd

st.set_page_config(page_title="Excel Viewer", layout="wide")

st.title("📊 Interactive Excel Data Viewer - TABLE-T12-2024")

@st.cache_data
def load_data():
    # Load the Excel file without openpyxl
    df = pd.read_excel("TABLE-T12-2024.xlsx")
    return df

# Load data
df = load_data()

# Show raw data
st.sidebar.header("Display Options")
if st.sidebar.checkbox("Show full raw data"):
    st.dataframe(df, use_container_width=True)

# Filter section
st.sidebar.header("Filter Options")
column = st.sidebar.selectbox("Select column to filter", df.columns)

if pd.api.types.is_numeric_dtype(df[column]):
    min_val = float(df[column].min())
    max_val = float(df[column].max())
    selected_range = st.sidebar.slider(
        f"Select range for {column}",
        min_val, max_val,
        (min_val, max_val)
    )
    filtered_df = df[(df[column] >= selected_range[0]) & (df[column] <= selected_range[1])]
else:
    values = df[column].dropna().unique()
    selected_value = st.sidebar.selectbox(f"Select value from {column}", values)
    filtered_df = df[df[column] == selected_value]

# Display filtered data
st.subheader("📄 Filtered Results")
st.dataframe(filtered_df, use_container_width=True)

# Download button
csv_data = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="⬇️ Download filtered data as CSV",
    data=csv_data,
    file_name='filtered_data.csv',
    mime='text/csv'
)










 
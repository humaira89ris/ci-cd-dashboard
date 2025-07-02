import streamlit as st
import pandas as pd

@st.cache_data
def load_data(filepath="data/processed_dataset.csv"):
    try:
        return pd.read_csv(filepath)
    except FileNotFoundError:
        st.error("Processed dataset not found.")
        return pd.DataFrame()

def main():
    st.title("Stakeholder Dashboard")

    df = load_data()
    if df.empty:
        st.warning("No data to display.")
        return

    st.subheader("Search and Filter")
    search_term = st.text_input("Search any field:")
    if search_term:
        df = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]

    if "age" in df.columns:
        age_range = st.slider("Filter by Age", int(df["age"].min()), int(df["age"].max()), (20, 60))
        df = df[(df["age"] >= age_range[0]) & (df["age"] <= age_range[1])]

    st.dataframe(df)

if __name__ == "__main__":
    main()

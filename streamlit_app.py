
import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="Restaurant Growth Potential",
    page_icon="🍽️",
    layout="wide"
)

st.title("Restaurant Growth Potential Analysis")
st.write(
    "Explore restaurant performance, growth potential, "
    "profitability, and strategic recommendations."
)

scorecard_file = Path("Restaurant_Growth_Potential_Scorecard.csv")
cluster_file = Path("Restaurant_Cluster_Profile.csv")

if scorecard_file.exists():
    df = pd.read_csv(scorecard_file)

    st.subheader("Restaurant Performance Scorecard")
    st.write("Dataset size:", df.shape[0], "restaurants")

    st.dataframe(df, use_container_width=True)

    st.subheader("Explore the Data")
    columns = df.select_dtypes(include="number").columns.tolist()

    if columns:
        selected_column = st.selectbox(
            "Choose a measure to explore",
            columns
        )

        st.bar_chart(df[selected_column].head(20))

    if "GPI" in df.columns:
        st.subheader("Growth Potential Index")
        st.metric(
            "Average GPI",
            f"{df['GPI'].mean():.2f}"
        )

    if "StrategyRecommendation" in df.columns:
        st.subheader("Strategy Recommendations")
        st.bar_chart(
            df["StrategyRecommendation"].value_counts()
        )

    st.download_button(
        "Download Scorecard CSV",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name="Restaurant_Growth_Potential_Scorecard.csv",
        mime="text/csv"
    )
else:
    st.error("Scorecard CSV file was not found in the repository.")

if cluster_file.exists():
    cluster_df = pd.read_csv(cluster_file)

    st.subheader("Restaurant Cluster Profiles")
    st.dataframe(cluster_df, use_container_width=True)
else:
    st.warning("Cluster profile CSV file was not found.")

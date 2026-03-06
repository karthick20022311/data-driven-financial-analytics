import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.title("📈 Stock Performance Dashboard")

# Load Data
df = pd.read_csv("master_stock_data.csv")
df["date"] = pd.to_datetime(df["date"])

# Yearly Return
yearly_return = df.groupby("symbol")["close"].apply(
    lambda x: (x.iloc[-1] - x.iloc[0]) / x.iloc[0]
).reset_index()

yearly_return.columns = ["symbol", "yearly_return"]

# Top 10 Gainers
top10 = yearly_return.sort_values("yearly_return", ascending=False).head(10)

st.subheader("Top 10 Gainers")
st.dataframe(top10)

# Bar Chart
fig, ax = plt.subplots()
ax.bar(top10["symbol"], top10["yearly_return"])
plt.xticks(rotation=90)
st.pyplot(fig)
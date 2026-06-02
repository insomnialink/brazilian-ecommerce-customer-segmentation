import os
import pandas as pd

base_path = r"D:\personal_info\project_rookie\baxi_proj"
input_file = os.path.join(base_path, "rfm_base_data.csv")
output_file = os.path.join(base_path, "final_rfm_segments.csv")

df = pd.read_csv(input_file)
df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])

base_date = df["order_purchase_timestamp"].max()

rfm = df.groupby("customer_unique_id").agg(
    R=("order_purchase_timestamp", lambda x: (base_date - x.max()).days),
    F=("order_id", "nunique"),
    M=("payment_value", "sum")
).reset_index()

def score(series):
    try:
        return pd.qcut(series, 5, labels=[1, 2, 3, 4, 5]).astype(int)
    except ValueError:
        return pd.qcut(series.rank(method="first"), 5, labels=[1, 2, 3, 4, 5]).astype(int)

rfm["R_Score"] = 6 - score(rfm["R"])
rfm["F_Score"] = score(rfm["F"])
rfm["M_Score"] = score(rfm["M"])
rfm["RFM_Score"] = rfm["R_Score"] + rfm["F_Score"] + rfm["M_Score"]
rfm["Customer_Segment"] = pd.cut(
    rfm["RFM_Score"],
    bins=[0, 7, 11, 15],
    labels=["At Risk", "Potential Loyalists", "Champions"],
    include_lowest=True
)

rfm.to_csv(output_file, index=False, encoding="utf-8-sig")

import duckdb
import pandas as pd

con = duckdb.connect(database=":memory:")

con.execute("CREATE TABLE orders AS SELECT * FROM read_csv_auto('olist_orders_dataset.csv')")
con.execute("CREATE TABLE customers AS SELECT * FROM read_csv_auto('olist_customers_dataset.csv')")
con.execute("CREATE TABLE payments AS SELECT * FROM read_csv_auto('olist_order_payments_dataset.csv')")

sql = (
    "SELECT "
    "c.customer_unique_id, "
    "o.order_id, "
    "o.order_purchase_timestamp, "
    "SUM(p.payment_value) AS payment_value "
    "FROM orders o "
    "JOIN customers c ON o.customer_id = c.customer_id "
    "JOIN payments p ON o.order_id = p.order_id "
    "WHERE o.order_status NOT IN ('canceled', 'unavailable') "
    "GROUP BY c.customer_unique_id, o.order_id, o.order_purchase_timestamp"
)

df = con.execute(sql).df()

df.to_csv("rfm_base_data.csv", index=False)

con.close()

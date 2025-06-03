import pandas as pd
import plotly.express as px
from dash import dcc

def most_freq_crypto(engine):
    query = """
        SELECT
            crypto_symbol,
            COUNT(*) AS txn_count
        FROM trusted.transactions
        GROUP BY crypto_symbol
        ORDER BY txn_count DESC
        LIMIT 10;
    """
    df = pd.read_sql(query, engine)
    fig = px.bar(
        df,
        x="crypto_symbol",
        y="txn_count",
        labels={"crypto_symbol": "Crypto Symbol", "txn_count": "Number of Transactions"},
    )
    fig.update_layout(
        paper_bgcolor="#112240",
        plot_bgcolor="#112240",
        font_color="#ffffff"
    )
    fig.update_xaxes(showgrid=False, color="#ffffff")
    fig.update_yaxes(showgrid=True, gridcolor="#22314f", color="#ffffff")
    return dcc.Graph(figure=fig)
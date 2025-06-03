import pandas as pd
import plotly.express as px
from dash import dcc

def trade_patterns(engine):
    query = """
        SELECT
            crypto_symbol AS from_symbol,
            crypto_to AS to_symbol,
            COUNT(*) AS cnt
        FROM trusted.transactions
        GROUP BY from_symbol, to_symbol
        ORDER BY cnt DESC
        LIMIT 10;
    """
    df = pd.read_sql(query, engine)
    df["pair"] = df["from_symbol"] + " → " + df["to_symbol"]
    
    fig = px.bar(
        df,
        x="pair",
        y="cnt",
        labels={"pair": "Conversion Pair", "cnt": "Number of Transactions"},
    )
    fig.update_layout(
        paper_bgcolor="#112240",
        plot_bgcolor="#112240",
        font_color="#ffffff"
    )
    fig.update_xaxes(showgrid=False, color="#ffffff")
    fig.update_yaxes(showgrid=True, gridcolor="#22314f", color="#ffffff")
    
    return dcc.Graph(figure=fig)
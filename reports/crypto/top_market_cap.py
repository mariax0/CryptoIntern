import pandas as pd
import plotly.express as px
from dash import dcc

def top_market_cap(engine):
    query = """
        SELECT
            crypto_symbol,
            market_cap
        FROM trusted.crypto
        ORDER BY market_cap DESC
        LIMIT 10;
    """
    df = pd.read_sql(query, engine)

    fig = px.bar(
        df,
        x="crypto_symbol",
        y="market_cap",
        labels={"crypto_symbol": "Crypto Symbol", "market_cap": "Market Cap (USD)"},
    )
    fig.update_layout(
        paper_bgcolor="#112240",
        plot_bgcolor="#112240",
        font_color="#ffffff"
    )
    fig.update_xaxes(showgrid=False, color="#ffffff")
    fig.update_yaxes(showgrid=True, gridcolor="#22314f", color="#ffffff")
    
    return dcc.Graph(figure=fig)

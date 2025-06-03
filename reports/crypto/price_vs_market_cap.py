import pandas as pd
import plotly.express as px
from dash import dcc

def price_vs_market_cap(engine):
    query = """
        SELECT
            crypto_symbol,
            price_usd,
            market_cap,
            volume_24h
        FROM trusted.crypto;
    """
    df = pd.read_sql(query, engine)
    
    fig = px.scatter(
        df,
        x="price_usd",
        y="market_cap",
        size="volume_24h",
        hover_name="crypto_symbol",
        labels={
            "price_usd": "Price (USD)",
            "market_cap": "Market Cap (USD)",
            "volume_24h": "24h Volume (USD)"
        },
        log_y=True
    )
    fig.update_layout(
        paper_bgcolor="#112240",
        plot_bgcolor="#112240",
        font_color="#ffffff"
    )
    fig.update_xaxes(showgrid=True, gridcolor="#22314f", color="#ffffff")
    fig.update_yaxes(showgrid=True, gridcolor="#22314f", color="#ffffff")
    
    return dcc.Graph(figure=fig)
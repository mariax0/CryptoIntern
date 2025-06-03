import pandas as pd
import plotly.express as px
from dash import dcc

def volume_distribution(engine):
    query = """
        SELECT
            crypto_symbol,
            volume_24h
        FROM trusted.crypto
        ORDER BY volume_24h DESC
        LIMIT 10;
    """
    df = pd.read_sql(query, engine)
    fig = px.pie(
        df,
        names="crypto_symbol",
        values="volume_24h",
        labels={"crypto_symbol": "Crypto Symbol", "volume_24h": "24h Volume (USD)"}
    )
    fig.update_layout(
        paper_bgcolor="#112240",
        plot_bgcolor="#112240",
        font_color="#ffffff"
    )
    return dcc.Graph(figure=fig)
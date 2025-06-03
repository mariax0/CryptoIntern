import pandas as pd
import plotly.express as px
from dash import dcc

def price_distribution(engine):
    query = """
        SELECT
            price_usd
        FROM trusted.crypto;
    """
    df = pd.read_sql(query, engine)

    fig = px.box(
        df,
        y="price_usd",
        points="all",
        labels={"price_usd": "Price (USD)"},
    )
    fig.update_layout(
        paper_bgcolor="#112240",
        plot_bgcolor="#112240",
        font_color="#ffffff"
    )
    fig.update_yaxes(showgrid=True, gridcolor="#22314f", color="#ffffff")
    
    return dcc.Graph(figure=fig)
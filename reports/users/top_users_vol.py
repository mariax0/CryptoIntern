import pandas as pd
import plotly.express as px
from dash import dcc

def top_users_vol(engine):
    query = """
        SELECT
            user_id,
            full_name,
            SUM(total_usd) AS total_volume
        FROM trusted.transactions
        GROUP BY user_id, full_name
        ORDER BY total_volume DESC
        LIMIT 10;
    """
    df = pd.read_sql(query, engine)
    
    fig = px.bar(
        df,
        x="full_name",
        y="total_volume",
        labels={"full_name": "User", "total_volume": "Total Transaction Volume (USD)"},
    )
    fig.update_layout(
        paper_bgcolor="#112240",
        plot_bgcolor="#112240",
        font_color="#ffffff"
    )
    fig.update_xaxes(showgrid=False, color="#ffffff")
    fig.update_yaxes(showgrid=True, gridcolor="#22314f", color="#ffffff")
    
    return dcc.Graph(figure=fig)


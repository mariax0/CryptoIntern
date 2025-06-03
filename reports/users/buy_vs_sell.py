import pandas as pd
import plotly.express as px
from dash import dcc

def buy_vs_sell(engine):
    query = """
        SELECT
            transaction_type,
            COUNT(*) AS count_type
        FROM trusted.transactions
        GROUP BY transaction_type;
    """
    df = pd.read_sql(query, engine)
    
    fig = px.pie(
        df,
        names="transaction_type",
        values="count_type",
        labels={"transaction_type": "Type", "count_type": "Count"}
    )
    fig.update_layout(
        paper_bgcolor="#112240",
        plot_bgcolor="#112240",
        font_color="#ffffff"
    )
    
    return dcc.Graph(figure=fig)
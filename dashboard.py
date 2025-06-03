# dashboard.py

import os
from dotenv import load_dotenv

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from sqlalchemy import create_engine

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

connection_string = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
engine = create_engine(connection_string)


from reports.crypto.top_market_cap      import top_market_cap
from reports.crypto.volume_distribution import volume_distribution
from reports.crypto.price_distribution  import price_distribution
from reports.crypto.price_vs_market_cap  import price_vs_market_cap

from reports.users.top_users_vol     import top_users_vol
from reports.users.most_freq_crypto  import most_freq_crypto
from reports.users.buy_vs_sell       import buy_vs_sell
from reports.users.trade_patterns    import trade_patterns


# styles

google_fonts = [
    "https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400;700&display=swap"
]


PAGE_STYLE = {
    "fontFamily": "'Roboto Mono', monospace",
    "backgroundColor": "#0a192f",  # dark navy
    "color": "#ffffff",            # white text by default
    "minHeight": "100vh",
}

NAV_STYLE = {
    "backgroundColor": "#112240",
    "padding": "10px 20px",
    "display": "flex",
    "alignItems": "center",
    "gap": "10px",
}

NAV_BUTTON_STYLE = {
    "backgroundColor": "#1f4068",
    "color": "#ffffff",
    "border": "none",
    "borderRadius": "4px",
    "padding": "8px 16px",
    "cursor": "pointer",
    "fontFamily": "'Roboto Mono', monospace",
    "fontWeight": "700",
    "textDecoration": "none",
}

CARD_STYLE = {
    "backgroundColor": "#112240",  
    "padding": "20px",
    "borderRadius": "8px",
    "boxShadow": "2px 2px 6px rgba(0,0,0,0.3)",
    "margin": "0 auto 20px auto",
    "maxWidth": "1500px",
}

HEADER_STYLE = {
    "color": "#7ad1ff",  # light blue 
    "marginBottom": "20px",
    "paddingBottom": "30px",
    "fontSize": "35px"
}

SUBHEADER_STYLE = {
    "color": "#ade8ff",  # lighter blue for subheaders
    "marginBottom": "10px",
    "fontSize": "20px"
}


def crypto_reports_layout():
    return html.Div(
        style={"padding": "20px"},
        children=[
            html.H2("₿ CRYPTOCURRENCY REPORTS", style=HEADER_STYLE),
            html.Div(
                style=CARD_STYLE,
                children=[
                    html.H4("Top 10 Cryptos by Market Cap", style=SUBHEADER_STYLE),
                    top_market_cap(engine),
                ],
            ),
            html.Div(
                style=CARD_STYLE,
                children=[
                    html.H4("24h Volume Distribution", style=SUBHEADER_STYLE),
                    volume_distribution(engine),
                ],
            ),
            html.Div(
                style=CARD_STYLE,
                children=[
                    html.H4("Price Distribution", style=SUBHEADER_STYLE),
                    price_distribution(engine),
                ],
            ),
            html.Div(
                style=CARD_STYLE,
                children=[
                    html.H4("Price vs. Market Cap Scatter", style=SUBHEADER_STYLE),
                    price_vs_market_cap(engine),
                ],
            ),
        ],
    )


def user_reports_layout():
    return html.Div(
        style={"padding": "20px"},
        children=[
            html.H2("💱 TRANSACTION REPORTS", style=HEADER_STYLE),
            html.Div(
                style=CARD_STYLE,
                children=[
                    html.H4("Top 10 Users by Transaction Volume", style=SUBHEADER_STYLE),
                    top_users_vol(engine),
                ],
            ),
            html.Div(
                style=CARD_STYLE,
                children=[
                    html.H4("Most Frequently Used Cryptocurrencies", style=SUBHEADER_STYLE),
                    most_freq_crypto(engine),
                ],
            ),
            html.Div(
                style=CARD_STYLE,
                children=[
                    html.H4("Buy vs. Sell Ratio Across All Users", style=SUBHEADER_STYLE),
                    buy_vs_sell(engine),
                ],
            ),
            html.Div(
                style=CARD_STYLE,
                children=[
                    html.H4("Top Conversion Patterns (From → To)", style=SUBHEADER_STYLE),
                    trade_patterns(engine),
                ],
            ),
        ],
    )


# home page
def home_layout():
    return html.Div(
        style={"padding": "100px 20px", "textAlign": "center"},
        children=[
            html.H1(
                "Welcome to CryptoIntern Dashboard",
                style={**HEADER_STYLE, "fontSize": "36px", "marginBottom": "20px"},
            ),
            html.P(
                "Select a page to explore different reports:",
                style={"fontSize": "18px", "marginBottom": "40px", "color": "#ffffff"},
            ),
            html.Div(
                style={"display": "flex", "justifyContent": "center", "gap": "40px"},
                children=[
                    dcc.Link(
                        html.Button("Cryptocurrency Reports", style=NAV_BUTTON_STYLE),
                        href="/crypto",
                    ),
                    dcc.Link(
                        html.Button("Transaction Reports", style=NAV_BUTTON_STYLE),
                        href="/users",
                    ),
                ],
            ),
        ],
    )


app = dash.Dash(__name__, external_stylesheets=google_fonts, suppress_callback_exceptions=True)
server = app.server

app.layout = html.Div(
    style=PAGE_STYLE,
    children=[
        dcc.Location(id="url", refresh=False),
        html.Div(
            style=NAV_STYLE,
            children=[
                dcc.Link(html.Button("Home", style=NAV_BUTTON_STYLE), href="/"),
                dcc.Link(html.Button("Cryptos", style=NAV_BUTTON_STYLE), href="/crypto"),
                dcc.Link(html.Button("Transactions", style=NAV_BUTTON_STYLE), href="/users"),
            ],
        ),
        # page content (populated by callback)
        html.Div(id="page-content", style={"padding": "20px"}),
    ],
)



@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname"),
)
def display_page(pathname):
    if pathname == "/crypto":
        return crypto_reports_layout()
    elif pathname == "/users":
        return user_reports_layout()
    else:
        return home_layout()


if __name__ == "__main__":
    app.run(debug=True)

#Import Libraries
import dash
import dash_labs as dl
import dash_bootstrap_components as dbc


#Create App
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.YETI], plugins=[dl.plugins.pages],
                meta_tags=[{'name':'viewport', 'content':'width=device-width, initial-scale=1.0'}])

app.config.suppress_callback_exceptions=True

app.title = "New Exporter Success Prediction Tool"

# Create Navigation bar
navbar = dbc.NavbarSimple(
    children = [
        dbc.Row(
            [
                dbc.Col(dbc.DropdownMenu
                    (
                        children=[
                            dbc.DropdownMenuItem(page["name"], href=page["path"])
                            for page in dash.page_registry.values()
                            if page["module"] != "pages.not_found_404"],
                        nav=True,
                        in_navbar=True,
                        label="Menu",          
                    )
                ),
            ]
        )
    ],
    brand="New Exporter Success Prediction Tool",
    brand_href="#",
    color="primary",
    dark=True,
    class_name="mb-2"
)

#Main layout
app.layout = dbc.Container(
    [
        dbc.Row(navbar),
        dbc.Row(dl.plugins.page_container),
    ],
    class_name="dbc",
    fluid=True,
)

# This call will be used with Gunicorn server
server = app.server

# Testing server
app.run_server(debug=True, host="localhost", port=8050)

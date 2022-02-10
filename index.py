import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input,Output

# Import data
df = pd.read_csv("VacunaCOVID19Colombia.csv")

# Init the app
app = dash.Dash(__name__)

# Create the layout. The dashboard desing
app.layout = html.Div([
    
    html.Div([
        html.H1('Colombia: Vacunación Por Departamentos'),
        html.Img(src = 'assets/colombia.png')        
    ], className = 'banner'),
    
    html.Div([
        html.Div([
            html.P('Seleccione el Departamento', className = 'fix_label', style = {'color':'black', 'margin-top':'2px'}),
            dcc.Checklist(df.Nom_Territorio.unique(), id = 'states'
            )
        ], className = 'create_container2 two columns', style = {'margin-bottom':'10 px'}),
    ], className = 'row flex-display'),
    
    html.Div([
        html.Div([
            dcc.Graph(id = 'graphic_1', figure ={})
        ], className = 'create_container2 five columns'),
        
        html.Div([
            dcc.Graph(id = 'graphic_2', figure ={})
        ], className = 'create_container2 five columns')
    ], className = 'row flex-display')
    
])

@app.callback(
    Output(component_id='graphic_1', component_property='figure'),
    Input(component_id='show-secret', component_property='n_clicks')
)


if __name__ == "__main__":
    app.run_server(debug= True)

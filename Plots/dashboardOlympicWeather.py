import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df1 = pd.read_csv('../Datasets/Olympic2016Rio.csv')
df2 = pd.read_csv('../Datasets/Weather2014-15.csv')

app = dash.Dash()

# Bar Chart Data
new_df = df1.groupby(['NOC']).agg(
    {'Bronze': 'sum', 'Silver': 'sum', 'Gold': 'sum'})
barchart_df = df1.sort_values(by=['Total'], ascending=[False]).head(20)
data_barchart = [go.Bar(x=barchart_df['NOC'], y=barchart_df['Total'])]

# Stack Bar Chart Data
new_df = df1.groupby(['NOC']).agg(
    {'Bronze': 'sum', 'Silver': 'sum', 'Gold': 'sum'})
stackbarchart_df = df1.sort_values(by=['Total'], ascending=[False]).head(20).reset_index()
trace1_stackbarchart = go.Bar(x=stackbarchart_df['NOC'], y=stackbarchart_df['Bronze'], name='Bronze',
                              marker={'color': '#CD7F32'})
trace2_stackbarchart = go.Bar(x=stackbarchart_df['NOC'], y=stackbarchart_df['Silver'], name='Silver',
                              marker={'color': '#9EA0A1'})
trace3_stackbarchart = go.Bar(x=stackbarchart_df['NOC'], y=stackbarchart_df['Gold'], name='Gold',
                              marker={'color': '#FFD700'})
data_stackbarchart = [trace1_stackbarchart, trace2_stackbarchart, trace3_stackbarchart]

# Line Chart Data
dfL = df2.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
line_df = dfL.groupby(['month'])['actual_max_temp'].max().reset_index()
line_df['month'] = pd.Categorical(line_df['month'],
                                  ['July', 'August', 'September', 'October', 'November', 'December', 'January',
                                   'February', 'March', 'April', 'May', "June"])
line_df = line_df.sort_values('month')
data_linechart = [go.Scatter(x=line_df['month'], y=line_df['actual_max_temp'], mode='lines', name='month')]

# Multi Line Chart Data
multiline_df = df2.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
new_multiline_df = multiline_df.groupby(['month']).agg(
    {'actual_max_temp': 'max', 'actual_mean_temp': 'mean', 'actual_min_temp': 'min'}).reset_index()
new_multiline_df['month'] = pd.Categorical(new_multiline_df['month'],
                                           ['July', 'August', 'September', 'October', 'November', 'December', 'January',
                                            'February', 'March', 'April', 'May', 'June'])
new_multiline_df = new_multiline_df.sort_values('month')
trace1_multiline = go.Scatter(x=new_multiline_df['month'], y=new_multiline_df['actual_max_temp'], mode='lines',
                              name='Max')
trace2_multiline = go.Scatter(x=new_multiline_df['month'], y=new_multiline_df['actual_mean_temp'], mode='lines',
                              name='Mean')
trace3_multiline = go.Scatter(x=new_multiline_df['month'], y=new_multiline_df['actual_min_temp'], mode='lines',
                              name='Min')
data_multiline = [trace1_multiline, trace2_multiline, trace3_multiline]

# Bubble Chart Data
dfB = df2.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
bubble_df = dfB.groupby(['month']).agg(
    {'average_max_temp': 'max', 'average_min_temp': 'min'}).reset_index()

# Preparing data
data_bubblechart = [
    go.Scatter(x=bubble_df['average_min_temp'],
               y=bubble_df['average_max_temp'],
               text=bubble_df['month'],
               mode='markers',
               marker=dict(size=bubble_df['average_max_temp'],color=bubble_df['average_max_temp'], showscale=True))
]

# Heatmap Data
data_heatmap = [go.Heatmap(x=df2['day'],
                           y=df2['month'],
                           z=df2['record_max_temp'].values.tolist(),
                           colorscale='Jet')]

# Layout
app.layout = html.Div(children=[
    html.H1(children='Python Dash',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    html.Div('Web dashboard for Data Visualization using Python', style={'textAlign': 'center'}),
    html.Div('Rio 2016 Olympic Medals', style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.Br(),

    # Bar Chart
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Bar chart', style={'color': '#df1e56'}),
    html.Div('This bar chart represent the number of medals in the top 20 countries.'),
    dcc.Graph(id='graph2',
              figure={
                  'data': data_barchart,
                  'layout': go.Layout(title='Rio 2016 Olympic Medals',
                                      xaxis={'title': 'Country'}, yaxis={'title': 'Number of medals'})
              }
              ),

    # Stack Bar Chart
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Stack bar chart', style={'color': '#df1e56'}),
    html.Div(
        'This stack bar chart represent the number of medals in the top 20 countries, displaying all medal types.'),
    dcc.Graph(id='graph3',
              figure={
                  'data': data_stackbarchart,
                  'layout': go.Layout(title='Rio 2016 Olympic Medals',
                                      xaxis={'title': 'Country'}, yaxis={'title': 'Number of medals'},
                                      barmode='stack')
              }
              ),

    # Line Chart
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Line chart', style={'color': '#df1e56'}),
    html.Div('This line chart represent the actual max temperature of each month in weather statistics.'),
    dcc.Graph(id='graph4',
              figure={
                  'data': data_linechart,
                  'layout': go.Layout(title='Max Temp 2014 - 2015', xaxis_title="Month",
                                      yaxis_title="Max Temp")
              }
              ),

    # Multi Line Chart
    html.H3('Multi Line chart', style={'color': '#df1e56'}),
    html.Div(
        'This line chart represents the max, mean, and min temperatures in the given period.'),
    dcc.Graph(id='graph5',
              figure={
                  'data': data_multiline,
                  'layout': go.Layout(
                      title='Max, Mean, and Min Temperatures of Each Month Jul 2014 - Jun 2015',
                      xaxis={'title': 'Month'}, yaxis={'title': 'Temperature'})
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),

    # Bubble Chart
    html.Hr(style={'color': '#7FDBFF'}),
        html.H3('Bubble chart', style={'color': '#df1e56'}),
        html.Div(
            'This bubble chart represent the average min and max temperature of each month in weather statistics.'),
        dcc.Graph(id='graph6',
                  figure={
                      'data': data_bubblechart,
                      'layout': go.Layout(title='Average Max Min 2014-2015', xaxis_title="Average Min Temp",
                       yaxis_title="Average Max Temp", hovermode='closest')
                  }
                  ),

    # Heat Map
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Heat map', style={'color': '#df1e56'}),
    html.Div(
        'This heat map represent the record maximum temperatures of each month.'),
    dcc.Graph(id='graph7',
              figure={
                  'data': data_heatmap,
                  'layout': go.Layout(title='Record max temperatures by month',
                                      xaxis={'title': 'Day'}, yaxis={'title': 'Month'})
              }
              )

])

if __name__ == '__main__':
    app.run_server()

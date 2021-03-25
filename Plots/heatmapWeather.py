import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')

# Removing empty spaces to avoid errors
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Preparing data
data = [go.Heatmap(x=df['day'],
                   y=df['month'],
                   z=df['record_max_temp'].values.tolist(),
                   colorscale='Jet')]

# Preparing layout
layout = go.Layout(title='Max Temperature Jul 2014 - Jun 2015', xaxis_title="Day of Week",
                   yaxis_title="Month")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='heatmapWeather.html')
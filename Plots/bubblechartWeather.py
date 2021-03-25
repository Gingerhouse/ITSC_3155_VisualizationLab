import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Datasets/Weather2014-15.csv')

# Removing empty spaces to avoid errors
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Creating sum of number of cases group by month Column
new_df = df.groupby(['month']).agg({'average_max_temp': 'max', 'actual_mean_temp': 'mean', 'average_min_temp': 'min'}).reset_index()

new_df['month'] = pd.Categorical(new_df['month'], ['July', 'August', 'September', 'October', 'November', 'December', 'January', 'February', 'March', 'April', 'May', 'June'])

new_df = new_df.sort_values('month')

# Preparing data
data = [
    go.Scatter(x=new_df['average_min_temp'],
               y=new_df['average_max_temp'],
               text=new_df['month'],
               mode='markers',
               marker=dict(size=new_df['actual_mean_temp'] ,color=new_df['actual_mean_temp'] , showscale=True),
               name='actual_mean_temp')
]

# Preparing layout
layout = go.Layout(title='Max vs. Min Temperatures of Each Month Jul 2014 - Jun 2015', xaxis_title="Min Temp",
                   yaxis_title="Max Temp", hovermode='closest')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubblechartWeather.html')
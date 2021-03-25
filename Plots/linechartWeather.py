import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')

# Removing empty spaces to avoid errors
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Creating sum of number of cases group by month Column
new_df = df.groupby(['month'])['actual_max_temp'].max().reset_index()

new_df['month'] = pd.Categorical(new_df['month'], ['July', 'August', 'September', 'October', 'November', 'December', 'January', 'February', 'March', 'April', 'May', 'June'])

new_df = new_df.sort_values('month')

# Preparing data
data = [go.Scatter(x=new_df['month'], y=new_df['actual_max_temp'], mode='lines', name='month')]

# Preparing layout
layout = go.Layout(title='Hottest Temperatures of Each Month Jul 2014 - Jun 2015', xaxis_title='Month',
                   yaxis_title='Temperature')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='linechartWeather.html')

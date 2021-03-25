import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')

# Removing empty spaces to avoid errors
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Creating sum of number of cases group by month Column
new_df = df.groupby(['month']).agg({'actual_max_temp': 'max', 'actual_mean_temp': 'mean', 'actual_min_temp': 'min'}).reset_index()

new_df['month'] = pd.Categorical(new_df['month'], ['July', 'August', 'September', 'October', 'November', 'December', 'January', 'February', 'March', 'April', 'May', 'June'])

new_df = new_df.sort_values('month')

# Preparing data
trace1 = go.Scatter(x=new_df['month'], y=new_df['actual_max_temp'], mode='lines', name='Max')
trace2 = go.Scatter(x=new_df['month'], y=new_df['actual_mean_temp'], mode='lines', name='Mean')
trace3 = go.Scatter(x=new_df['month'], y=new_df['actual_min_temp'], mode='lines', name='Min')
data = [trace1,trace2,trace3]


# Preparing layout
layout = go.Layout(title='Max, Mean, and Min Temperatures of Each Month Jul 2014 - Jun 2015', xaxis_title="Month",
                   yaxis_title="Temperature")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='multilinechartWeather.html')
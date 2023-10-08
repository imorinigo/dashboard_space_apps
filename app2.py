import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from windrose import WindroseAxes

# Load your weather dataset (assuming it's a pandas DataFrame)
# Replace 'df' with the name of your DataFrame.
# Example: df = pd.read_csv('your_weather_data.csv')

st.set_page_config(layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("Weather Data Visualization")

# Create a line plot for temperature
st.write("## Temperature Over Time")

# Layout the metrics in two rows
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Temperature", "70 °F", "1.2 °F")
with col2:
    st.metric("Wind", "9 mph", "-8%")
with col3:
    st.metric("Precipitation", "45%", "5%")
with col4:
    st.metric("Humidity", "86%", "-4%")

# Load temperature data
df_temp = pd.read_csv("csv/all_temperatures.csv")


import plotly.express as px

def plot_vars2(data, x, y, year):
    # Create a figure with Plotly Express
    fig = px.line(data, x=x, y=y, color=year, title='Variation of temperature over the years')
    
    # Add markers to the lines
    fig.update_traces(mode='lines+markers')

    # Annotate the highest and lowest points
    max_value = data[y].max()
    min_value = data[y].min()
    max_x = data[data[y] == max_value][x].values[0]
    min_x = data[data[y] == min_value][x].values[0]

    fig.add_annotation(
        text=f'Highest: {max_value:.2f}',
        x=max_x,
        y=max_value + 1,
        arrowhead=2,
        arrowcolor='green',
        arrowwidth=2,
        arrowsize=1,
        font=dict(size=16, color='green')
    )

    fig.add_annotation(
        text=f'Lowest: {min_value:.2f}',
        x=min_x,
        y=min_value - 1,
        arrowhead=2,
        arrowcolor='red',
        arrowwidth=2,
        arrowsize=1,
        font=dict(size=18, color='red')
    )

    # Customize axes and legend
    fig.update_xaxes(title_text='Years', title_font=dict(size=22))
    fig.update_yaxes(title_text='TEMPERATURE C', title_font=dict(size=22))
    fig.update_layout(legend_title_text='YEAR', legend_title_font=dict(size=22))

    return fig


def plot_vars3(data, x, y, year):
    # Create a figure with Plotly Express
    fig = px.line(data, x=x, y=y, color=year, title='Variation of temperature over the years')
    
  
    fig.update_layout(width=1200, height=600)
    # Add markers to the lines
    fig.update_traces(mode='lines+markers')

    # Annotate the highest and lowest points
    max_value = data[y].max()
    min_value = data[y].min()
    max_x = data[data[y] == max_value][x].values[0]
    min_x = data[data[y] == min_value][x].values[0]

    fig.add_annotation(
        text=f'Highest: {max_value:.2f}',
        x=max_x,
        y=max_value + 1,
        arrowhead=2,
        arrowcolor='green',
        arrowwidth=2,
        arrowsize=1,
        font=dict(size=16  , color='green')
    )

    fig.add_annotation(
        text=f'Lowest: {min_value:.2f}',
        x=min_x,
        y=min_value - 1,
        arrowhead=2,
        arrowcolor='red',
        arrowwidth=2,
        arrowsize=1,
        font=dict(size=18, color='red')
    )

    # Customize axes and legend
    fig.update_xaxes(title_text='Years', title_font=dict(size=22))
    fig.update_yaxes(title_text='TEMPERATURE C', title_font=dict(size=22))
    fig.update_layout(legend_title_text='YEAR', legend_title_font=dict(size=22))

    # Display the plot in Streamlit
    st.plotly_chart(fig)


# Create a line chart for temperature
st.write("### Line Chart")
st.plotly_chart(plot_vars3(df_temp, 'day', 'valor', 'year'))

# Load precipitation data
all_precipitacion_df = pd.read_csv("csv/precipitacion/all_precipitacion.csv")

# Create a bar chart for precipitation
st.write("### Yearly Precipitation")
plt.figure(figsize=(70, 26))
sns.barplot(x='Month_Name', y='Valor', data=all_precipitacion_df, palette='Blues')
plt.title('Year Precipitation', fontsize=50, color='blue')
plt.xlabel('Month Name')
plt.ylabel('Precipitation (mm)')

# Display the bar chart
st.pyplot(plt)

# Load wind data
ros = pd.read_csv("csv/rosely/2022_dir_velocidad.csv")

# Create a wind rose chart
st.write("### Wind Rose")
fig = plt.figure(figsize=(15, 15))
ax = WindroseAxes(fig, rect=[0.1, 0.1, 0.8, 0.8])
fig.add_axes(ax)
ax.bar(ros.Valor_direccion, ros.Valor_veloc, bins=16, normed=True, opening=0.8)
ax.set_legend()

# Display the wind rose chart
st.pyplot(fig)


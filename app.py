import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
#import plotly.graph_objects as go
from windrose import WindroseAxes

# Load your weather dataset (assuming it's a pandas DataFrame)
# Replace 'df' with the name of your DataFrame.
# Example: df = pd.read_csv('your_weather_data.csv')


st.set_page_config(layout='wide')

#with open('style.css') as f:
  #  st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
   


st.title("Weather Data Visualization")

# Create a line plot for temperature
st.write("## Temperature Over Time")

#               ROW A

st.markdown('### Metrics')
col1, col2, col3,col4 = st.columns(4)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Precipitation", "45%", "5%")
col4.metric("Humidity", "86%", "-4%")

# Row B

#c1, c2 = st.columns((55,24))

df_temp=pd.read_csv("csv/all_temperatures.csv") 
print(df_temp)


#PLOT EXAMPLE 2 
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

def plot_vars2(data, x, y, year):
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

# Example usage in Streamlit
# plot_vars(your_data_frame, 'x_column', 'y_column', 'year_column')



st.markdown('### Line chart')

plot_vars2(df_temp,'day', 'valor', 'year')

with st.expander("See explanation"):
    st.write("The chart above shows some numbers I picked for you."
             "I rolled actual dice for these, so they're *guaranteed* to"
             "be random.")
    st.image("https://static.streamlit.io/examples/dice.jpg")


all_precipitacion_df= pd.read_csv("csv/precipitacion/all_precipitacion.csv")
ros=pd.read_csv("csv/rosely/2022_dir_velocidad.csv")

c1, c2 = st.columns((5,5))
with c1:
    st.title('Year Precipitation')

        # Define the order of months

        # Create a bar plot using Seaborn and set the order of x-axis labels
        #plt.figure(figsize=(100, 56))
    sns.barplot(x='Month_Name', y='Valor', data=all_precipitacion_df, palette='Blues')
    #plt.title('Year Precipitation', fontsize=50, color='blue' )
    plt.xlabel('Month_name')
    plt.ylabel('Precipitation (mm)')
        # Display the plot in Streamlit
    st.pyplot(plt)


with c2:

    # ROSA DE VIENTO
    fig = plt.figure(figsize=(15, 5))
    ax = WindroseAxes(fig, rect=[0.1, 0.1, 0.8, 0.8])  # Define rect coordinates here

            # Add the windrose
    fig.add_axes(ax)
    ax.bar(ros.Valor_direccion, ros.Valor_veloc, bins=16, normed=True, opening=0.8)
    ax.set_legend()

    use_container_width=True
            # Display the plot in Streamlit
    st.pyplot(fig)





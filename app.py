import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
#import plotly.graph_objects as go
from windrose import WindroseAxes


st.set_page_config(layout='wide')

#with open('style.css') as f:
  #  st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
   


st.title("Weather Insights Analysis - Ypacarai Lake" )

# Create a line plot for temperature
st.write("### Monitoring the Lake's Vital Signs: Real-time Temperature Insights")

#               ROW A

#st.markdown('### Metrics')
col1, col2, col3,col4 = st.columns(4)
col1.metric("Temperature", "27°C", "2°C")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Precipitation", "45%", "5%")
col4.metric("Humidity", "86%", "-4%")

# Row B

#c1, c2 = st.columns((55,24))

df_temp=pd.read_csv("csv/all_temperatures.csv") 
print(df_temp)

st.markdown('### Analyzing Temperature Variations')
#PLOT EXAMPLE 2 
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

def plot_vars2(data, x, y, year):
    # Create a figure with Plotly Express
    fig = px.line(data, x=x, y=y, color=year)
    
  
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
    fig.update_yaxes(title_text='TEMPERATURE °C', title_font=dict(size=22))
    fig.update_layout(legend_title_text='YEAR', legend_title_font=dict(size=22))

    # Display the plot in Streamlit
    st.plotly_chart(fig)


#st.markdown('### Line chart')

plot_vars2(df_temp,'day', 'valor', 'year')



with st.expander("See explanation of the above figure"):
    st.write("According to Sapriza, temperature is related to algal bloom because the majority of species prefer higher temperatures (Bonilla, 2009), reason why most blooms "
             " occur during the summer or spring (Benítez Rodas, et al., 2017). Indeed, this aligns with the results obtained in the mention study. Where 75% of the cases studied"
             " prior to the bloom, the periods in which this phenomenon is observed have higher temperatures compared to their respective periods when the event is not observed."
             "The event is referred to green colored water in the lake. Furthermore, according to the characterization of algae, most of these blooms exhibit their highest growth"
             "rates at temperatures between 25°C and 30°C. These conditions are observed in the days leading up to the sightings of the blooms and, conversely, are disrupted during the days leading up to the periods in which the event is not recorded.   " 

            "Source: Sapriza and Pavetti, 2023. Catholic University, Science and Technology Faculty)")

# SECOND ROW   
all_precipitacion_df= pd.read_csv("csv/precipitacion/all_precipitacion.csv")
ros=pd.read_csv("csv/rosely/2022_dir_velocidad.csv")

c1, c2 = st.columns((7,5))
with c1:
    #st.title('Yearly Precipitation Trends')

        # Define the order of months

        # Create a bar plot using Seaborn and set the order of x-axis labels
        #plt.figure(figsize=(100, 56))
    st.title('Monthly Precipitation Trends Across Years')

# Create a bar plot using Seaborn
    #plt.figure(figsize=(16, 6))
    sns.barplot(data=all_precipitacion_df, x='Month_Name', y='Valor', hue='Year', palette='Blues')
    #plt.title('Yearly Precipitation by Month')
    plt.xlabel('Month')
    plt.ylabel('Precipitation (mm)')
    plt.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xticks(rotation=45)

    # Display the plot in Streamlit
    st.pyplot(plt)

    with st.expander("See explanation of the above figure"):
        st.write(" It is well-documented in the literature that rainfall generally does not promote blooming "
                 "(Bonilla, 2009), unless it involves organic matter runoff that can be utilized by algae for " 
                 "their growth. In such cases, rainfall should ideally occur several days before the onset of the bloom to allow sufficient time for its development. Examining periods with blooms, it's noteworthy that 75% of them occur without prior rainfall. Among the remaining 25% of cases,"
                 " one event witnessed rainfall five days before the algae were observed, possibly suggesting an input of organic matter through runoff. Following the blooms, there were three instances of post-bloom precipitation, "
                 "which may have contributed to the dispersion and dilution of the algae. "
"Source: Sapriza and Pavetti, 2023. Catholic University, Science and Technology Faculty ")

with c2:

    # ROSA DE VIENTO
    st.title('Wind Direction and Speed Visualization')
    fig = plt.figure() #figsize=(15, 5)
    ax = WindroseAxes(fig, rect=[0.1, 0.1, 0.8, 0.8])  # Define rect coordinates here

            # Add the windrose
    fig.add_axes(ax)
    ax.bar(ros.Valor_direccion, ros.Valor_veloc, bins=16, normed=True, opening=0.8)
    ax.set_legend()

    use_container_width=True
            # Display the plot in Streamlit
    st.pyplot(fig)

    with st.expander("See explanation of the above figure"):
        st.write("Wind speed can interfere in the mixing zone, reactivating cyanobacteria that are already in the process of sedimentation and thus promoting blooming (Benítez Rodas et al., 2017) (Delgado, Lozano, & Facetti Masulli, 2014). Wind gust can contribute to the reactivation of cyanobacteria, resulting in a bloom occurring again two and three days after the initial event, respectively."
        "Source: Sapriza and Pavetti, 2023. Catholic University, Science and Technology Faculty ")



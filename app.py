import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

#dataset
df = pd.read_csv('india.csv')

#to wide the streamlit width
st.set_page_config(layout='wide')

#first select box data
state_name = df['State'].unique().tolist()
state_name.insert(0,'Select')
state_name.insert(1,'Overall India')

#Second and third selectbx data
features = df.columns[5:].tolist()
features.insert(0,'Select')



#Sidebar title
st.sidebar.title('India Census Data Visualization')

#sidebar first selectbox
state_name = st.sidebar.selectbox('Select a state',state_name)

#sidebar second selectbox
primary = st.sidebar.selectbox('Select Primary Parameter',features)

#sidebar third selectbox
secondary = st.sidebar.selectbox('Select Secondary Parameter',features)

#sidebar button
btn1 = st.sidebar.button('Plot Graph')


if btn1:
    if state_name == 'Overall India':

        #title
        st.markdown(
            """
            <style>
            .custom-subheader {
                color: #f39c12;  /* Change to your desired color */
                font-size: 27px; /* Adjust the font size as needed */
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # Using the custom subheader with markdown
        st.markdown('<div class="custom-subheader">Size Represents the Primary Parameter</div>', unsafe_allow_html=True)
        st.markdown('<div class="custom-subheader">Color Represents the Secondary Parameter</div>',
                    unsafe_allow_html=True)

        #plotly data
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude",
                                zoom=3.5, mapbox_style='carto-positron',
                                size= primary, color=secondary,
                                color_continuous_scale=px.colors.cyclical.IceFire,
                                size_max=30,width=1200,height=700)

        #to show the graph in streamlit
        st.plotly_chart(fig,use_container_width=True)

    else:
        st.markdown(
            """
            <style>
            .custom-subheader {
                color: #f39c12;  /* Change to your desired color */
                font-size: 27px; /* Adjust the font size as needed */
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # Using the custom subheader with markdown
        st.markdown('<div class="custom-subheader">Size Represents the Primary Parameter</div>', unsafe_allow_html=True)
        st.markdown('<div class="custom-subheader">Color Represents the Secondary Parameter</div>',
                    unsafe_allow_html=True)


        # for each stat
        state_df = df[df['State'] == state_name]

        #graph plot
        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude",
                                zoom=3.5, mapbox_style='carto-positron',
                                size= primary, color=secondary,
                                color_continuous_scale=px.colors.cyclical.IceFire,
                                size_max=30,width=1200,height=700,
                                hover_name='District')

        #to show the graph in streamlit
        st.plotly_chart(fig,use_container_width=True)









import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
st.set_page_config(layout='wide')
data_=pd.read_csv('WORLD.csv')
data_=data_.iloc[:,:-1]

year=data_.columns.str[:5][4:].astype(int)
selected_df=st.selectbox('Enter GDP or Else Type :-',options=data_['Series Name'].unique())
df=data_[data_['Series Name']== selected_df ]

def coumpar_country_GDP():
    c_name=df['Country Name'].unique()
    country_name=st.multiselect('Choose country name which you whant to coumper.',options=c_name,default=None)
    try:
    

        country_data=[]
        for i in country_name:
            c1=df[df['Country Name'] == i]
            c1=np.array(c1.iloc[:,4:]).T
            c1=pd.DataFrame(c1,columns=['Value'])
            c1['Year']=year
            c1['Country Name']= i
            country_data.append(c1)
        df_country_coumparition=pd.concat(country_data,axis=0)
        fig=px.line(df_country_coumparition,x='Year',y='Value',color='Country Name',width=1350,height=700)
        
        # t=df_country_coumparition.max()[4:].astype(float).astype(int)
        # y_axis_tickvals = range=list(np.linspace(0,int('1'+('0'*len(str(t.max())))),2).astype(int))  
        # # Update layout to set y-axis range and title (optional)
        # fig.update_layout( yaxis_range=y_axis_tickvals,yaxis_title="Avrage Value")
        st.plotly_chart(fig)
    except:
        st.write('Select Country Names.')
if df is not None:       
    coumpar_country_GDP()


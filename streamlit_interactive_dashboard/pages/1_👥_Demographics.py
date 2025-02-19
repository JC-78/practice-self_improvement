import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

st.title("Demographics")
st.markdown("This interactive dashboard supports the exploration of the demographics (age, gender, and race) of the people involved in fatal accidental overdoses in Allegheny County.  You can filter by the year of the overdose incident, as well as the primary drug present in the incident.")

df = pd.read_csv("data/overdose_data_092223.csv")
df.death_date_and_time = pd.to_datetime(df.death_date_and_time)

# to make the visualizations more meaningful, we unabbreviate the race and sex columns

df['race'] = df['race'].str.replace('W','White')
df['race'] = df['race'].str.replace('B','Black')
df['race'] = df['race'].str.replace('H|A|I|M|O|U','Other', regex=True) #there are very few non-white/back decedents in this dataset, so we merge the remaining categories to 'other'
df.dropna(subset = ['race'], inplace=True)  #get rid of nulls

df['sex'] = df['sex'].str.replace('M','Male')
df['sex'] = df['sex'].str.replace('F','Female')

st.subheader("Filters")

#insert filters here

# st.sidebar.subheader('Filters')

# year_range = st.sidebar.slider('Year Range', min_value=df['case_year'].min(), max_value=df['case_year'].max(), value=(df['case_year'].min(), df['case_year'].max()))

# filtered_df = df[(df['case_year'] >= year_range[0]) & (df['case_year'] <= year_range[1])]

# selected_drugs = st.sidebar.multiselect('Primary Drug', df['combined_od1'].unique())

# if selected_drugs:
#     filtered_df = filtered_df[filtered_df['combined_od1'].isin(selected_drugs)]


# filters_container = st.container()

# with filters_container:
#     year_range = st.slider('Year Range', min_value=df['case_year'].min(), max_value=df['case_year'].max(),
#                            value=(df['case_year'].min(), df['case_year'].max()))

#     selected_drugs = st.multiselect('Primary Drug', df['combined_od1'].unique())

# filtered_df = df[(df['case_year'] >= year_range[0]) & (df['case_year'] <= year_range[1])]
# if selected_drugs:
#     filtered_df = filtered_df[filtered_df['combined_od1'].isin(selected_drugs)]
filters_container = st.container()

with filters_container:
    col1, col2 = st.columns(2)  # Divide the container into two columns
    
    with col1:
        year_range = st.slider('Year Range', min_value=df['case_year'].min(), max_value=df['case_year'].max(),
                               value=(df['case_year'].min(), df['case_year'].max()))
    
    with col2:
        selected_drugs = st.multiselect('Primary Drug', df['combined_od1'].unique())

# Applying filters
filtered_df = df[(df['case_year'] >= year_range[0]) & (df['case_year'] <= year_range[1])]
if selected_drugs:
    filtered_df = filtered_df[filtered_df['combined_od1'].isin(selected_drugs)]


#insert visualizations here

year_histogram = alt.Chart(filtered_df).mark_bar().encode(
    x=alt.X('case_year:O', axis=alt.Axis(title='Year')),  
    y='count()',
).properties(
    title='Year'
)

age_histogram = alt.Chart(filtered_df).mark_bar().encode(
    x='count()',
    y='age:Q',
).properties(
    title='Age'
)

gender_bar_chart = alt.Chart(filtered_df).mark_bar().encode(
    x='count()',
    y='sex:N',
).properties(
    title='Gender'
)

race_mapping = {
    'White': 'White',
    'Black': 'Black',
    'Other': 'Other'
}

def map_race(race):
    return race_mapping.get(race, 'Other')

filtered_df['race_binned'] = filtered_df['race'].apply(map_race)

race_bar_chart = alt.Chart(filtered_df).mark_bar().encode(
    x='count()',
    y=alt.Y('race_binned:N', title='Race', axis=alt.Axis(labelExpr="if(datum.value == 'Other', 'Other', datum.label)")),
).properties(
    title='Race'
)

st.subheader('Visualizations')
# st.altair_chart(year_histogram, use_container_width=True)
# st.altair_chart(age_histogram, use_container_width=True)
# st.altair_chart(gender_bar_chart, use_container_width=True)
# st.altair_chart(race_bar_chart, use_container_width=True)
st.altair_chart(year_histogram, use_container_width=True)

charts_container = st.container()

with charts_container:
    col1, col2, col3 = st.columns(3)  
    with col1:
        st.altair_chart(age_histogram, use_container_width=True)
    with col2:
        st.altair_chart(gender_bar_chart, use_container_width=True)
    with col3:
        st.altair_chart(race_bar_chart, use_container_width=True)

        

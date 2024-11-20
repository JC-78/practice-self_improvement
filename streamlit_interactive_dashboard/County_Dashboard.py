import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

st.header("_Allegheny County_ :red[Fatal Accidental Overdoses]")

st.markdown("A series of interactive dashboards to support exploration of the Allegheny County Fatal Accidental Overdoses dataset.")

st.markdown('This data is published from the [Western Pennsylvania Regional Data Center](https://data.wprdc.org/dataset/allegheny-county-fatal-accidental-overdoses).  It describes fatal accidental overdose incidents in Allegheny County, denoting age, gender, race, drugs present, zip code of incident and zip code of residence.')

st.markdown("This is the raw data used to produce the dashboard:")

df = pd.read_csv("data/overdose_data_092223.csv")
df.death_date_and_time = pd.to_datetime(df.death_date_and_time)

st.dataframe(df)

st.markdown("Please choose a dashboard using the sidebar on the left.")


# # Add a sidebar to the dashboard for filters
# st.sidebar.subheader('Filters')

# year_range = st.sidebar.slider('Year Range', min_value=df['case_year'].min(), max_value=df['case_year'].max(), value=(df['case_year'].min(), df['case_year'].max()))

# filtered_df = df[(df['case_year'] >= year_range[0]) & (df['case_year'] <= year_range[1])]

# selected_drugs = st.sidebar.multiselect('Primary Drug', df['combined_od1'].unique())

# if selected_drugs:
#     filtered_df = filtered_df[filtered_df['combined_od1'].isin(selected_drugs)]

# year_histogram = alt.Chart(filtered_df).mark_bar().encode(
#     x='case_year:O',
#     y='count()',
# ).properties(
#     title='Year Histogram'
# )

# age_histogram = alt.Chart(filtered_df).mark_bar().encode(
#     x='count()',
#     y='age:Q',
# ).properties(
#     title='Age Histogram'
# )

# gender_bar_chart = alt.Chart(filtered_df).mark_bar().encode(
#     x='count()',
#     y='sex:N',
# ).properties(
#     title='Gender Bar Chart'
# )

# race_mapping = {
#     'W': 'White',
#     'B': 'Black'
# }

# # Function to map anything other than 'B' and 'W' to 'Other'
# def map_race(race):
#     return race_mapping.get(race, 'Other')

# filtered_df['race_binned'] = filtered_df['race'].apply(map_race)

# race_bar_chart = alt.Chart(filtered_df).mark_bar().encode(
#     x='count()',
#     y=alt.Y('race_binned:N', title='Race', axis=alt.Axis(labelExpr="if(datum.value == 'Other', 'Other', datum.label)")),
# ).properties(
#     title='Race Bar Chart'
# )

# st.subheader('Visualizations')
# st.altair_chart(year_histogram, use_container_width=True)
# st.altair_chart(age_histogram, use_container_width=True)
# st.altair_chart(gender_bar_chart, use_container_width=True)
# st.altair_chart(race_bar_chart, use_container_width=True)

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Load data
df = pd.read_csv("data/overdose_data_092223.csv")
df['death_date_and_time'] = pd.to_datetime(df['death_date_and_time'])

# Title and description
st.title("Trends")
st.markdown("This interactive dashboard supports the exploration of trends of the primary drugs involved in fatal accidental overdoses in Allegheny County. You can filter by the date of the overdose incident, as well as select the number of top-ranked primary drugs to show.")

# Filters
st.subheader("Filters")

filter_col1, filter_col2 = st.columns(2)

with filter_col1:
    date_range = st.slider("Select Date Range", df['death_date_and_time'].min().date(), df['death_date_and_time'].max().date(), (df['death_date_and_time'].min().date(), df['death_date_and_time'].max().date()))
    date_range = tuple(pd.Timestamp(date) for date in date_range)

with filter_col2:
    num_top_drugs = st.number_input("Select Number of Top Drugs", min_value=1, max_value=10, value=8)

filtered_df = df[(df['death_date_and_time'] >= date_range[0]) & (df['death_date_and_time'] <= date_range[1])]

drug_counts = filtered_df.groupby([filtered_df['death_date_and_time'].dt.year, 'combined_od1']).size().reset_index(name='count')

top_drugs = drug_counts.groupby('combined_od1')['count'].sum().nlargest(num_top_drugs).index.tolist()

drug_counts = drug_counts[drug_counts['combined_od1'].isin(top_drugs)]

charts = []
for drug in top_drugs:
    chart = alt.Chart(drug_counts[drug_counts['combined_od1'] == drug]).mark_area(opacity=0.3).encode(
        x=alt.X('death_date_and_time:O', axis=alt.Axis(title='Fatal overdoses per year')),  
        y='count:Q',
        color='combined_od1:N'
    ).properties(
        width=600,
        height=300,
        title=f'Trend for {drug}'
    )
    charts.append(chart)

charts_combined = alt.vconcat(*charts)

st.altair_chart(charts_combined)

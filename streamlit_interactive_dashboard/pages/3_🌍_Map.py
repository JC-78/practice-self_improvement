import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("data/overdose_data_092223.csv")
df['death_date_and_time'] = pd.to_datetime(df['death_date_and_time'])
df.incident_zip=pd.to_numeric(df['incident_zip'],errors='coerce')
df=df.dropna(subset=['incident_zip'])
df['incident_zip'] = df['incident_zip'].astype(int)

filtered_dates=st.slider("Date filter",min_value=df['death_date_and_time'].dt.date.min(),max_value=df['death_date_and_time'].dt.date.max(),value=(df['death_date_and_time'].dt.date.min(),df['death_date_and_time'].dt.date.max()))

df_latlon = pd.read_csv("data/zipcodes_latlon.csv")
df_pitt = pd.read_csv("data/zipcodes_AlleghenyCounty.csv")
tmp=df['death_date_and_time']
df=df[ (tmp.dt.date<=max(filtered_dates)) & (tmp.dt.date>=min(filtered_dates))]

zip_cases=df.groupby(['incident_zip'])['incident_zip'].count() 
filtered_case_count=st.slider("Case filter",min_value=zip_cases.min(),max_value=zip_cases.max(),value=(zip_cases.min(),zip_cases.max()))

zip_cases=zip_cases.to_frame()
zip_cases=zip_cases.rename(columns={'incident_zip':'case_count'}).reset_index()
tmp=zip_cases['case_count']
zip_cases=zip_cases[(tmp<=max(filtered_case_count))&(tmp>=min(filtered_case_count))]

zip_cases=zip_cases.rename(columns={'incident_zip':'ZIP'})
zip_cases=zip_cases.merge(df_latlon,how='left',on='ZIP')
zip_cases=zip_cases.dropna()
zip_cases['circle_size']=zip_cases['case_count']*10
# st.map(filtered_dates,latitude='LAT',longitude='LNG')
st.map(zip_cases,latitude='LAT',longitude='LNG',size='circle_size')
####
# Filter out non-numeric and missing values in 'incident_zip' column
# df = df[df['incident_zip'].notna() & df['incident_zip'].str.isdigit()]
# df['incident_zip'] = df['incident_zip'].astype(int)



# allegheny_zipcodes_list = allegheny_zipcodes['ZIPCODE'].tolist()
# df_allegheny = df[df['incident_zip'].isin(allegheny_zipcodes_list)]

# df_allegheny = df_allegheny.merge(zipcodes_latlon, how='left', left_on='incident_zip', right_on='ZIP')

# st.sidebar.header('Filters')

# min_date = df_allegheny['death_date_and_time'].min()
# max_date = df_allegheny['death_date_and_time'].max()

# # Handle NaN values
# if pd.isna(min_date):
#     min_date = pd.Timestamp('1900-01-01')
# if pd.isna(max_date):
#     max_date = pd.Timestamp.now()

# col1, col2 = st.columns(2)
# with col1:
#     date_range = st.date_input('Date Range', 
#                                min_value=min_date, 
#                                max_value=max_date, 
#                                value=(min_date, max_date))

# start_date = pd.Timestamp(date_range[0])
# end_date = pd.Timestamp(date_range[1])

# with col2:
#     min_cases, max_cases = st.slider('Number of Cases', 
#                                       min_value=df_allegheny['incident_zip'].value_counts().min(), 
#                                       max_value=df_allegheny['incident_zip'].value_counts().max(), 
#                                       value=(df_allegheny['incident_zip'].value_counts().min(), df_allegheny['incident_zip'].value_counts().max()))

# filtered_data = df_allegheny[(df_allegheny['death_date_and_time'] >= start_date) & 
#                              (df_allegheny['death_date_and_time'] <= end_date) &
#                              (df_allegheny['incident_zip'].value_counts() >= min_cases) &
#                              (df_allegheny['incident_zip'].value_counts() <= max_cases)]

# st.header('Prevalent Locations of Fatal Accidental Overdoses in Allegheny County')

# # st.map(filtered_data[['LAT', 'LNG']])
# st.map(filtered_data,latitude='LAT',longitude='LNG')

# st.write('Filtered Data:')
# st.write(filtered_data)

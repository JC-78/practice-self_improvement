# hw3-template

In this assignment, you will adopt the persona of being a data scientist for Allegheny County’s Health Department.  Your goal is to build data science tools to make it easier for the health department to understand trends of an ongoing health crisis:  fatal accidental overdoses from a variety of drugs in the county.  The Western Pennsylvania Regional Data Center publishes a monthly dataset that describes fatal accidental overdose incidents in Allegheny County, denoting age, gender, race, drugs present, zip code of incident and zip code of residence.

This data, downloaded as of September 22, 2023, is located in [data/overdose_data_092223.csv](data/overdose_data_092223.csv)

Through a series of assignments, you will build out a dashboard to support the interactive exploration and analysis of the dataset.  You will use this same repository for Assignments 3a, 3b, and 3c.  

- [ ] For Assignment 3a, Update the provided Streamlit python file, `pages/1_👥_Demographics.py`
- [ ] For Assignment 3b, Update the provided Streamlit python file, `pages/2_📈_Trends.py`
- [ ] For Assignment 3c, Update the provided Streamlit python file, `pages/3_🌍_Map.py`
- [ ] In addition, submit your Github repository URL on Canvas for each of the three assignments.

## Running the Streamlit app

You can execute the Streamlit app by running `streamlit run County_Dashboard.py`


-------section A

Q:Did you notice any interesting patterns or trends in the dataset?
A: I thought it was interesting to see the white race consistently dominate in terms of count of records over black race every year. I was anticipating it to be the other way around due to expectation of usual racial bias in the data collected.

Q:Was it possible to understand how the dataset was different in the earlier years versus the more recent years? 
If so, what were some differences?  
If not, how would you suggest changing the dashboard to make differences easier to find?

A:In earlier years (2007-2016), the number of cases every year was monotonoically increasing. From 2017 onward, although it was increasing mostly every year, there were two years(at the start and at the end of the spectrum) when the number of cases lowered drastically. 

Also, in the earlier years, there were records of 400 black and 2600 white individuals. In the later years, there were 800 black and 2800 white individuals. Although the increase in record of black individuals is percentage-wise lower than that of white individuals, there is higher absolute increase in the record of black individuals in the later years. 

Q:Did you discover any filters that demonstrated big differences from the overall dataset among the demographics (such as age, race, or gender)?

A: By filtering out only years 2022-2023, I saw that the distribution of age histogram would vary from its usual distributions in others. From normal distribution, it would become more skewed to the left. I thought this was interesting, as this indicated the increase in younger people contributing to the rise in count of records. 

Q:Are there any other features you wish were present in your dashboard to either make discovery easier or to explore alternative aspects of the dataset?

A:I wish there was more features that went in-depth of the drug's details. For example, 
are they depressants or opioids? Such information would help me explore what are recurring drug trait types in majority of cases recorded.

-------section B


Did you notice any interesting patterns or trends in the dataset?
I thought it was interesting that for the top 5 drugs, the count of cases peaked between 2020-2022 for three of them (heroin,cocaine,fentanyl) but the count was rock bottom for other two(alprazolam, alcohol). Perhaps this indicates people having switched between drugs.

Was it possible to understand how the dataset was different in the earlier years versus the more recent years? 
If so, what were some differences?  
If not, how would you suggest changing the dashboard to make differences easier to find?

Thanks to the 'data range' feature, it was easier to see how the dataset was different in the earlier years versus the more recent years. For example, you can see how most drugs(Ex.Cocaine,Fentanyl) generally increased in terms of case counts over years. You can also see some cases, in which a drug's high case number hits rock bottom in later years and recover, or stays low at bottom (ex.Heroin and Alcohol)

Are there any other features you wish were present in your dashboard to either make discovery easier or to explore alternative aspects of the dataset?

Give that we have visualisation in time series format, I think it would be interesting to break this visualisation down into more lower-level components, such as seasonality and cyclical component.

-------section C

Did you notice any interesting patterns or trends in the dataset?

I thought there was an interesting change in patterns from first half to second half of data range filter. From 2007 to 2015, there were noticeable hot spots in terms of cases and they were Mount Oliver, Hill District, and region between East Allegheny and strip district. Then, in the second half (2015 to 2023), the radius of these 3 regions drastically increased. 

Was it possible to understand how the dataset was different in the earlier years versus the more recent years? 

It was possible to understand how the dataset was different in the earlier years due to the date filter and different circle sizes indicating the location range of cases recorded.

If so, what were some differences?  

There were more noticeable hotspots, both small and hot, in the earlier years. On the other hand, in later years, every hotspot became so relatively larger that even smaller hotspots became of medium size. 

Are there any other features you wish were present in your dashboard to either make discovery easier or to explore alternative aspects of the dataset?

It'd be interesting to encode the colour of cirlces, depending on the cause of majority of cases recorded around that area. 
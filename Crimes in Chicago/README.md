# Crimes in Chicago

Reported incidents of crime (with the exception of murders where data exists for each victim) 
that occurred in the City of Chicago from 2001 to present. Data is extracted from 
the Chicago Police Department's CLEAR (Citizen Law Enforcement Analysis and Reporting) system.

Download CSV file (~1.7 GB) from https://catalog.data.gov/dataset/crimes-2001-to-present-398a4  
and save it as <code>Crimes in Chicago/Crimes_-_2001_to_present.csv</code>  
Next, run <code>crimes_in_chicago.py</code>

Columns:
- Date - date when the incident occurred. this is sometimes a best estimate.
- Primary Type - The primary description of the IUCR code.
- Description - The secondary description of the IUCR code, a subcategory of the primary description.
- Location Description - Description of the location where the incident occurred.
- Arrest - Indicates whether an arrest was made.

- Domestic - Indicates whether the incident was domestic-related as defined by 
  the Illinois Domestic Violence Act.

- Beat - Indicates the beat where the incident occurred. 
  A beat is the smallest police geographic area – each beat has a dedicated police beat car.
  Three to five beats make up a police sector, and three sectors make up a police district.
  The Chicago Police Department has 22 police districts.
  See the beats at https://data.cityofchicago.org/d/aerh-rz74

- District - Indicates the police district where the incident occurred.
  See the districts at https://data.cityofchicago.org/d/fthy-xz3r

- Ward - The ward (City Council district) where the incident occurred.
  See the wards at https://data.cityofchicago.org/d/sp34-6z76
  
- Community Area - Indicates the community area where the incident occurred. 
  Chicago has 77 community areas. See the community areas at 
  https://data.cityofchicago.org/d/cauq-8yn6
  
Example:
ID,Case Number,Date,Block,IUCR,Primary Type,Description,Location Description,Arrest,Domestic,Beat,District,Ward,Community Area,FBI Code,X Coordinate,Y Coordinate,Year,Updated On,Latitude,Longitude,Location,Historical Wards 2003-2015,Zip Codes,Community Areas,Census Tracts,Wards,Boundaries - ZIP Codes,Police Districts,Police Beats  
11706917,JC287103,05/31/2019 11:55:00 PM,052XX W HURON ST,143A,WEAPONS VIOLATION,UNLAWFUL POSS OF HANDGUN,STREET,true,false,1524,015,37,25,15,,,2019,06/07/2019 04:05:48 PM,,,,,,,,,,,  
11706936,JC287099,05/31/2019 11:53:00 PM,002XX S DEARBORN ST,0460,BATTERY,SIMPLE,CTA PLATFORM,false,false,0113,001,42,32,08B,,,2019,06/07/2019 04:05:48 PM,,,,,,,,,,,  
11706901,JC287144,05/31/2019 11:53:00 PM,034XX N CLARK ST,1360,CRIMINAL TRESPASS,TO VEHICLE,SIDEWALK,true,false,1924,019,44,6,26,,,2019,06/07/2019 04:05:48 PM,,,,,,,,,,,  
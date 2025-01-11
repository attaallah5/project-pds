import multiprocessing
import pandas as pd 
import numpy as np  
import time
import requests
import json




ds = pd.read_csv("mobile_usage_behavioral_analysis.csv")
pd.set_option("display.max_rows", None) 
print(ds)

print("the median Gaming App Usage Hours: ",np.median(ds["Gaming_App_Usage_Hours"]))
print("the shape(r,c) is: ",np.shape(ds))
print(ds.dtypes)
print("Number of ELements",ds.size)
print(ds.describe())
print ( "the correlation between age and total app usage hours: ",ds['Total_App_Usage_Hours'].corr(ds['Age']) )
# print ( ds['Daily_Screen_Time_Hours'].isnull())it shows the null values for each row true while its null
# print ( ds['Age'].notnull()) it shows the not null values for each row true while its not null
ages= np.array([ds['Age']])
smuh=np.array([ds['Social_Media_Usage_Hours']])
combined_array = np.concatenate((ages, smuh),axis=0).T
df_CA=pd.DataFrame(combined_array, columns=['Age', 'Social_Media_Usage_Hours'])
print(df_CA)


print("number of logical processors: ",multiprocessing.cpu_count())

to_test= ds.select_dtypes(exclude='object')
print("applying the correlation on the dataset: \n ",to_test.corr())
for i in range(0,10):
    
    ds_json= json.dumps(ds['Daily_Screen_Time_Hours'][i])
    print(f"Daily Screen Time Hours for each user {i+1}: ",ds_json)
    

#turned the data set into json
#orient='records': This specifies the format of the JSON data. When orient='records' is used, each row of the DataFrame will be converted into a dictionary
#lines=True: This argument ensures that each record (dictionary) is written as a separate line in the file. 
ds.to_json("ds.json", orient='records', lines=True, index=False)
dataset_json = pd.read_json("ds.json", orient='records', lines=True)
print(dataset_json.head())

    


get_response =requests.get("https://www.kaggle.com/datasets/bhadramohit/smartphone-usage-and-behavioral-dataset")
print(get_response.status_code)
print(get_response.url)

# Code	Reason Phrase
# 200	OK
# 201	Created
# 204	No Content
# 301	Moved Permanently
# 302	Found
# 400	Bad Request
# 401	Unauthorized
# 403	Forbidden
# 404	Not Found
# 500	Internal Server Error
# 502	Bad Gateway
# 503	Service Unavailable
print(get_response.reason)
#It shows the total duration between when the request was sent and when the response was fully received.
print(get_response.elapsed)
print(get_response.text)





    














import pandas as pd
import numpy as np
import os
import yaml

df_processed = pd.read_csv("dataset/telecom.csv")

df_processed.drop(['area_code','phone_number'] , axis = 1 , inplace = True)
df_processed['international_plan'] = df_processed['international_plan'].map({'no' : 0 , 'yes' : 1})
df_processed['voice_mail_plan'] = df_processed['voice_mail_plan'].map({'no' : 0 , 'yes' : 1})

data_path = os.path.join("data","processed")

df_processed.to_csv(os.path.join(data_path , "data_processed.csv"))
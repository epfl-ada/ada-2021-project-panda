import os
import pandas as pd 
from glob import glob

def extract_gender(path_in = '/content/drive/MyDrive/ADA/Project_datasets/speaker_attributes.parquet',\
                   path_out = '/content/drive/MyDrive/ADA/Processed_datasets/Gender') : 
 
    # Find all the files absolute path
    path_parquet_files = path_in + '/part*'
    files = sorted(glob(path_parquet_files))

    # Here I filter only male and female speakers and write to csv files

    for f in files :
      df = pd.read_parquet(f, engine = 'pyarrow',columns = ['gender','id'])
      df_filtered = df[df['gender'].isin([['Q6581072'],['Q6581097']])]
      
      # Explicit M/F
      df_filtered.loc[df_filtered['gender'] == 'Q6581072']  = 'F'
      df_filtered.loc[df_filtered['gender'] == 'Q6581097'] = 'M'
      break

      df_filtered.to_csv(os.path.join(path_out, 'speakers-genders.csv'),\
                        compression = 'bz2',\
                        mode= 'a') # appending at then end of the file
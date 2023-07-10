import imdlib as imd
import pandas as pd


start_dy = '2020-07-06'
end_dy = '2020-07-09'
var_type = 'tmin'         # other options are ('tmin'/ 'tmax'/ 'rain')
file_dir=f'F:/imd_daily/test/{var_type}'
data = imd.get_real_data(var_type, start_dy, end_dy, file_dir)

ds = data.get_xarray()
# print(ds)
grouped_data = ds.groupby('time')

# Iterate over the groups
for date, group in grouped_data:
    # Convert the group to a DataFrame
    df = group.to_dataframe()
    df = df.drop(columns=['time'])
    # Extract the date as a string
    date_str = pd.to_datetime(date).strftime('%Y%m%d').replace('-', '')
    print(f"Processing for Date:{date_str}")
    csv_file = f'F:imd_daily/test_csv/{var_type}/{date_str}_{var_type}.csv'
    df.to_csv(csv_file)
print("CSV Generation Completed.")
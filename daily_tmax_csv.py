import imdlib as imd
import pandas as pd


start_dy = '2015-06-01'
end_dy = '2023-07-05'
var_type = 'tmax'
file_dir = 'F:/imd_daily/tmax/'

data = imd.open_real_data(var_type, start_dy, end_dy, file_dir)
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
    csv_file = f'F:imd_daily/tmax_csv/{date_str}_tmax.csv'
    df.to_csv(csv_file)
print("CSV Generation Complete")
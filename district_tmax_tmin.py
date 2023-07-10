import os
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
from geopandas.tools import sjoin
from time import perf_counter

t1 = perf_counter()
# Folder paths
shapefile_path = 'F:/imd_daily/updated_district/district.shp'
csv_folder = 'F:/imd_daily/tmax_csv/'
output_folder = 'F:/imd_daily/tmax_csv/'


shapefile = gpd.read_file(shapefile_path)
# print(shapefile.columns)
shapefile.sindex

for csv_file_name in os.listdir(csv_folder):
    # Check if the file is a CSV
    if csv_file_name.endswith('.csv'):
        # Extract the file name without extension
        csv_file_base = os.path.splitext(csv_file_name)[0]

        # Construct the corresponding CSV file path
        csv_file_path = os.path.join(csv_folder, csv_file_name)

        # Read the CSV file
        df = pd.read_csv(csv_file_path)

        # Create a GeoDataFrame from the DataFrame with lat/lon coordinates
        geometry = [Point(lon, lat) for lon, lat in zip(df['lon'], df['lat'])]
        crs = {'init': 'epsg:4326'}  # Define the coordinate reference system (CRS)
        gdf = gpd.GeoDataFrame(df, crs=crs, geometry=geometry)

        # Perform the spatial join
        joined_data = sjoin(gdf, shapefile, how="inner", op="within")
        columns_to_drop = ['geometry', 'index_right', 'State_LGD', 'DISTRICT_L', 'REMARKS']
        joined_data = joined_data.drop(columns=columns_to_drop)

        # Save the modified CSV file
        updated_csv_file_path = os.path.join(output_folder, f'{csv_file_base}.csv')
        joined_data.to_csv(updated_csv_file_path, index=False)

t2 = perf_counter()
print(f'Time Spent:{t2-t1}')

# Start to use pandas
import numpy as np
import pandas as pd
import googlemaps

def prepare_data(df):
    gmaps = googlemaps.Client(key = 'AIzaSyBsi0k8u9O0sPTLSpVZz5_24YWyg0l_0iY')

    for row in range(len(df)):
        try:
            lat = df.loc[row, 'Latitude']
            lang = df.loc[row, 'Longitude']

            return_results = gmaps.reverse_geocode(
            (lat,lang),
            location_type = "APPROXIMATE",
            result_type = "country",
            )

            address_components = return_results[0].get('address_components')
            results = address_components[0].get('long_name')
        except:
            results = "ERROR"

        df.loc[row, 'Country'] = results

    df_geo = pd.DataFrame(
        df, columns=['Vol_name', 'Sta_yr', 'Erup_dur', 'VEI', 'Latitude', 'Longitude', 'Country'])

    return df_geo

if __name__ == '__main__':
    new_original_file = "Cleaned_GVP_Eruption_Results.xlsx"
    df_original = pd.read_excel(
        new_original_file, sheet_name='Sheet1', skiprows=0)
    df_geo = prepare_data(df_original)

    print(df_geo.info(verbose=True))
    print(df_geo.head())

    df_geo.to_excel('Geo_Eruption_Results.xlsx', index=False)



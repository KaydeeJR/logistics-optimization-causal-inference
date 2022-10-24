from math import radians, cos, sin, asin, sqrt

class DataPreparation:
    """
    Performs feature engineering
    """
    def __init__(self) -> None:
        pass

    def get_hour_of_day(self, df_column):
        """
        Parameters: dataframe column of datatype datetime
        Returns: the hour of the day of the datetime object - 24 hour format
        """
        return df_column.hour

    def get_trip_duration(self, df_start_col, df_end_col):
        """
        calculate the time taken to complete an order
        Parameters: start datetime, end datetime 
        Returns: duration in minutes
        """
        time_diff = df_end_col - df_start_col
        return time_diff
    
    def get_trip_distance(self, df_origin_col, df_dest_col):
        """
        Parameters: origin coordinates, destination coordinates as object datatypes
        
        Returns: distance between the 2 points in Kilometers
        """ 
        # getting latitude and longitude
        origin_lat = float(df_origin_col.split(',')[0])
        origin_long = float(df_origin_col.split(',')[1])
        dest_lat = float(df_dest_col.split(',')[0])
        dest_long = float(df_dest_col.split(',')[1])
        # Using latitude and longitude (in degrees)
        # calculate the distance between two points on the earth

        # convert degrees to radians
        long_o = radians(origin_long)
        long_d = radians(dest_long)
        lat_o = radians(origin_lat)
        lat_d = radians(dest_lat)
        
        # Using the Haversine formula to calculate distance along a sphere
        dlon = long_d - long_o
        dlat = lat_d - lat_o
        arc_dist = sin(dlat / 2)**2 + cos(lat_o) * cos(lat_d) * sin(dlon / 2)**2

        c = 2 * asin(sqrt(arc_dist))
    
        # Radius of earth in kilometers
        r = 6371
        
        return(c * r) 

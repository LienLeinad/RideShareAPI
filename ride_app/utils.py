from math import asin, cos, radians, sin, sqrt

from django.db.models.functions import ASin, Cos, Radians, Sin, Sqrt


def haversine_db(lat1, lon1, lat2, lon2):
    """
    Calculate the great-circle distance between two points
    on a sphere given their longitudes and latitudes using Django DB functions.
    """

    # Earth's mean radius in kilometers
    r = 6371

    # Convert latitude and longitude from degrees to radians
    lat1_rad = Radians(lat1)
    lon1_rad = Radians(lon1)
    lat2_rad = Radians(lat2)
    lon2_rad = Radians(lon2)

    # Haversine formula
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad
    a = Sin(dlat / 2) ** 2 + Cos(lat1_rad) * Cos(lat2_rad) * Sin(dlon / 2) ** 2
    c = 2 * ASin(Sqrt(a))

    return c * r


# NOTE: implementing non-db version for testing
def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great-circle distance between two points
    on a sphere given their longitudes and latitudes.
    """
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))

    # Earth's mean radius in kilometers (can be adjusted for miles, etc.)
    r = 6371

    return c * r

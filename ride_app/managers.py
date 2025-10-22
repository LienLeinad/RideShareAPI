from django.db.models import F, FloatField, QuerySet, Sum

from ride_app.utils import haversine_db


class RideQuerySet(QuerySet):
    def annotate_driver_distance(self, longitude: float, latitude: float):
        return self.annotate(
            driver_distance=Sum(
                haversine_db(
                    lat1=latitude,
                    lon1=longitude,
                    lat2=F("pickup_latitude"),
                    lon2=F("pickup_longitude"),
                ),
                output_field=FloatField(),
            )
        )

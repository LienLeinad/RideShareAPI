import csv

from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = "Generates a CSV report of rides longer than 1 hour."

    def handle(self, *args, **options):
        self.stdout.write("Generating long rides report...")

        query = """
        SELECT
            DATE(ride.pickup_time) AS Month,
            driver_user.first_name || ' ' || driver_user.last_name AS Driver,
            COUNT(ride.id) AS 'Count of Trips > 1 hr'
        FROM
            ride_app_rideevent AS event
        INNER JOIN
            ride_app_ride AS ride ON event.ride_id = ride.id
        INNER JOIN
            ride_app_user AS driver_user ON ride.driver_id = driver_user.id
        WHERE
            event.description LIKE '%dropped off%'
            AND (
                strftime('%s', event.created_at) - strftime('%s', ride.pickup_time)
            ) > 3600
        GROUP BY
            Month,
            Driver;
        """

        with connection.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
            col_names = [desc[0] for desc in cursor.description]

        with open("long_rides_report.csv", "w", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(col_names)
            csv_writer.writerows(rows)

        self.stdout.write(
            self.style.SUCCESS("Successfully generated long_rides_report.csv")
        )

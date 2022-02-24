import random

from django.core.management.base import BaseCommand, CommandError
import requests

from statii.models import Statie


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        cookies = {
            "JSESSIONID": "",
            "ROUTEID": ""
        }

        response = requests.get("", cookies=cookies)
        print(response.status_code)

        json_obj = response.json()

        for element in json_obj['Routes'][0]["RouteStations"]:
            Statie.objects.create(nume=element["StationName"], long=random.randint(0, 100), lat=random.randint(0, 100))
            print(element["StationName"])



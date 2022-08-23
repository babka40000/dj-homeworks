import csv

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones_csv = list(csv.DictReader(file, delimiter=';'))

        for phone_csv in phones_csv:
            phone_desc = Phone(name=phone_csv['name'], image=phone_csv['image'], price=int(phone_csv['price']),
                               release_date=phone_csv['release_date'], lte_exists=phone_csv['lte_exists'],
                               slug=slugify(phone_csv['name'])
                               )
            phone_desc.save()

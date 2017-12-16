from __future__ import absolute_import, division, print_function, \
    with_statement
from peewee import *
from property_data.property_model import CachePropertyModel
from property_data.memory_cache_database import init_cache_database
from site_structure_dumper.data_parser import propertyParser
import logging


class dataStorer:
    def __init__(self, db_filename):
        self.db_filename = db_filename
        init_cache_database()

    def cache_json_response_to_memory(self, json_obj):
        if json_obj == []:
            return

        json_obj = json_obj['features']
        for feature_obj in json_obj:
            property_obj = feature_obj['properties']
            item = CachePropertyModel()
            property = propertyParser(property_obj)
            item.identificatie = property.get_woz_obj_identificatie()
            item.house_number = property.get_housenumber()
            item.house_number_ext = property.get_housenumber_ext()
            item.postcode = property.get_post_code()
            item.plaatsnaam = property.get_plaatsnaam()
            item.street = property.get_straat()
            item.price_2015 = "none"
            item.price_2016 = "none"
            item.bouwjaar = property.get_bouwjaar()
            item.gebruiksdoel = property.get_gebruiksdoel()
            item.oppervlakte = property.get_oppervlakte()
            try:
                item.save()
            except Exception as e:
                logging.info(e)
            del item

    def dump_memory_database_to_file_database(self):
        class BaseModel(Model):
            class Meta:
                database = SqliteDatabase(self.db_filename)

        class FilePropertyModel(BaseModel):
            identificatie = CharField(unique=True)
            house_number = CharField(null=True)
            house_number_ext = CharField(null=True)
            postcode = CharField(null=True)
            plaatsnaam = CharField(null=True)
            street = CharField(null=True)

            price_2015 = CharField(null=True)
            price_2016 = CharField(null=True)

            bouwjaar = CharField(null=True)
            gebruiksdoel = CharField(null=True)
            oppervlakte = CharField(null=True)

        db = SqliteDatabase(self.db_filename)
        db.connect()
        try:
            db.drop_tables([FilePropertyModel])
        except:
            pass
        db.create_tables([FilePropertyModel])
        db.close()

        for entry in CachePropertyModel.select():
            item = FilePropertyModel()
            item.identificatie = entry.identificatie
            item.house_number = entry.house_number
            item.house_number_ext = entry.house_number_ext
            item.postcode = entry.postcode
            item.plaatsnaam = entry.plaatsnaam
            item.street = entry.street
            item.price_2015 = entry.price_2015
            item.price_2016 = entry.price_2016
            item.bouwjaar = entry.bouwjaar
            item.gebruiksdoel = entry.gebruiksdoel
            item.oppervlakte = entry.oppervlakte
            item.save()
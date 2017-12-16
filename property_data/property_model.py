from __future__ import absolute_import, division, print_function, \
    with_statement
from peewee import *


class BaseModel(Model):
    class Meta:
        database = SqliteDatabase(":memory:")
        
class CachePropertyModel(BaseModel):
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
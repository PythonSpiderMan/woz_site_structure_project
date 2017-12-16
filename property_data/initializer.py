from __future__ import absolute_import, division, print_function, \
    with_statement
from peewee import *
from property_data.property_model import PropertyModel

# ------ Stt Unit Tests ------


def test_store_data():
    class BaseModel(Model):
        class Meta:
            database = SqliteDatabase("temp.db")

    class DBModel(BaseModel):
        identificatie = CharField(unique=True)
        house_number = CharField(null=True)
        house_number_ext = CharField(null=True)
        postcode = CharField(null=True)
        plaatsnaam = CharField(null=True)
        street = CharField(null=True)

        price_2015 = CharField(null=True)
        price_2016 = CharField(null=True)
        price_2017 = CharField(null=True)

        bouwjaar = CharField(null=True)
        gebruiksdoel = CharField(null=True)
        oppervlakte = CharField(null=True)

    db = SqliteDatabase("temp.db")
    db.connect()
    try:
        db.drop_tables([DBModel])
    except:
        pass
    db.create_tables([DBModel])
    db.close()

    init_cache_database()
    model = PropertyModel()
    model.identificatie = "10000"
    model.save()
    del model

    for entry in PropertyModel.select():
        new_model = DBModel()
        new_model.identificatie = entry.identificatie
        new_model.save()


# ------ End Unit Tests ------


# ------ Stt Interfaces ------


def init_cache_database():
    db = SqliteDatabase("temp1.db")
    db.connect()
    try:
        db.drop_tables([PropertyModel])
    except:
        pass
    db.create_tables([PropertyModel])
    db.close()


# ------ End Interfaces ------

from __future__ import absolute_import, division, print_function, \
    with_statement
from peewee import *
from property_data.property_model import CachePropertyModel

# ------ Stt Unit Tests ------


def test_store_data():
    init_cache_database()
    model = CachePropertyModel()
    if hasattr(model, "identificatie"):
        model.identificatie = "10000"
    model.save()
    del model

    entry = CachePropertyModel.select()[0]
    assert entry.identificatie == "10000"


# ------ End Unit Tests ------


# ------ Stt Interfaces ------


def init_cache_database():
    db = SqliteDatabase(":memory:")
    db.connect()
    # try:
    #     db.drop_tables([CachePropertyModel])
    # except:
    #     pass
    db.create_tables([CachePropertyModel], safe=True)
    db.close()




# ------ End Interfaces ------

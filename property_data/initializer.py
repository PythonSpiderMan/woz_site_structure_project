from __future__ import absolute_import, division, print_function, \
    with_statement
import requests
from peewee import *
import json
import numpy
import logging
from multiprocessing.dummy import Pool as ThreadPool
import threading
from property_data.property_model import PropertyModel


def init_database():
    db = SqliteDatabase("netherland_properties.db")
    db.connect()
    try:
        db.drop_tables([PropertyModel])
    except:
        pass
    db.create_tables([PropertyModel])
    db.close()
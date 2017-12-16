from __future__ import absolute_import, division, print_function, \
    with_statement
import logging


class propertyParser:
    @staticmethod
    def get_total_properties(json_obj):
        try:
            return len(json_obj['features'])
        except Exception as e:
            logging.error(e)
            logging.error("There is no features here")
            return 0

    def __init__(self, properties_obj):
        self.json_obj = properties_obj

    def get_woz_obj_identificatie(self):
        try:
            return self.json_obj['wobj_obj_id']
        except Exception as e:
            logging.error(e)
            logging.error("this building has no identification code. ")
            return "none"

    def get_housenumber(self):
        try:
            return self.json_obj['wobj_huisnummer']
        except Exception as e:
            logging.log("this building has no house number. ")
            return "none"

    def get_housenumber_ext(self):
        try:
            return self.json_obj['wobj_huisletter']
        except Exception as e:
            logging.info("this building has no house number extension")
            return "none"

    def get_post_code(self):
        try:
            return self.json_obj['wobj_postcode']
        except Exception as e:
            logging.info('this building has no postcode. ')
            return "none"

    def get_plaatsnaam(self):
        try:
            return self.json_obj['wobj_woonplaats']
        except Exception as e:
            logging.info(e)
            logging.info("this building has no plaatsnaam. ")
            return "none"

    def get_straat(self):
        try:
            return self.json_obj['wobj_straat']
        except Exception as e:
            logging.info(e)
            logging.info("this building has no street name. ")
            return "none"

    def get_bouwjaar(self):
        try:
            return self.json_obj['wobj_bag_bouwjaar']
        except Exception as e:
            logging.info(e)
            logging.info("this building has no bouwjaar. ")
            return "none"

    def get_gebruiksdoel(self):
        try:
            return self.json_obj['wobj_bag_gebruiksdoel']
        except Exception as e:
            logging.info(e)
            logging.info("this building has no gebruiksdoel. ")
            return "none"

    def get_oppervlakte(self):
        try:
            return self.json_obj['wobj_oppervlakte']
        except Exception as e:
            logging.info(e)
            logging.info("this building has no oppervlakte. ")
            return "none"

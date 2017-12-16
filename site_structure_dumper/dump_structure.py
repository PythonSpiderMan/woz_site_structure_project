from __future__ import absolute_import, division, print_function, \
    with_statement
import logging
from site_structure_dumper.utils import dumper_utils


# ------- Start Unit Tests -------


def test_basic_dump():
    try:
        obj = dump_properties_structure_from_id_to_id(15300024745, 15300025745)
        assert obj is not None
        assert len(obj['features']) > 10
    except ValueError as e:
        logging.error(e)
        logging.error("please update the code for parse obj id. ")
    except Exception as e:
        logging.error(e)
        logging.error("please update the code for scrapping objs. ")


# ------ End Unit Tests ------

def dump_properties_structure_from_id_to_id(from_id=-1, to_id=-1):
    f, t = from_id, to_id
    if f == -1 or t == -1:
        raise ValueError("Please pass from_id and to_id. ")

    f, t = dumper_utils.format_id_to_string(f, t)
    if f == -1 or t == -1:
        raise ValueError("from_id and to_id cannot be parsed. ")

    d = dumper(f, t)
    d.run()
    json_obj = d.response_obj()

    return json_obj

# ------ End Interfaces ------


class dumper:
    def __init__(self, from_id=None, to_id=None):
        self.f = from_id
        self.t = to_id
        xml_obj = \
            """
                    <wfs:GetFeature
                        xmlns:wfs="http://www.opengis.net/wfs" service="WFS" version="1.1.0" xsi:schemaLocation="http://www.opengis.net/wfs http://schemas.opengis.net/wfs/1.1.0/wfs.xsd"
                        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
                        <wfs:Query typeName="wozloket:woz_woz_object" srsName="EPSG:28992"
                            xmlns:WozViewer="http://WozViewer.geonovum.nl"
                            xmlns:ogc="http://www.opengis.net/ogc">
                            <ogc:Filter
                                xmlns:ogc="http://www.opengis.net/ogc">
                                <ogc:And>
                                    <ogc:PropertyIsGreaterThan matchCase="true">
                                        <ogc:PropertyName>wobj_obj_id</ogc:PropertyName>
                                        <ogc:Literal>%s</ogc:Literal>
                                    </ogc:PropertyIsGreaterThan>
                                    <ogc:PropertyIsLessThan matchCase="true">
                                        <ogc:PropertyName>wobj_obj_id</ogc:PropertyName>
                                        <ogc:Literal>%s</ogc:Literal>
                                    </ogc:PropertyIsLessThan>
                                </ogc:And>
                            </ogc:Filter>
                        </wfs:Query>
                    </wfs:GetFeature>
                    """
        self.xml_obj = xml_obj % (str(self.f), str(self.t))
        self.json_dict = 2

    def check_id(self):
        f = self.f
        t = self.t
        if f is None:
            raise Exception("From id is None, check the script please. ")
        if type(f) is not str:
            raise Exception("Please format id to string first. ")
        if t is None:
            raise Exception("To id is None, check the script please. ")
        if type(f) is not str:
            raise Exception("Please format id to string first. ")

    def post_request(self, socket):
        s = socket
        xml_obj = self.xml_obj
        from_id = self.f
        to_id = self.t
        response = int()
        try:
            response = s.post(url="https://www.wozwaardeloket.nl/woz-proxy/wozloket", data=xml_obj)
            print("scraping woz obj from id %s to id %s . " % (str(from_id), str(to_id)), end="\n")
        except Exception as e:
            logging.error(e)
            logging.error("request failed. ")
            logging.error("from_id=%s" % str(from_id))
            logging.error("to_id=%s" % str(to_id))
            response = 1
        return response

    def run(self):
        try:
            self.check_id()
        except Exception as e:
            logging.error(e)

        s = dumper_utils.init_request()
        while s == 1:
            logging.error("Request cannot be initiated, now retrying. ")
            s = dumper_utils.init_request()

        s_with_cookie = dumper_utils.request_cookie(s)
        while s_with_cookie == 1:
            logging.error("Error occurred on requesting cookies, now retrying. ")
            s_with_cookie = dumper_utils.request_cookie(s)

        response = self.post_request(s_with_cookie)
        while response == 1:
            logging.error("error occurred during start request, now trying restart the request.")
            response = self.post_request(s_with_cookie)
        del s_with_cookie

        json_dict = dumper_utils.parse_request_to_dict(response)
        if json_dict == 2:
            logging.error("this response can not be parsed. ")
        self.json_dict = json_dict

    def response_obj(self):
        if self.json_dict == 2:
            logging.error("this response is not valid. ")
            return None
        else:
            return self.json_dict



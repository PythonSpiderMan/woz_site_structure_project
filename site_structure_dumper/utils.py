from __future__ import absolute_import, division, print_function, \
    with_statement
import requests
import json
import logging
import unittest


# ------ Stt Unit Tests ------
class UnitTest(unittest.TestCase):
    def test_request_to_dict(self):
        assert dumper_utils.parse_request_to_dict(None) == 2

    def test_format_id_to_string(self):
        assert dumper_utils.format_id_to_string(10, 90) == ("000000000010","000000000090")

    def test_init_request(self):
        request_obj = dumper_utils.init_request()
        assert request_obj != 1

    def test_request_cookie(self):
        s = requests.Session()
        request_obj = dumper_utils.request_cookie(s)
        assert request_obj != 1
        s.close()

# ------ End Unit Tests ------


class dumper_utils:
    @staticmethod
    def parse_request_to_dict(response):
        text_response = response
        if not hasattr(text_response, "text"):
            logging.error("this response has no text attribute. ")
            # raise ValueError("This is not a valid response. ")
            return 2

        json_obj = int()
        try:
            json_obj = json.loads(text_response.text)
        except Exception as e:
            logging.error("Error occured when parsing response to json object. ")
            # raise ValueError("This is not a valid response")
            json_obj = 2
        return json_obj

    @staticmethod
    def format_id_to_string(f, t):
        from_id = int()
        to_id = int()
        try:
            from_id = str('%012d' % f)
            to_id = str('%012d' % t)
        except Exception as e:
            logging.error(e)
            logging.error("error occurred when formating from_id and to_id, make sure these are integers")
            logging.error("from_id: %s" % str(from_id))
            logging.error("to_id: %s" % str(to_id))
        return from_id, to_id


    @staticmethod
    def init_request():
        s = int()
        try:
            s = requests.Session()
            proxies = dict(http='socks5://127.0.0.1:1080',
                                 https='socks5://127.0.0.1:1080')
            s.proxies.update(proxies)
        except Exception as e:
            logging.error(e)
            logging.error("network may exploding, cannot initiate a request now. ")
            s = 1
        return s


    @staticmethod
    def request_cookie(request):
        s = int(1)
        try:
            request.get("https://www.wozwaardeloket.nl/index.jsp?a=1&accept=true&")
            s = request
        except Exception as e:
            logging.error(e)
            logging.error("Please fix your network connection status immediately")
            logging.error("the script will wait for you about 10 seconds :< ")
            s = 1
        return s

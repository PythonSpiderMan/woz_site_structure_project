from site_structure_dumper import data_scrapper, data_storer


def test_scrape_woz_objs_to_file():
    storer = data_storer.dataStorer(db_filename="temp.db")

    obj = data_scrapper.dump_properties_structure_from_id_to_id(3, 2)
    storer.cache_json_response_to_memory(obj)

    obj = data_scrapper.dump_properties_structure_from_id_to_id(15300024745, 20000000)
    storer.cache_json_response_to_memory(obj)

    storer.dump_memory_database_to_file_database()

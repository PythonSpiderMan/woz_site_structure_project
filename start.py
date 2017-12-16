from site_structure_dumper import data_scrapper, data_storer
from multiprocessing.dummy import Pool as ThreadPool


def scrape_range_to_cache(index):
    global storer
    step = 5000
    obj = data_scrapper.dump_properties_structure_from_id_to_id(index*step+1, ((index+1)*step)+2)
    storer.cache_json_response_to_memory(obj)
    print("scrape range from %s to %s" % (str(index*step+1), str((index+1)*step)+2))


if __name__ == '__main__':
    global storer
    storer = data_storer.dataStorer(db_filename="temp.db")


    total_steps = range(8000000, 200000000)
    # total_steps = range(0, 200000000)
    objects_total = len(total_steps)

    chunks = [total_steps[x:x + 1000] for x in range(0, len(total_steps), 1000)]
    for each_chunk in chunks:
        pool = ThreadPool(1000)
        pool.map(scrape_range_to_cache, each_chunk)
        pool.close()
        pool.join()

    storer.dump_memory_database_to_file_database()

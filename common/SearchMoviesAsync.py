import multiprocessing as mp
import time
from common.Movie import Movie
from imdbpie import Imdb

def foo_pool(x):
    time.sleep(2)
    return x*x

result_list = []
def log_result(result):
    # This is called whenever foo_pool(i) returns a result.
    # result_list is modified only by the main process, not the pool workers.
    result_list.append(result)

def apply_async_with_callback():
	pool = Pool(processes=1) 
		imdb = Imdb()
		dict=imdb.search_for_title(value)
		movies = []
		for m in dict:
			if (m['type']!=None):
					pool.apply_async(Movie, args = (m['imdb_id'], ), callback = movies.append)
		return movies
	
    pool = mp.Pool()
	imdb = Imdb()
	dict=imdb.search_for_title(value)
	for m in dict:
				if (m['type']!=None):
						pool.apply_async(Movie, args = (m['imdb_id'], ), callback = movies.append)
    pool.close()
    pool.join()
    print(result_list)

if __name__ == '__main__':
    apply_async_with_callback()
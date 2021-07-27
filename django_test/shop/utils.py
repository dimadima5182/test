import functools
from time import perf_counter
from django.db import reset_queries
from django.db import connection


def query_debugger(func):
    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        reset_queries()
        start_queries = len(connection.queries)

        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()

        end_queries = len(connection.queries)
        print(f'Query_count : {end_queries - start_queries}')
        print(f'Function : {func.__name__}')
        print(f'Finished in : {(end - start):.2f}s')
        return result

    return inner_func
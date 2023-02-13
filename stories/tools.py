import gevent


def get_all(task, urls):
    def do_request(url):
        task.client.get(url)

    pool = gevent.pool.Pool()

    for url in urls:
        pool.spawn(do_request, url)
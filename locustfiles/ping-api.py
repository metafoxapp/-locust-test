from locust import HttpUser, between, task


class PingApi(HttpUser):
    wait_time = between(3, 5)

    @task(1)
    def ping(self):
        with self.client.get('/api/v1/ping') as res:
            pass

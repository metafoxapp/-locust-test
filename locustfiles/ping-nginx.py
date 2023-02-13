from locust import HttpUser, between, task


class PingNginx(HttpUser):
    wait_time = between(1, 3)

    @task(1)
    def ping(self):
        with self.client.get('/nginx-ping') as res:
            pass

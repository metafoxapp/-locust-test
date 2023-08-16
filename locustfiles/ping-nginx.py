from locust import HttpUser, between, task, constant


class PingNginx(HttpUser):
    wait_time = between(3, 5)

    @task(1)
    def ping(self):
        with self.client.get('/nginx-ping') as res:
            pass

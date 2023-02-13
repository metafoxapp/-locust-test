from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from locust import TaskSet, task


class LocustUserBehavior(TaskSet):

    def open_home_page(self):
        self.client.get("/")
        self.client.wait.until(EC.visibility_of_element_located((By.XPATH, '//a[text()="Documentation"]')),
                               "documentation link is visible")

    def click_through_to_documentation(self):
        self.client.find_element_by_xpath('//a[text()="Documentation"]').click()
        self.client.wait.until(EC.visibility_of_element_located((By.XPATH, '//h1[text()="Locust Documentation"]')),
                               "documentation is visible")

    @task(1)
    def homepage_and_docs(self):
        self.client.timed_event_for_locust("Go to", "homepage", self.open_home_page)
        self.client.timed_event_for_locust("Click to", "documentation", self.click_through_to_documentation)

    def stop(self):
        self.interrupt()
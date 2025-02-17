from locust import HttpUser, between, task, constant

from common.auth import pick_random_user


class GuestVisitSite(HttpUser):
    wait_time = between(3, 5)

    @task(5)
    def guest_visit_homepage(self):
        self.client.get('/api/v1/core/translation/web/auto/now')
        self.client.get('/api/v1/core/web/settings/now')

    @task(2)
    def app_blogs(self):
        self.client.get('/api/v1/blog')
        self.client.get('/api/v1/blog?view=feature')
        self.client.get('/api/v1/blog-category')
        self.client.get('/api/v1/blog?sort=most_viewed')
        self.client.get('/api/v1/blog?category_id=1&view=search')

    @task(2)
    def app_events(self):
        self.client.get('/api/v1/event-category')
        self.client.get('/api/v1/event?sort=most_interested')
        self.client.get('/api/v1/event?sort=recent&view=interested')
        self.client.get('/api/v1/event?sort=recent&view=going')
        self.client.get('/api/v1/event?limit=6&view=feature')
        self.client.get('/api/v1/event?sort=recent&view=going')
        self.client.get('/api/v1/event?sort=recent&view=interested')
        self.client.get('/api/v1/event')
        self.client.get('/api/v1/event?user_id=1&when=upcoming')
        self.client.get('/api/v1/event?sort=end_time&view=related&when=past')
        self.client.get('/api/v1/event?category_id=1&view=search')

    @task(5)
    def app_feed(self):
        self.client.get('/api/v1/feed/check-new?last_feed_id=1')
        self.client.get('/api/v1/feed?view=latest')

    @task(10)
    def app_groups(self):
        self.client.get('/api/v1/group/category')
        self.client.get('/api/v1/group?limit=6&view=feature')
        self.client.get('/api/v1/group?sort=most_member')
        self.client.get('/api/v1/group')
        self.client.get('/api/v1/group?category_id=10&view=search')
        self.client.get('/api/v1/group?q=Knowledge&category_id=10&view=search')
        self.client.get('/api/v1/group?q=Knowledge&when=this_month&category_id=10&view=search')

    @task(5)
    def announcements(self):
        self.client.get('/api/v1/announcement')

    @task(5)
    def feeds(self):
        self.client.get('/api/v1/feed?view=latest&last_feed_id=54')

    @task(5)
    def next_feeds(self):
        self.client.get('/api/v1/feed?view=latest&last_feed_id=100&page=2')

    @task(2)
    def app_marketplace(self):
        self.client.get('/api/v1/marketplace-category')
        self.client.get('/api/v1/marketplace?view=feature')
        self.client.get('/api/v1/marketplace?sort=most_viewed')
        self.client.get('/api/v1/marketplace?view=all')
        self.client.get('/api/v1/marketplace?category_id=1&view=search')

    @task(2)
    def app_pages(self):
        self.client.get('/api/v1/page?sort=most_member')
        self.client.get('/api/v1/page/category')
        self.client.get('/api/v1/page?limit=6&view=feature')
        self.client.get('/api/v1/page')
        self.client.get('/api/v1/page?category_id=10&view=search')
        self.client.get('/api/v1/page?q=Knowledge&category_id=10&view=search')
        self.client.get('/api/v1/page?q=Knowledge&when=this_month&category_id=10&view=search')

    @task(5)
    def app_photos(self):
        self.client.get('/api/v1/photo?limit=6&view=feature')
        self.client.get('/api/v1/photo-category')

        self.client.get('/api/v1/photo-album')
        self.client.get('/api/v1/photo-album?limit=6&view=feature')

    @task(1)
    def app_poll(self):
        self.client.get('/api/v1/poll?view=search')
        self.client.get('/api/v1/poll')
        self.client.get('/api/v1/poll?view=feature')
        self.client.get('/api/v1/poll?sort=most_viewed')
        pass

    @task(1)
    def app_quiz(self):
        self.client.get('/api/v1/quiz?view=search')
        self.client.get('/api/v1/quiz')
        self.client.get('/api/v1/quiz?view=feature')
        self.client.get('/api/v1/quiz?sort=most_played')

    @task(1)
    def app_browse_users(self):
        self.client.get('/api/v1/user')
        self.client.get('/api/v1/user?view=recommend')
        self.client.get('/api/v1/user?view=recent')
        self.client.get('/api/v1/user?view=featured')

    @task(1)
    def view_user(self):
        user_id = pick_random_user().get('id')
        self.client.get('/api/v1/user/' + user_id)
        self.client.get('/api/v1/feed?user_id=' + user_id)
        self.client.get('/api/v1/photo?sort=latest&user_id=' + user_id)
        self.client.get('/api/v1/user/info/' + user_id)

        self.client.get('/api/v1/video?limit=12&sort=recent&user_id=' + user_id)
        self.client.get('/api/v1/page?limit=12&sort=latest&user_id=' + user_id)
        self.client.get('/api/v1/marketplace?user_id=' + user_id)
        self.client.get('/api/v1/blog?user_id=' + user_id)
        self.client.get('/api/v1/poll?user_id=' + user_id)
        self.client.get('/api/v1/quiz?user_id=' + user_id)
        self.client.get('/api/v1/video?user_id=' + user_id)
        self.client.get('/api/v1/event?user_id=' + user_id)
        self.client.get('/api/v1/forum-thread?user_id=' + user_id)

    @task(1)
    def browse_videos(self):
        self.client.get('/api/v1/video/category')
        self.client.get('/api/v1/video?view=feature')
        self.client.get('/api/v1/video?sort=most_viewed')
        self.client.get('/api/v1/video')
        self.client.get('/api/v1/video?category_id=1&view=search')

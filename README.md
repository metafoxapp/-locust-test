# Load Test


## Initial Server

**database server**

8 cores CPU x AMD EPYC Processor
16 GB RAM

**app server**

8 cores CPU x AMD EPYC Processor
16 GB RAM


**Load test database**

```txt
activity_post .......................................................................................... 332,360
announcement ............................................................................................. 5,000
blog ................................................................................................... 332,194
comment ................................................................................................ 332,062
event .................................................................................................... 8,328
forum_post ............................................................................................. 100,005
forum_thread ............................................................................................. 5,000
group .................................................................................................... 8,356
marketplace ............................................................................................ 100,000
music_album ............................................................................................ 212,168
music_playlist ......................................................................................... 212,156
music_song ............................................................................................. 212,155
page ................................................................................................... 100,097
photo .................................................................................................. 532,153
photo_album ............................................................................................ 212,126
poll ................................................................................................... 172,189
quiz .................................................................................................... 20,000
user ................................................................................................... 100,000
video .................................................................................................. 212,107
feed ................................................................................................. 1,458,761
Total ................................................................................................ 4,667,217
```

## Scenarios

### For logged in user

User spend time is 5 and 15 seconds between each step

- User login
- User visit /
- User Visit /activitypoint
- User Visit /blog
- User Visit /event
- User post a new event
- User visit / again
- User check if new feed
- User post a new feed with background status
- User post a new checkin status
- User create a new poll
- User visit /friend
- User create a new friend list
- User visit /groups
- User post a new group
- User check if new notifications
- User mark all notification is read
- User scroll home page down to load more feeds 2 times
- User edit their shortcuts
- User visit marketplaces
- User visit /pages
- User add new page
- User visit app /photo
- User visit app /poll
- User post a new poll
- User visit /quiz
- User post a new quiz
- User visit their saved at /
- User add new saved collections
- User visit there account settings, notification settings, ...
- User browse site members
- User browse site videos
- User browse forum post
- User reply forum post


## Results

### Stage 00 - No Optimize

- [Metrics](/apm-results/v5.1.3-stage-00.md)

### Stage 01 - Apply Preload

In this stages

- Support command `php artisan preload:gen` to update preload.php from opcache status scripts.
- Optimize Docker Image with smaller size and extensions. [Docker Image](https://hub.docker.com/layers/foxsystem/metafox-fpm/prod/images/sha256-720d836b0ceb614173b03ae08cdef4c1e110d1ca2b4064057035a8557e595223?context=repo)
- [Implement Opcache Preloading](https://www.php.net/manual/en/opcache.preloading.php)
- [Metrics](/apm-results/v5.1.3-stage-01.md)
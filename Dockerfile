FROM locustio/locust:2.15.1
RUN pip3 install graphqlclient faker Jinja2 realbrowserlocusts  selenium


ENTRYPOINT ["/bin/sh","/home/locust/start.sh"]
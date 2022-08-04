FROM python:3.7


RUN mkdir -p /test_app/logs
ADD ./setup.py /test_app//setup.py
RUN python3 /test_app/setup.py install

ADD . /test_app
RUN chmod -v +x /test_app/docker/entry.sh

WORKDIR /test_app

CMD ["/test_app/docker/entry.sh" ]

FROM python:3.7-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install -r requirements.txt

ADD entrypoint.sh /
ADD src /src
ADD action.yaml /

ENTRYPOINT ["/entrypoint.sh"]


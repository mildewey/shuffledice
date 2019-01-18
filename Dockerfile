FROM python:3.7

# install prerequisites
RUN pip install pipenv
COPY Pipfile ./
RUN pipenv lock -r > requirements.txt
RUN pip install -r requirements.txt

WORKDIR /config
ENV SHUFFLEDICE_CONF_DIR /config
COPY config .

VOLUME /var/shuffledice/logs

WORKDIR /code
COPY shuffledice .
EXPOSE 8080

ENTRYPOINT ["python"]
CMD ["main.py"]

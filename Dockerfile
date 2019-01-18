FROM python:3.7

# install prerequisites
WORKDIR /code
RUN pip install pipenv
COPY Pipfile ./
RUN pipenv lock -r > requirements.txt
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8080

ENTRYPOINT ["python"]
CMD ["shuffledice/main.py"]

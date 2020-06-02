FROM python:3.7

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["/usr/local/bin/evennia"]
CMD ["start", "-l"]
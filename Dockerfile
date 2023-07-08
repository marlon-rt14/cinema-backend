FROM python:3.11.4-alpine3.17
WORKDIR /code
COPY . .

ENV MYSQL_USERNAME=root
ENV MYSQL_PASSWORD=marlon
ENV MYSQL_DATABASE=cinemadb
ENV MYSQL_HOSTNAME=cinema
ENV MYSQL_PORT=3306
ENV SECRET_KEY=whoismarlon

RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD ["python3", "/src/index.py"]
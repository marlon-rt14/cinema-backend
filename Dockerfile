FROM python:3.11.1
WORKDIR /code
COPY . .

ENV MYSQL_USERNAME=root
ENV MYSQL_PASSWORD=marlon
ENV MYSQL_DATABASE=cinema
ENV MYSQL_HOSTNAME=192.168.0.107
ENV MYSQL_PORT=3306
ENV SECRET_KEY=whoismarlon

RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "./src/index.py"]
FROM alpine:latest

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

WORKDIR /flask_app

COPY . .

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 50000

ENTRYPOINT ["python3"]
CMD ["app.py"]



FROM python:alpine

WORKDIR /app

RUN apk add --no-cache build-base musl-dev linux-headers

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN apk del build-base musl-dev linux-headers

COPY src/ /app/src/

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "src.app:app"]

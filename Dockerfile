FROM python:3.9-slim

WORKDIR /

RUN pip install flask

COPY . .

EXPOSE 5000

CMD ["python3", "app.py"]

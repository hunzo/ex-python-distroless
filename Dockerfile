FROM python:3.10-slim as venv

COPY requirements.txt .
RUN pip install --disable-pip-version-check -r requirements.txt 

FROM gcr.io/distroless/python3

COPY --from=venv /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
ENV PYTHONPATH=/usr/local/lib/python3.10/site-packages

WORKDIR /app
COPY . /app

CMD ["server.py"]

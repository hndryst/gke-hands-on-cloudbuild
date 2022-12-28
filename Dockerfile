FROM python:3.10.9-slim-bullseye
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY rest.py .
CMD ["python3", "rest.py"]
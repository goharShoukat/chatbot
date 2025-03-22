
FROM python:3.11-slim-bookworm


WORKDIR /usr/src/app

COPY requirements.txt .


RUN pip install --no-cache-dir --upgrade -r requirements.txt


COPY backend .


CMD ["fastapi", "run", "app/main.py", "--port", "80"]
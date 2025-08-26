FROM python:3.12-slim

WORKDIR /app
COPY game.py /app/

ENV PYTHONUNBUFFERED=1

CMD ["python", "game.py"]

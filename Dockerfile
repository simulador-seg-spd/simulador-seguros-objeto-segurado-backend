FROM python:3.12-alpine

WORKDIR /backend

ENV WORKERS=2 \
  THREADS=10 \
  PORT_APP=8080 \
  TZ=America/Sao_Paulo \
  PROJ_DIR=/usr



COPY . /backend
RUN pip install -r requirements.txt

EXPOSE 8080

CMD gunicorn --workers $WORKERS \
  --threads $THREADS \
  --bind 0.0.0.0:$PORT_APP \
  --log-level debug \
  app:app
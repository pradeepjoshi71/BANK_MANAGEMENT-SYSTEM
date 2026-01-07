FROM python:3.10-slim

WORKDIR /app

COPY BACKEND /app/BACKEND
COPY FRONTEND /app/FRONTED
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["pyton","app.py"]



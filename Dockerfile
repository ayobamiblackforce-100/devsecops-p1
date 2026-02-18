FROM python:3.10.19-slim-trixie

WORKDIR /app/

COPY /app/* /app/

RUN pip install -r requirements.txt

CMD ["streamlit", "run", "app.py"]

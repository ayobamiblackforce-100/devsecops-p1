FROM python:3.10.19-slim-trixie

WORKDIR /app/

COPY ./requirements.txt /app/

COPY ./app.py /app/

RUN pip install -r requirements.txt

CMD ["streamlit", "run", "app.py"]

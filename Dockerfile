FROM python:3.10.0
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"] # debug mode
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
FROM python:3.8.8-slim
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
EXPOSE 80
COPY mysql_alchemy/ /app
WORKDIR /app
CMD ["python", "main.py"]
FROM python:slim
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY app.py .
ENTRYPOINT ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
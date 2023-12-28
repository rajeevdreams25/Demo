
FROM python:3.8-slim

# ADD main.py .

ADD main.py .


RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80


# ENV NAME World


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

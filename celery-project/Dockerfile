FROM python:3.9.17  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUNBUFFERED=1

WORKDIR /
COPY /proj /proj
COPY requirements.txt ./  
RUN pip install --no-cache-dir -r requirements.txt  
RUN rm requirements.txt  

ENTRYPOINT celery -A proj worker --loglevel=INFO
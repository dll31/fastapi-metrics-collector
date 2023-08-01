FROM python:3.9.17  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUNBUFFERED=1

WORKDIR /  
COPY requirements.txt ./  
RUN pip install --no-cache-dir -r requirements.txt  
RUN rm requirements.txt  

COPY main.py /code/ 
WORKDIR /code/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
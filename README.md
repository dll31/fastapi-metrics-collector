# fastapi-metrics-collector
Collecting metrics to Prometheus from fastapi application and Celery using prometheus-client, celery flower and celery-exporter by danihodovic.

# Run
docker-compose up

# Check metrics in Prometheus expression 
## fastapi
my_requests_total (after visited localhost:8000)

## Celery 
### using Flower
flower_worker_online
all Flower metrics available here: https://flower.readthedocs.io/en/latest/prometheus-integration.html#available-metrics
### using celery-exporter
celery_worker_up
all celery-exporter metrics available here: https://github.com/danihodovic/celery-exporter/tree/master#metrics

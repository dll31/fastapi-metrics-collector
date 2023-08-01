from fastapi import FastAPI, Response
from prometheus_client import CollectorRegistry, Counter
import prometheus_client
import uvicorn


app = FastAPI()


class MetricsCollector():
    registry = CollectorRegistry()
    my_requests_total = Counter('my_requests_total', 'HTTP Failures', ['method', 'endpoint'], registry=registry)

    def __init__(self):
        pass

    
    
collector = MetricsCollector()

@app.get("/")
async def root():
    collector.my_requests_total.labels('get', '/').inc()
    return {"message": "Root page"}

@app.get('/hello_world')
async def hello():
    collector.my_requests_total.labels('get', '/hello_world').inc()
    return {"message": "Hello world"}


@app.get('/bye_world')
async def bye():
    collector.my_requests_total.labels('get', '/bye_world').inc()
    return {"message": "Bye world"}

@app.get('/metrics')
def metrics():
    return Response(
        prometheus_client.generate_latest(registry=collector.registry), 
        media_type=prometheus_client.CONTENT_TYPE_LATEST,        
    )


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        port=8000,
        reload=True
    )

    

    
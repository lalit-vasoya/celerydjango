from celery import Celery

app = Celery('priodic_tasks',broker="amqp://guest:guest@localhost:5672//", backend='db+postgresql://postgres:postgres@localhost/celerydemo')

total = 0

@app.task
def check():
    global total
    if total>1:
        print('Greate then 10')
    else:
        print(f'Less then 10 {total}')
    total+=1
    return total

app.conf.beat_schedule = {
    'check-every-10-seconds': {
        'task': 'priodic_task.check',
        'schedule': 10.0,
	'args':[],
    },
}


app.conf.timezone = 'UTC'

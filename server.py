from sanic import Sanic
from sanic import response
import asyncio
import redis

app = Sanic(__name__)
app.redis_con = redis.StrictRedis(host="redis", port=6379, db=0, decode_responses=True)

def cache_set(key, val):
    app.redis_con.set(key, val)

def cache_get(key, df_val = None):
    result = app.redis_con.get(key)

    if result is None and df_val is not None:
        cache_set(key, df_val)
        result = df_val

    return result

@app.route('/')
async def index(request):
    url = app.url_for('count')
    return response.redirect(url)

@app.route('/add_task')
async def add_task(request):
    id = cache_get('task:count', 0)
    app.redis_con.incr('task:count')

    cache_set(f'task:{id}', 'rodando')

    await asyncio.sleep(10)
    return response.text(f'Id Task -> {id}')

@app.route('/count')
async def count(request):
    tot = cache_get('task:count', 0)
    return response.text(f'Total de Tasks -> {tot}')

@app.route('/query/<task_id:int>', methods=['GET', 'POST'])
async def query(request, task_id):
    status = cache_get(f'task:{task_id}', df_val = 'não encontrado')

    return response.text(status)
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
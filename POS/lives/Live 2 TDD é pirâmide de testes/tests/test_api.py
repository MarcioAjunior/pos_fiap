import pytest
from httpx import AsyncClient
from app import app #Resolver o problema do módulo

@pytest.mark.asyncio
async def test_read_tasks():
    async with AsyncClient(app=app, base_url='https://127.0.0.1:8000') as ac:
        response = await ac.get('/tasks')
        assert response.status_code == 200
        assert response.json() == {'tasks' : []}
        
        
#Tarefinha
#Criar o test de create

#Criar test de delete

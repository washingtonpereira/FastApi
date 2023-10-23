from fastapi import FastAPI
from fastapi  import HTTPException
from fastapi import status
from models import Produto
import uvicorn



app = FastAPI(title="Lista de Produtos")



produtos = {
    1:{
        "name":"Damasco",
        "price":79.90
    },
    2:{
        "name":"Goma de Tapioca",
        "price":6.30

    }
    
}


@app.get('/produtos')
async def get_produtos():
    return produtos



#Pegando apenas um produto da Api
@app.get('/produtos/{produto_id}')
async def get_produto(produto_id: int):
    try:
        produto = produtos[produto_id]
        return produto
    except KeyError:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='produto não encontrado.')
    

#Inserindo produtos
@app.post('/produtos',status_code=status.HTTP_201_CREATED)
async def post_produto(produto: Produto):
     next_id: int = len(produtos) + 1
     produtos[next_id] = produto
     del produto.id
     return produto
     


@app.put('/produtos/{produto_id}')
async def put_produto(produto_id: int, produto: Produto):
     if produto_id in produtos:
          produtos[produto_id] = produto 
          del produto.id

          return produto
     else:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Produto ou id não existe{produto_id}')    
    


@app.delete('/produtos/{produto_id}')
async def delete_produto(produto_id: int):
     if produto_id in produtos:
          del produtos[produto_id]

     else:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'produto ou id nao existe{produto_id}')     
     
"""if __name__ =='__main__':
    import uvicorn
    
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
"""
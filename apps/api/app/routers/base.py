from abc import ABC
from fastapi.routing import APIRouter

class BaseRouter(ABC):
    
    def __init__(self, router) -> None:
        self.__router = router
    
    @property
    def router(self):
        return self.__router
    
    def get(self, *args, **kwargs):
        return self.__router.get(*args, **kwargs)
    
    def patch(self, *args, **kwargs):
        return self.__router.patch(*args, **kwargs)
    
    def post(self, *args, **kwargs):
        return self.__router.post(*args, **kwargs)
    
    def put(self, *args, **kwargs):
        return self.__router.put(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        return self.__router.delete(*args, **kwargs)
    
    def put(self, *args, **kwargs):
        return self.__router.put(*args, **kwargs)
    
    def options(self, *args, **kwargs):
        return self.__router.options(*args, **kwargs)
    
    def head(self, *args, **kwargs):
        return self.__router.head(*args, **kwargs)
    
    def trace(self, *args, **kwargs):
        return self.__router.trace(*args, **kwargs)
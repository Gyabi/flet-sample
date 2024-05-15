from typing import TypeVar, Generic, Callable

T = TypeVar('T')

class State(Generic[T]):
    def __init__(self, value: T) -> None:
        self._value = value
        self._observers: list[Callable]  = []
        
    def get(self) -> T:
        return self._value
    
    def set(self, value: T) -> None:
        self._value = value
        self.notify()
        
    def notify(self) -> None:
        for observer in self._observers:
            observer()
            
    def bind(self, observer: Callable) -> None:
        self._observers.append(observer)
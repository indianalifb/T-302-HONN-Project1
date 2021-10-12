from abc import ABC, abstractmethod



class IGamemodeCreator(ABC): 
    @abstractmethod
    def factory_method(self): 
        pass
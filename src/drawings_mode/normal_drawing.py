from src.drawings_mode.Idrawing import Idrawing
from src.drawings_catagories.animal_normal import AnimalNormal


class NormalDrawing(Idrawing):

    def create_animal(self,false_number):
        return AnimalNormal.draw_animal(false_number)

    
    def create_food():
        pass


    def create_country():
        pass


from src.drawings_catagories.countries_normal import CountriesNormal
from src.drawings_catagories.food_normal import FoodNormal
from src.drawings_mode.Idrawing import Idrawing
from src.drawings_catagories.animal_normal import AnimalNormal


class NormalDrawing(Idrawing):
    #return the correct class /animal/food/country normal mode
    def create_animal(self):
        return AnimalNormal()

    
    def create_food(self):
        return FoodNormal()


    def create_country(self):
        return CountriesNormal()


from src.drawings_mode.Idrawing import Idrawing
from src.drawings_catagories.animal_competitive import AnimalCompetitive
from src.drawings_catagories.food_competitve import FoodCompetitive
from src.drawings_catagories.countries_competitive import CountriesCompetitive

class CompetitveDrawing(Idrawing):
    #return the correct class /animal/food/country competitive mode
    def create_animal(self):
        return AnimalCompetitive()

    def create_food(self):
        return FoodCompetitive()

    def create_country(self):
        return CountriesCompetitive()


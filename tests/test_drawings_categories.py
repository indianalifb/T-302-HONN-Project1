import pytest
from unittest.mock import Mock, MagicMock
from unittest.mock import patch, call

from src.drawings_catagories.animal_competitive import AnimalCompetitive
from src.drawings_catagories.animal_normal import AnimalNormal
from src.drawings_catagories.countries_competitive import CountriesCompetitive
from src.drawings_catagories.countries_normal import CountriesNormal
from src.drawings_catagories.food_competitve import FoodCompetitive
from src.drawings_catagories.food_normal import FoodNormal


@patch('builtins.print')
def test_that_tests_first_stage_of_animal_normal(mocked_print):
    # Arrange
    animal_normal = AnimalNormal()

    animal_normal.draw_animal(1)
    assert mocked_print.mock_calls == [call("#                                                 #"),
                                       call("#                                                 #"),
                                       call("#                                                 #"),
                                       call("#                                                 #"),
                                       call("#                                                 #"),
                                       call("#                                                 #"),
                                       call("#                                                 #"),
                                       call("#                                                 #"),
                                       call("#                                                 #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_second_stage_of_animal_normal(mocked_print):
    # Arrange
    animal_normal = AnimalNormal()

    animal_normal.draw_animal(2)
    assert mocked_print.mock_calls == [call("#                                 +               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_third_stage_of_animal_normal(mocked_print):
    # Arrange
    animal_normal = AnimalNormal()

    animal_normal.draw_animal(3)
    assert mocked_print.mock_calls == [call("#               +-----------------+               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_fourth_stage_of_animal_normal(mocked_print):
    # Arrange
    animal_normal = AnimalNormal()

    animal_normal.draw_animal(4)
    assert mocked_print.mock_calls == [call("#               +-w---------------+               #"),
                                       call("#                  \              |               #"),
                                       call("#                   \__           |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_fifth_stage_of_animal_normal(mocked_print):
    # Arrange
    animal_normal = AnimalNormal()

    animal_normal.draw_animal(5)
    assert mocked_print.mock_calls == [call("#               +-w---------------+               #"),
                                       call("#                  \  c(..)o      |               #"),
                                       call("#                   \__(-)        |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_sixth_stage_of_animal_normal(mocked_print):
    # Arrange
    animal_normal = AnimalNormal()

    animal_normal.draw_animal(6)
    assert mocked_print.mock_calls == [call("#               +-w---------------+               #"),
                                       call("#                  \  c(..)o      |               #"),
                                       call("#                   \__(-)        |               #"),
                                       call("#                       /         |               #"),
                                       call("#                      /          |               #"),
                                       call("#                     w           |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_seventh_stage_of_animal_normal(mocked_print):
    # Arrange
    animal_normal = AnimalNormal()

    animal_normal.draw_animal(7)
    assert mocked_print.mock_calls == [call("#               +-w---------------+               #"),
                                       call("#                  \  c(..)o      |               #"),
                                       call("#                   \__(-)        |               #"),
                                       call("#                       /\        |               #"),
                                       call("#                      /(_)       |               #"),
                                       call("#                     w           |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]
@patch('builtins.print')
def test_that_tests_eighth_stage_of_animal_normal(mocked_print):
    # Arrange
    animal_normal = AnimalNormal()

    animal_normal.draw_animal(8)
    assert mocked_print.mock_calls == [call("#               +-w---------------+               #"),
                                       call("#                  \  c(..)o   (  |               #"),
                                       call("#                   \__(-)    __) |               #"),
                                       call("#                       /\   (    |               #"),
                                       call("#                      /(_)___)   |               #"),
                                       call("#                     w           |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]
@patch('builtins.print')
def test_that_tests_ninth_stage_of_animal_normal(mocked_print):
    # Arrange
    animal_normal = AnimalNormal()

    animal_normal.draw_animal(9)
    assert mocked_print.mock_calls == [call("#               +-w---------------+               #"),
                                       call("#                  \  c(..)o   (  |               #"),
                                       call("#                   \__(-)    __) |               #"),
                                       call("#                       /\   (    |               #"),
                                       call("#                      /(_)___)   |               #"),
                                       call("#                     w /         |               #"),
                                       call("#                      |          |               #"),
                                       call("#                      m          |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_tenth_stage_of_animal_normal(mocked_print):
    # Arrange
    animal_normal = AnimalNormal()

    animal_normal.draw_animal(10)
    assert mocked_print.mock_calls == [call("#               +-w---------------+               #"),
                                       call("#                  \  c(..)o   (  |               #"),
                                       call("#                   \__(-)    __) |               #"),
                                       call("#                       /\   (    |               #"),
                                       call("#                      /(_)___)   |               #"),
                                       call("#                     w /|        |               #"),
                                       call("#                      | \        |               #"),
                                       call("#                      m  m       |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_first_stage_of_countries_normal(mocked_print):
    # Arrange
    countries_normal = CountriesNormal()

    countries_normal.draw_countries(1)
    assert mocked_print.mock_calls == [call("#                                                 #"),
                                       call("#                                                 #"),
                                       call("#                                                 #"),
                                       call("#                                                 #"),
                                       call("#                                                 #"),
                                       call("#                                                 #"),
                                       call("#                                                 #"),
                                       call("#                                                 #"),
                                       call("#                                                 #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_second_stage_of_countries_normal(mocked_print):
    # Arrange
    countries_normal = CountriesNormal()

    countries_normal.draw_countries(2)
    assert mocked_print.mock_calls == [call("#                                 I               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_third_stage_of_countries_normal(mocked_print):
    # Arrange
    countries_normal = CountriesNormal()

    countries_normal.draw_countries(3)
    assert mocked_print.mock_calls == [call("#                                 I               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                   #####$|$#####/|               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_fourth_stage_of_countries_normal(mocked_print):
    # Arrange
    countries_normal = CountriesNormal()

    countries_normal.draw_countries(4)
    assert mocked_print.mock_calls == [call("#                                 I               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                   #####$|$#####/|               #"),
                                       call("#                   $$$$$$|$$$$$$ |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_fifth_stage_of_countries_normal(mocked_print):
    # Arrange
    countries_normal = CountriesNormal()

    countries_normal.draw_countries(5)
    assert mocked_print.mock_calls == [call("#                                 I               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                   #####$|$#####/|               #"),
                                       call("#                   $$$$$$|$$$$$$ |               #"),
                                       call("#                   ------+------ |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_sixth_stage_of_countries_normal(mocked_print):
    # Arrange
    countries_normal = CountriesNormal()

    countries_normal.draw_countries(6)
    assert mocked_print.mock_calls == [call("#                                 I               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                   #####$|$#####/|               #"),
                                       call("#                   $$$$$$|$$$$$$ |               #"),
                                       call("#                   ------+------ |               #"),
                                       call("#                   $$$$$$|$$$$$$ |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_seventh_stage_of_countries_normal(mocked_print):
    # Arrange
    countries_normal = CountriesNormal()

    countries_normal.draw_countries(7)
    assert mocked_print.mock_calls == [call("#                                 I               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                   #####$|$#####/|               #"),
                                       call("#                   $$$$$$|$$$$$$ |               #"),
                                       call("#                   ------+------ |               #"),
                                       call("#                   $$$$$$|$$$$$$ |               #"),
                                       call("#                   #####$|$#####\|               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_eighth_stage_of_countries_normal(mocked_print):
    # Arrange
    countries_normal = CountriesNormal()

    countries_normal.draw_countries(8)
    assert mocked_print.mock_calls == [call("#                                 I               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                   #####$|$#####/|               #"),
                                       call("#                   $$$$$$|$$$$$$ |               #"),
                                       call("#                   ------+------ |               #"),
                                       call("#                   $$$$$$|$$$$$$ |               #"),
                                       call("#                   #####$|$#####\|               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_ninth_stage_of_countries_normal(mocked_print):
    # Arrange
    countries_normal = CountriesNormal()

    countries_normal.draw_countries(9)
    assert mocked_print.mock_calls == [call("#                                 I               #"),
                                       call("#                                 |               #"),
                                       call("#                   #####$|$#####/|               #"),
                                       call("#                   $$$$$$|$$$$$$ |               #"),
                                       call("#                   ------+------ |               #"),
                                       call("#                   $$$$$$|$$$$$$ |               #"),
                                       call("#                   #####$|$#####\|               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_tenth_stage_of_countries_normal(mocked_print):
    # Arrange
    countries_normal = CountriesNormal()

    countries_normal.draw_countries(10)
    assert mocked_print.mock_calls == [call("#                                 I               #"),
                                       call("#                   #####$|$#####/|               #"),
                                       call("#                   $$$$$$|$$$$$$ |               #"),
                                       call("#                   ------+------ |               #"),
                                       call("#                   $$$$$$|$$$$$$ |               #"),
                                       call("#                   #####$|$#####\|               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]


@patch('builtins.print')
def test_that_tests_first_stage_of_food_normal(mocked_print):
    # Arrange
    food_normal = FoodNormal()

    food_normal.draw_food(1)
    assert mocked_print.mock_calls == [call("#                                                 #"),
                                       call("#                                                 #"),
                                       call("#                                                 #"),
                                       call("#                                                 #"),
                                       call("#                                                 #"),
                                       call("#                                                 #"),
                                       call("#                                                 #"),
                                       call("#                                                 #"),
                                       call("#                                                 #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_second_stage_of_food_normal(mocked_print):
    # Arrange
    food_normal = FoodNormal()

    food_normal.draw_food(2)
    assert mocked_print.mock_calls == [call("#                                 +               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_third_stage_of_food_normal(mocked_print):
    # Arrange
    food_normal = FoodNormal()

    food_normal.draw_food(3)
    assert mocked_print.mock_calls == [call("#                       +---------+               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_fourth_stage_of_food_normal(mocked_print):
    # Arrange
    food_normal = FoodNormal()

    food_normal.draw_food(4)
    assert mocked_print.mock_calls == [call("#                       +---------+               #"),
                                       call("#                       |         |               #"),
                                       call("#                       |         |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_fifth_stage_of_food_normal(mocked_print):
    # Arrange
    food_normal = FoodNormal()

    food_normal.draw_food(5)
    assert mocked_print.mock_calls == [call("#                       +---------+               #"),
                                       call("#                       |         |               #"),
                                       call("#                       |         |               #"),
                                       call("#                       O         |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_sixth_stage_of_food_normal(mocked_print):
    # Arrange
    food_normal = FoodNormal()

    food_normal.draw_food(6)
    assert mocked_print.mock_calls == [call("#                       +---------+               #"),
                                       call("#                       |         |               #"),
                                       call("#                       |         |               #"),
                                       call("#                       O         |               #"),
                                       call("#                       |         |               #"),
                                       call("#                       |         |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_seventh_stage_of_food_normal(mocked_print):
    # Arrange
    food_normal = FoodNormal()

    food_normal.draw_food(7)
    assert mocked_print.mock_calls == [call("#                       +---------+               #"),
                                       call("#                       |         |               #"),
                                       call("#                       |         |               #"),
                                       call("#                       O         |               #"),
                                       call("#                      /|         |               #"),
                                       call("#                       |         |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_eighth_stage_of_food_normal(mocked_print):
    # Arrange
    food_normal = FoodNormal()

    food_normal.draw_food(8)
    assert mocked_print.mock_calls == [call("#                       +---------+               #"),
                                       call("#                       |         |               #"),
                                       call("#                       |         |               #"),
                                       call("#                       O         |               #"),
                                       call("#                      /|\        |               #"),
                                       call("#                       |         |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_ninth_stage_of_food_normal(mocked_print):
    # Arrange
    food_normal = FoodNormal()

    food_normal.draw_food(9)
    assert mocked_print.mock_calls == [call("#                       +---------+               #"),
                                       call("#                       |         |               #"),
                                       call("#                       |         |               #"),
                                       call("#                       O         |               #"),
                                       call("#                      /|\        |               #"),
                                       call("#                       |         |               #"),
                                       call("#                      /          |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_tenth_stage_of_food_normal(mocked_print):
    # Arrange
    food_normal = FoodNormal()

    food_normal.draw_food(10)
    assert mocked_print.mock_calls == [call("#                       +---------+               #"),
                                       call("#                       |         |               #"),
                                       call("#                       |         |               #"),
                                       call("#                       O         |               #"),
                                       call("#                      /|\        |               #"),
                                       call("#                       |         |               #"),
                                       call("#                      / \        |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]


@patch('builtins.print')
def test_that_tests_first_stage_of_animal_comp(mocked_print):
    # Arrange
    animal_comp = AnimalCompetitive()

    animal_comp.draw_animal(1)
    assert mocked_print.mock_calls == [call("#               +-w---------------+               #"),
                                       call("#                  \              |               #"),
                                       call("#                   \__           |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_second_stage_of_animal_comp(mocked_print):
    # Arrange
    animal_comp = AnimalCompetitive()

    animal_comp.draw_animal(2)
    assert mocked_print.mock_calls == [call("#               +-w---------------+               #"),
                                       call("#                  \  c(..)o      |               #"),
                                       call("#                   \__(-)        |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_third_stage_of_animal_comp(mocked_print):
    # Arrange
    animal_comp = AnimalCompetitive()

    animal_comp.draw_animal(3)
    assert mocked_print.mock_calls == [call("#               +-w---------------+               #"),
                                       call("#                  \  c(..)o      |               #"),
                                       call("#                   \__(-)        |               #"),
                                       call("#                       /         |               #"),
                                       call("#                      /          |               #"),
                                       call("#                     w           |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_fourth_stage_of_animal_comp(mocked_print):
    # Arrange
    animal_comp = AnimalCompetitive()

    animal_comp.draw_animal(4)
    assert mocked_print.mock_calls == [call("#               +-w---------------+               #"),
                                       call("#                  \  c(..)o      |               #"),
                                       call("#                   \__(-)        |               #"),
                                       call("#                       /         |               #"),
                                       call("#                      /          |               #"),
                                       call("#                     w           |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_fifth_stage_of_animal_comp(mocked_print):
    # Arrange
    animal_comp = AnimalCompetitive()

    animal_comp.draw_animal(5)
    assert mocked_print.mock_calls == [call("#               +-w---------------+               #"),
                                       call("#                  \  c(..)o      |               #"),
                                       call("#                   \__(-)        |               #"),
                                       call("#                       /\        |               #"),
                                       call("#                      /(_)       |               #"),
                                       call("#                     w           |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_sixth_stage_of_animal_comp(mocked_print):
    # Arrange
    animal_comp = AnimalCompetitive()

    animal_comp.draw_animal(6)
    assert mocked_print.mock_calls == [call("#               +-w---------------+               #"),
                                       call("#                  \  c(..)o   (  |               #"),
                                       call("#                   \__(-)    __) |               #"),
                                       call("#                       /\   (    |               #"),
                                       call("#                      /(_)___)   |               #"),
                                       call("#                     w           |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_seventh_stage_of_animal_comp(mocked_print):
    # Arrange
    animal_comp = AnimalCompetitive()

    animal_comp.draw_animal(7)
    assert mocked_print.mock_calls == [call("#               +-w---------------+               #"),
                                       call("#                  \  c(..)o   (  |               #"),
                                       call("#                   \__(-)    __) |               #"),
                                       call("#                       /\   (    |               #"),
                                       call("#                      /(_)___)   |               #"),
                                       call("#                     w /         |               #"),
                                       call("#                      |          |               #"),
                                       call("#                      m          |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_eighth_stage_of_animal_comp(mocked_print):
    # Arrange
    animal_comp = AnimalCompetitive()

    animal_comp.draw_animal(8)
    assert mocked_print.mock_calls == [call("#               +-w---------------+               #"),
                                       call("#                  \  c(..)o   (  |               #"),
                                       call("#                   \__(-)    __) |               #"),
                                       call("#                       /\   (    |               #"),
                                       call("#                      /(_)___)   |               #"),
                                       call("#                     w /|        |               #"),
                                       call("#                      | \        |               #"),
                                       call("#                      m  m       |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_first_stage_of_countries_comp(mocked_print):
    # Arrange
    countries_comp = CountriesCompetitive()

    countries_comp.draw_countries(1)
    assert mocked_print.mock_calls == [call("#                                 I               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                   #####$|$#####/|               #"),
                                       call("#                   $$$$$$|$$$$$$ |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_second_stage_of_countries_comp(mocked_print):
    # Arrange
    countries_comp = CountriesCompetitive()

    countries_comp.draw_countries(2)
    assert mocked_print.mock_calls == [call("#                                 I               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                   #####$|$#####/|               #"),
                                       call("#                   $$$$$$|$$$$$$ |               #"),
                                       call("#                   ------+------ |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_third_stage_of_countries_comp(mocked_print):
    # Arrange
    countries_comp = CountriesCompetitive()

    countries_comp.draw_countries(3)
    assert mocked_print.mock_calls == [call("#                                 I               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                   #####$|$#####/|               #"),
                                       call("#                   $$$$$$|$$$$$$ |               #"),
                                       call("#                   ------+------ |               #"),
                                       call("#                   $$$$$$|$$$$$$ |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_fourth_stage_of_countries_comp(mocked_print):
    # Arrange
    countries_comp = CountriesCompetitive()

    countries_comp.draw_countries(4)
    assert mocked_print.mock_calls == [call("#                                 I               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                   #####$|$#####/|               #"),
                                       call("#                   $$$$$$|$$$$$$ |               #"),
                                       call("#                   ------+------ |               #"),
                                       call("#                   $$$$$$|$$$$$$ |               #"),
                                       call("#                   #####$|$#####\|               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_fifth_stage_of_countries_comp(mocked_print):
    # Arrange
    countries_comp = CountriesCompetitive()

    countries_comp.draw_countries(5)
    assert mocked_print.mock_calls == [call("#                                 I               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                   #####$|$#####/|               #"),
                                       call("#                   $$$$$$|$$$$$$ |               #"),
                                       call("#                   ------+------ |               #"),
                                       call("#                   $$$$$$|$$$$$$ |               #"),
                                       call("#                   #####$|$#####\|               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_sixth_stage_of_countries_comp(mocked_print):
    # Arrange
    countries_comp = CountriesCompetitive()

    countries_comp.draw_countries(6)
    assert mocked_print.mock_calls == [call("#                                 I               #"),
                                       call("#                                 |               #"),
                                       call("#                   #####$|$#####/|               #"),
                                       call("#                   $$$$$$|$$$$$$ |               #"),
                                       call("#                   ------+------ |               #"),
                                       call("#                   $$$$$$|$$$$$$ |               #"),
                                       call("#                   #####$|$#####\|               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_seventh_stage_of_countries_comp(mocked_print):
    # Arrange
    countries_comp = CountriesCompetitive()

    countries_comp.draw_countries(7)
    assert mocked_print.mock_calls == [call("#                                 I               #"),
                                       call("#                   #####$|$#####/|               #"),
                                       call("#                   $$$$$$|$$$$$$ |               #"),
                                       call("#                   ------+------ |               #"),
                                       call("#                   $$$$$$|$$$$$$ |               #"),
                                       call("#                   #####$|$#####\|               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_first_stage_of_food_comp(mocked_print):
    # Arrange
    food_comp = FoodCompetitive()

    food_comp.draw_food(1)
    assert mocked_print.mock_calls == [call("#                       +---------+               #"),
                                       call("#                       |         |               #"),
                                       call("#                       |         |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]
@patch('builtins.print')
def test_that_tests_second_stage_of_food_comp(mocked_print):
    # Arrange
    food_comp = FoodCompetitive()

    food_comp.draw_food(2)
    assert mocked_print.mock_calls == [call("#                       +---------+               #"),
                                       call("#                       |         |               #"),
                                       call("#                       |         |               #"),
                                       call("#                       O         |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_third_stage_of_food_comp(mocked_print):
    # Arrange
    food_comp = FoodCompetitive()

    food_comp.draw_food(3)
    assert mocked_print.mock_calls == [call("#                       +---------+               #"),
                                       call("#                       |         |               #"),
                                       call("#                       |         |               #"),
                                       call("#                       O         |               #"),
                                       call("#                       |         |               #"),
                                       call("#                       |         |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_fourth_stage_of_food_comp(mocked_print):
    # Arrange
    food_comp = FoodCompetitive()

    food_comp.draw_food(4)
    assert mocked_print.mock_calls == [call("#                       +---------+               #"),
                                       call("#                       |         |               #"),
                                       call("#                       |         |               #"),
                                       call("#                       O         |               #"),
                                       call("#                      /|         |               #"),
                                       call("#                       |         |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_fifth_stage_of_food_comp(mocked_print):
    # Arrange
    food_comp = FoodCompetitive()

    food_comp.draw_food(5)
    assert mocked_print.mock_calls == [call("#                       +---------+               #"),
                                       call("#                       |         |               #"),
                                       call("#                       |         |               #"),
                                       call("#                       O         |               #"),
                                       call("#                      /|\        |               #"),
                                       call("#                       |         |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_sixth_stage_of_food_comp(mocked_print):
    # Arrange
    food_comp = FoodCompetitive()

    food_comp.draw_food(6)
    assert mocked_print.mock_calls == [call("#                       +---------+               #"),
                                       call("#                       |         |               #"),
                                       call("#                       |         |               #"),
                                       call("#                       O         |               #"),
                                       call("#                      /|\        |               #"),
                                       call("#                       |         |               #"),
                                       call("#                      /          |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]

@patch('builtins.print')
def test_that_tests_seventh_stage_of_food_comp(mocked_print):
    # Arrange
    food_comp = FoodCompetitive()

    food_comp.draw_food(7)
    assert mocked_print.mock_calls == [call("#                       +---------+               #"),
                                       call("#                       |         |               #"),
                                       call("#                       |         |               #"),
                                       call("#                       O         |               #"),
                                       call("#                      /|\        |               #"),
                                       call("#                       |         |               #"),
                                       call("#                      / \        |               #"),
                                       call("#                                 |               #"),
                                       call("#                                 |               #"),
                                       call("#               ===================               #")]
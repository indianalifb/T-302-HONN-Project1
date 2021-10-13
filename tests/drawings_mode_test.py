from src.drawings_catagories.animal_competitive import AnimalCompetitive
from src.drawings_catagories.animal_normal import AnimalNormal
from src.drawings_catagories.countries_competitive import CountriesCompetitive
from src.drawings_catagories.countries_normal import CountriesNormal
from src.drawings_catagories.food_competitve import FoodCompetitive
from src.drawings_catagories.food_normal import FoodNormal
from src.drawings_mode.normal_drawing import NormalDrawing
from src.drawings_mode.competitve_drawing import CompetitveDrawing
import pytest
from unittest.mock import Mock, MagicMock, patch

def test_that_normal_animal_returns_animal_normal():
    # Arrange
    normal = NormalDrawing()
    # Act
    category = normal.create_animal()
    # Assert
    assert isinstance(category, AnimalNormal) == True

def test_that_normal_food_returns_food_normal():
    # Arrange
    normal = NormalDrawing()
    # Act
    category = normal.create_food()
    # Assert
    assert isinstance(category, FoodNormal) == True

def test_that_normal_country_returns_country_normal():
    # Arrange
    normal = NormalDrawing()
    # Act
    category = normal.create_country()
    # Assert
    assert isinstance(category, CountriesNormal) == True

def test_that_competitive_animal_returns_animal_competitive():
    # Arrange
    comp = CompetitveDrawing()
    # Act
    category = comp.create_animal()
    # Assert
    assert isinstance(category, AnimalCompetitive) == True

def test_that_competitive_food_returns_food_competitive():
    # Arrange
    comp = CompetitveDrawing()
    # Act
    category = comp.create_food()
    # Assert
    assert isinstance(category, FoodCompetitive) == True

def test_that_competitive_country_returns_country_competitive():
    # Arrange
    comp = CompetitveDrawing()
    # Act
    category = comp.create_country()
    # Assert
    assert isinstance(category, CountriesCompetitive) == True
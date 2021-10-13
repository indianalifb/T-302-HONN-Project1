# T-302-HONN-Project1

## About the system
Python console application.
## Prerequisites
Make sure you have installed all of the following prerequisites on your machine:

* Python3.6+
* PostgreSQL

## Running the program:
First make sure you have PostgreSQL installed<br/>
Create database Hangman and run create.sql script<br/>
in src/infrastructure add a .env file that contains your database configuration<br/>
 ```# postgres database logging
postgres_log_host="localhost"
postgres_log_database="Hangman"
postgres_log_user="postgres"
postgres_log_password="password"

# environment
environment="prod"
```

using VENV
In T-302-HONN-Projcet1 directory create a virtual environment<br>
Firstly make sure you have virtualenv installed<br>
```pip install virtualenv``` <br>
then we can run <br>
```virtualenv venv``` 
<br>
Next step we activate the environment<br>
```./venv/bin/activate``` <br> 
or if using Fish shell<br>
```source venv/bin/activate.fish``` <br>
Next up let's install required packages<br>
```python -m pip install -r requirements.txt``` <br>
Now the virtual environment should be set up and we can finally run the program<br>
```python -m src.main``` <br>
Now just sit back and guess some letters!<br>

## Design Patterns:
 • Strategy     
 • Decorator    
 • Abstract Factory     
 • Template Method  
 • State
 • Observer
 • Adapter

 ## Design Principles
 • Open-Closed Principle        
 • Single Responsibility Principle      
 • DRY  
 • Loose Coupling   
 • Encapsulate what varies	    

## Authors
Indíana Líf Bergsteinsdóttir - indiana18@ru.is     
Thelma Karen Jónsdóttir - thelma20@ru.is
Pálína Líf Ingadóttir - palinai20@ru.is
Þorgils Árni Hjálmarsson - thorgils20@ru.is

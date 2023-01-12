
# cryptoscrapt
Web scrapin script.

## Description
When executed this script gonna return an image of the top 50 crypto atm.

## Getting Started
To be able to reproduce the code i have made you will need a couple of things.
First you will need, obviously, a Python interpreter, version 3 is pretty much standard nowadays, and a package manager for Python, i will be covering PyPI in this one.
After you install both you can check if everything is alright by executing this commands:
```
python --version
pip --version
```

If this runs, then we are almost ready to execute the script.

## Environment
I've basically did this with a virtual environment, in my case im using pipenv but venv is quite ok.
To create a virtual environment you first need to download the one of ur taste, just run this command:
```
pip install virtualenv
```  
or
```
pip install pipenv
```
So once you have done that, depending of wich of the options you chosed, you will need to go to the directory you want to create the environment to, and execute this commands:
```
virtualenv <nameofyourenvironment>
```

or 

```
pipenv shell
```

In the first case, that command only going to create your virtualenv but it's not going to activate it, so to activate virtualenv you need to execute:
```
source <nameofyourenviroment>/Scripts/activate #windows 
source <nameofyourenviroment>/bin/activate #linux
```

With this we have completed our environment creation, now we move to dependencies.

## Dependencies
I'm assuming you already copy this repository to recreate the script, so you already have the requirements file, to download dependecies into your environment execute this commands.
For virtualenv:
```
pip install -r requirements.txt
```
For pipenv:
```
pipenv install -r requirements.txt
pipenv run pip install -r requirements.txt
```

In this case, pipenv is a little buggy, if you find yourself not being able to install dependcies with the first option just go with the second one, never fails.

### Execute
And finally you can execute the script by tiping in your directory this line:
```
python main.py #windows
python3 main.py #linux
``` 

### Result
And in the end you are going to be having an image like this one.

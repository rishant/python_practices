REST-API Specification:
    https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
    https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
    https://www.uuidgenerator.net/version4

ASGI vs WSGI:
    https://medium.com/analytics-vidhya/difference-between-wsgi-and-asgi-807158ed1d4c

Video References:
    Python Core:- https://www.youtube.com/watch?v=sCOw5y1RQpY&t=48857s
    Basic FastApi:- https://www.youtube.com/watch?v=GN6ICac3OXY
    FARM(FastAPI, ReactJS, MongoDB):- https://www.youtube.com/watch?v=oGwszbCH5Z4

FastAPI:
    https://fastapi.tiangolo.com/

uvicorn:
    https://www.uvicorn.org/

DataBase Object Modeling: Pydantic:- as ORMs, ODMs for databases.
    https://pydantic-docs.helpmanual.io/

Outofbox OpenApi integration with FastAPI:
    http://127.0.0.1:8000/docs

Project Setup Steps:
1. Create project folder and open in VScode.
2. Open terminal and run below commands.
https://pip.pypa.io/en/stable/cli/
    2.1 - Virtual environment creation and Activate:
        terminal:> python -m venv virtual-environment
        terminal:> virtual-environment\Scripts\activate

    2.2 - Install modules dependencies for project:
        terminal:> pip install fastapi uvicorn[standard]
    
    2.3 - Check and create requirements.txt file from virtual environment:
        terminal:> python -m pip freeze
        terminal:> python -m pip freeze > requirements.txt
        terminal:> pip freeze > requirements.txt

    2.4 - Now we can delete virtual environment and install or uninstall dependencies:
        terminal:> python -m pip install -r requirements.txt
        terminal:> pip install -r requirements.txt

        terminal:> python -m pip uninstall -r requirements.txt
        terminal:> pip uninstall -r requirements.txt

    2.5 - To list installed packages:
        terminal:> python -m pip list
        terminal:> python -m pip list --outdated

    2.6 - To show details about an installed package
        terminal:> python -m pip show sphinx

    2.7 - Searching for Packages
        terminal:> python -m pip search "query"

    2.8 - Start uvicorn server:
        terminal:>uvicorn main:app --reload
    

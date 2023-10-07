# HackMorelos2023

## Installation Instructions
### Installation
Create a virtual environment:
- You can use venv
- Activate the virtual environment
- Then from the virtual environment install the python packages specified in requirements.txt:  
`pip install -r requirements.txt`

## Running the application 
To run the development server to serve the Flask application:  
`flask --app app --debug run`

Then navigate to http://127.0.0.1:5000


## Generating requirements list from conda environment
`pip list --format=freeze > requirements.txt`
[source](https://stackoverflow.com/questions/62863020/pip-freeze-generating-file-on-conda-environment)
# Django VietCardOCR
## Installation
Creation of virtual environments is done by executing the command venv:
```bash
python -m venv venv
```

That will create a new folder env in your project directory. Next activate it with this command on mac/linux:
```bash
source venv/bin/active
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements:
```bash
pip install -r requirements.txt
```

In the project folder, create **media** folder and its subfolders as structure below:
```
├───media
│   └───images
│       ├───driving-license
│       ├───id-card
│       └───student-card
```

## Usage
Run the project with this command. Then open http://localhost:8000 in your borwser to see the website.
```bash
python manage.py runserver
```
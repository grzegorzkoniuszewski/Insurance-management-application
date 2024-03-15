# INSURANCE MANAGEMENT APPLICATION

## Introduction

The goal of this project is the application to manage user insurance policies, both vehicle and life insurance.

## Requirements
```bash
#create a virtual environment for application libriaries in Windows OS:
#add Python interpreter
#activating hermetic environment

venv\Scripts\activate
pip  install  -r  requirements.txt
pip  install  -r  test_requirements.txt
pip  list
```
Check: [tutorial venv](https://docs.python.org/3/tutorial/venv.html)
/ [djangoproject](https://www.djangoproject.com/) documentation

## Installation

Steps required to install and run the project locally.

1. Clone the repository:

    ```bash
    https://github.com/grzegorzkoniuszewski/Insurance-management-application
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Perform database migrations:

    ```bash
    python manage.py migrate
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

## Usage

The application is designed to facilitate the management of user insurance policies. Its features include:

1.  Adding, editing, and deleting user profiles.
2.  Adding, editing, and deleting insurance policies.
3.  Adding, editing, and deleting insurance companies.
4.  User panel functionality, including registration, login, and logout capabilities.

## Contributions

Any additional contribution to the project, such as reporting bugs, proposing new features, etc. is very welcome. 
Please contact any of authors regarding your observations, suggestions and comments.

## Authors

- Grzegorz Koniuszewski - Front-end, Back-end, Databases, Tests
https://github.com/grzegorzkoniuszewski
- Maciej Kulczycki - Front-end, Back-end, Databases, Tests
https://github.com/mackul1988
- Jakub Bułaj - Back-end
https://github.com/birbant

Special thanks for Mrs Beata Zalewa for suggestions, help and patience during making this project. 
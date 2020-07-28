# A Rest API using Python and Flask
> Quick simple CRUD project using Flask, Flask-RESTful, with JWT authentication.

> #Python #Flask #Flask-RESTful #Flask-SQLAlchemy #Flask-JWT-Extended

## Installation
- Clone this repo to your local machine using `https://github.com/rykehg/produtosPyFlaskJWTTests`.
- Start terminal in the root folder of this project.
- In Windows OS Start a new virtual environment and install the requirements.
```shell
$ python -m venv .venv
$ .venv\Scripts\Activate.ps1
$ pip install -r requirements.txt
```
- Now create a MySQL data base `CREATE DATABASE MyDataBase`
- To configure MySQL database just change `"config.py"` to your credentials (user, password, host and database).

- To run the API in console type `(.venv) $ python run.py`.
- If tables in the data base does not exist it will be created automatically by the API.

## Testing using a Client API
- To test API use Postman and import `"API Client/produtosFlask.postman_collection.json"`.
- Or use "REST Client" Extension for VS Code and file `"API Client/REST_API_Test.rest"`.
- Create an user and login to access other routes.

## Unit Tests
- It is important to make a separate virtual environment for testing.
- In terminal deactivate, if active, `$ deactivate` you current virtual environment and start a new one:
```shell
$ python -m venv .test-venv
$ .test-venv\Scripts\Activate.ps1
$ pip install -r requirements.txt
```

- Set a new database for testing in `"config.py"` file.
- We are going to use the standard library `unittest` and `json`.
- To run a single test file use the command:
```shell
$ python -m unittest tests/test_usuario_create.py
```

- To run all the tests:
```shell
$ python -m unittest --buffer
```

- Or use VSCode.
- To enable testes in VSCode `Ctrl`+`Shift`+`P` and type `Python: Configure Tests`
- Select `unittest`, `test` folder and `test_*py` pattern to identify test files

---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**


# Dog-Walking-Service

## Flask App
This is a flask app that uses a database to store some data.

## Requirements:
•  Python 3.6 or higher

•  Flask

•  SQLAlchemy

•  dotenv

## Installation
1. Clone this repository and cd into it.
2. Create a virtual environment and activate it.
3. Install the dependencies with `pip install -r requirements.txt`.
4. Create a .env file in the root directory and add the following variables:

```
DB_USERNAME=your_database_username
DB_PASSWORD=your_database_password
DB_HOST=your_database_host
DB_PORT=your_database_port
DB_NAME=your_database_name
```

## Starting
1. Run `flask run` to start the app.

## Usage
You can access the app at http://localhost:5000/.
You can use the endpoints listed in docs here http://localhost:5000/api/docs/.

## Testing
You can run the tests with pytest.

## License
This project is licensed under the MIT License.

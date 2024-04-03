# API Provider using Flask with JWT Authentication

This API provider utilizes the Flask Python framework and integrates Json Web Token (JWT) for authentication.

## Files Overview

- `app.py`: This file contains the implementation of the API provider's program using Flask.
- `consume.py`: An example program demonstrating how to consume the API provided by `app.py`.

## Data Source

The data utilized by the API provider is sourced from a CSV file. Using CSV data simplifies the process of data management and integration with the API. However, the API can also be adapted to work with other data sources such as MySQL and others.

## Requirements

To use this project, make sure you have the following installed:

- Python 3.x
- Flask
- Flask JWT Extended

## Testing

You can test the API endpoints using tools like Postman or Thunder Client (VS Code extension). Here's how:

1. **Obtain JWT Token:**
   - Acquire a JWT token using the appropriate authentication method provided by the API.

2. **Send Requests:**
   - Use the obtained JWT token to authenticate your requests.
   - Send HTTP requests to the desired endpoints using the tool of your choice (Postman or Thunder Client).

# Without Token
![Without Token](https://github.com/chairulimamizaaz/Flask-API-Provider-JWT/raw/main/Without%20Token.png)

# With Token
![Without Token](https://github.com/chairulimamizaaz/Flask-API-Provider-JWT/raw/main/Without%20Token.png)

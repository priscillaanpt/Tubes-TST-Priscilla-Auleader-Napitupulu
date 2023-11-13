# Tubes-TST-Priscilla-Auleader-Napitupulu

# Women Cloth Review API

## Description

The Women Cloth Review API is a service that allows users to review and manage clothing products. It provides endpoints for retrieving product information, adding new products, updating existing products, and posting reviews. This API is built using FastAPI and SQLAlchemy and offers a range of functionalities for users to interact with clothing products and reviews.

## API Endpoints

- **GET `/products/`**
  - Description: Retrieve a list of clothing products.
  - Response: A list of clothing products with details such as name, description, and price.
  - Additional Info: You can specify the number of products to skip and the maximum number of products to return using query parameters.

- **GET `/products/{product_id}`**
  - Description: Retrieve a specific clothing product by its ID.
  - Response: Details of the clothing product, including its name, description, and price.
  - Additional Info: You must provide the product's ID as a path parameter.

- **POST `/products/`**
  - Description: Create a new clothing product.
  - Request: Provide details of the new product, including name, description, and price in the request body.
  - Response: Details of the newly created product.

- **PUT `/products/{product_id}`**
  - Description: Update an existing clothing product.
  - Request: Provide the updated product details in the request body.
  - Response: Details of the updated product.
  - Additional Info: You must provide the product's ID as a path parameter.

- **DELETE `/products/{product_id}`**
  - Description: Delete a specific clothing product.
  - Response: Details of the deleted product.
  - Additional Info: You must provide the product's ID as a path parameter.

- **GET `/reviews/`**
  - Description: Retrieve a list of clothing reviews.
  - Response: A list of clothing reviews with details such as user ID, product ID, rating, and review text.
  - Additional Info: You can specify the number of reviews to skip and the maximum number of reviews to return using query parameters.

- **GET `/reviews/{review_id}`**
  - Description: Retrieve a specific clothing review by its ID.
  - Response: Details of the clothing review, including user ID, product ID, rating, and review text.
  - Additional Info: You must provide the review's ID as a path parameter.

- **POST `/reviews/`**
  - Description: Create a new clothing review.
  - Request: Provide details of the new review, including user ID, product ID, rating, and review text in the request body.
  - Response: Details of the newly created review.

- **PUT `/reviews/{review_id}`**
  - Description: Update an existing clothing review.
  - Request: Provide the updated review details in the request body.
  - Response: Details of the updated review.
  - Additional Info: You must provide the review's ID as a path parameter.

## Author

- Author: Priscilla Auleader Napitupulu (18221098)
- GitHub: (https://github.com/priscillaanpt)

## Library

The API is built using the following libraries and technologies:

- FastAPI: A modern, fast web framework for building APIs with Python.
- Uvicorn: An ASGI server that serves as the application server for FastAPI.
- SQLAlchemy: A powerful and flexible toolkit for working with SQL databases.
- Pydantic: Data validation and parsing library.
- JOSE (JSON Object Signing and Encryption): A library for handling JSON Web Tokens (JWT).

## Reference

- https://fastapi.tiangolo.com
- https://www.uvicorn.org
- https://www.sqlalchemy.org
- https://docs.pydantic.dev/latest/
- https://python-jose.readthedocs.io/en/latest/


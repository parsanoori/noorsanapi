# API Documentation for `credittotoken` and `approveco2` Endpoints

##  Warning: ChatGPT Generated README.md

This README.md file provides documentation for the API endpoints implemented in the provided Python Flask code. The code defines two endpoints, `/credittotoken` and `/approveco2`, and this documentation explains how to use them.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [`/credittotoken`](#credittotoken-endpoint)
  - [`/approveco2`](#approveco2-endpoint)

---

## Installation

Before using the API, you need to set up the Python environment and install the required dependencies.

1. Install Flask using pip (if not already installed):
   ```
   pip install flask
   ```

2. Save the provided Python code in a file, e.g., `app.py`.

3. Run the Flask application:
   ```
   python app.py
   ```

The application will start and be accessible at `http://localhost:5000`.

---

## Usage

### `/credittotoken` Endpoint

This endpoint is used to generate random data associated with a "token." It accepts a POST request and returns a JSON response with randomly generated data. Here's how to use it:

- **URL:** `/credittotoken`
- **Method:** `POST`
- **Request Body:**

  ```json
  {
    "tokenid": "YOUR_TOKEN_ID"
  }
  ```

  Replace `"YOUR_TOKEN_ID"` with the desired token ID.

- **Response:**

  Example Response:

  ```json
  {
    "company": "abcde",
    "technology": "fghij",
    "device": "klmno",
    "carbon_value": "pqrst",
    "carbon_type": "uvwxy",
    "project_name": "zabcd",
    "registry_address": "efghi",
    "credit_id": "jklmn",
    "retired_date": 1669459200,
    "energy": 123,
    "standard": "noorsan"
  }
  ```

  The response will contain random data fields associated with the token, including a `standard` field that is set to "noorsan" if the token ID starts with "1402," otherwise, it's a random string.

### `/approveco2` Endpoint

This endpoint is used to approve or reject CO2 data based on a given token ID and standard. It accepts a POST request and returns a JSON response with a boolean result. Here's how to use it:

- **URL:** `/approveco2`
- **Method:** `POST`
- **Request Body:**

  ```json
  {
    "tokenid": "YOUR_TOKEN_ID",
    "standard": "noorsan"
  }
  ```

  Replace `"YOUR_TOKEN_ID"` with the desired token ID and `"standard"` with the desired standard for approval.

- **Response:**

  Example Response (If approved):

  ```json
  {
    "result": true
  }
  ```

  Example Response (If not approved):

  ```json
  {
    "result": false
  }
  ```

  The response will contain a boolean `result` field, where `true` indicates approval if the standard is "noorsan" and the token ID starts with "1402." Otherwise, it returns `false`.

---

That's it! You can now use the `/credittotoken` and `/approveco2` endpoints of this API to generate random token data and approve/reject CO2 data, respectively. Make sure to provide the required input data in the request bodies as specified above.

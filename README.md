# Zkipster-Tech-Assessment-API-Automation

This repository contains the solution to the **API Automation** section of the QA Engineer technical assessment for zkipster.

---

## Tech Stack

- Python 3.8+
- Pytest
- Requests
---

## Happy Path Test Cases

1. Update only one field (e.g., status) 
2. Update with new tags
3. Update with a new category
4. Update with different photo URLs  
5. Update pet immediately after creating 
6. Update pet with Unicode / special characters in name
7. Update with edge values
8. Update a pet using minimal valid data
9. Update a pet with a unique ID not previously used
10. Update same pet multiple times

---

## Project Structure

``` bash
.
├── tests/
│   └── put_pet_endpoint.py
├── utils/
│   ├── __init__.py
│   └── payload_helper.py
├── requirements.txt
└── README.md

```

---

## How to run the project

1. Install all dependencies

``` bash
pip install -r requirements.txt
```

2. Run the tests

To run each test run the following command on the directory that contains the test cases:

``` bash
pytest -v tests/
```

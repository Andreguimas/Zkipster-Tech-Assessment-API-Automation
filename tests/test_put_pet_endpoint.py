import pytest
import requests
from utils.payload_helper import build_pet_payload

BASE_URL = "https://petstore.swagger.io/v2"
PET_ID = 1234567890

@pytest.fixture(scope="module")
# Create a base pet fixture that will be used in multiple tests
def base_pet():
    pet = build_pet_payload(pet_id=PET_ID, name="Buddy", status="available")
    response = requests.post(f"{BASE_URL}/pet", json=pet)
    assert response.status_code == 200
    return pet

# Test cases for the PUT /pet endpoint

# Update only the status of the pet
def test_update_pet_status_only(base_pet):
    base_pet["status"] = "pending"
    response = requests.put(f"{BASE_URL}/pet", json=base_pet)
    assert response.status_code == 200
    assert response.json()["status"] == "pending"

# Update the tags of the pet
def test_update_pet_tags(base_pet):
    base_pet["tags"] = [{"id": 2, "name": "new-tag"}]
    response = requests.put(f"{BASE_URL}/pet", json=base_pet)
    assert response.status_code == 200
    assert response.json()["tags"][0]["name"] == "new-tag"

# Update the category of the pet
def test_update_pet_category(base_pet):
    base_pet["category"] = {"id": 2, "name": "cats"}
    response = requests.put(f"{BASE_URL}/pet", json=base_pet)
    assert response.status_code == 200
    assert response.json()["category"]["name"] == "cats"

# Update the photoUrls to include a new image URL
def test_update_pet_photo_urls(base_pet):
    base_pet["photoUrls"] = ["https://example.com/cat.jpg"]
    response = requests.put(f"{BASE_URL}/pet", json=base_pet)
    assert response.status_code == 200
    assert "https://example.com/cat.jpg" in response.json()["photoUrls"]

# Update the pet's name with a unicode character
def test_update_pet_with_unicode_name(base_pet):
    base_pet["name"] = "Fígado"
    response = requests.put(f"{BASE_URL}/pet", json=base_pet)
    assert response.status_code == 200
    assert response.json()["name"] == "Fígado 🐶"

# Using maximum integer values for id and category id
def test_update_pet_with_max_int_ids(base_pet):
    base_pet["id"] = 9223372036854775807
    base_pet["category"]["id"] = 999999
    base_pet["tags"] = [{"id": 999999, "name": "edge-tag"}]
    response = requests.put(f"{BASE_URL}/pet", json=base_pet)
    assert response.status_code == 200
    assert response.json()["id"] == 9223372036854775807

# Test updating a pet with minimal valid data
def test_update_minimal_valid_data():
    minimal_pet = {
        "id": 111,
        "name": "MinimalPet",
        "photoUrls": ["https://example.com/minimal.jpg"],
        "status": "available"
    }
    response = requests.put(f"{BASE_URL}/pet", json=minimal_pet)
    assert response.status_code == 200
    assert response.json()["name"] == "MinimalPet"

# Update the pet multiple times with different names and statuses
def test_update_pet_multiple_times(base_pet):
    updates = [
        ("StepOne", "pending"),
        ("StepTwo", "sold"),
        ("StepThree", "available")
    ]
    for name, status in updates:
        base_pet["name"] = name
        base_pet["status"] = status
        response = requests.put(f"{BASE_URL}/pet", json=base_pet)
        assert response.status_code == 200
        assert response.json()["name"] == name
        assert response.json()["status"] == status

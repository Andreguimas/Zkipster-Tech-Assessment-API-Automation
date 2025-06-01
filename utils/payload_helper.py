def build_pet_payload(pet_id, name="Doggie", status="available"):
    return {
        "id": pet_id,
        "category": {
            "id": 1,
            "name": "dogs"
        },
        "name": name,
        "photoUrls": ["https://example.com/dog.jpg"],
        "tags": [
            {
                "id": 1,
                "name": "tag1"
            }
        ],
        "status": status
    }

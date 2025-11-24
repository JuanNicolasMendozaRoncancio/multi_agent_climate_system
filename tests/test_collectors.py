from src.database.mongodb_client import get_collection

def test_get_collection():
    col = get_collection("test_collection")
    result = col.insert_one({"message": "Hola Mundo desde MongoDB"})
    print("Inserted document ID:", result.inserted_id)

test_get_collection()
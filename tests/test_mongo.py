from src.database.mongodb_client import get_collection
print("Testing MongoDB connection...")
def test_insert():
    col = get_collection("raw")
    result = col.insert_one({"message": "Hola mundo"})
    print("Insertado:", result.inserted_id)

test_insert()
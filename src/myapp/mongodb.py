from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient(
    "mongodb+srv://joaquin:3volution@cluster0.ghkqw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)
db = client["mongo"]


class BaseModel:
    collection_name = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def get_collection(cls):
        """Returns the collection for the model."""
        if not cls.collection_name:
            raise NotImplementedError("Must define 'collection_name' in the model.")
        return db[cls.collection_name]

    @classmethod
    def create(cls, **kwargs):
        """Creates a new document in the collection."""
        collection = cls.get_collection()
        result = collection.insert_one(kwargs)
        return str(result.inserted_id)

    @classmethod
    def find(cls, query=None):
        """Finds documents based on a query."""
        query = query or {}
        collection = cls.get_collection()
        results = collection.find(query)
        return [cls(**doc) for doc in results]

    @classmethod
    def find_one(cls, query):
        """Finds a single document based on a query."""
        collection = cls.get_collection()
        doc = collection.find_one(query)
        return cls(**doc) if doc else None

    def save(self):
        """Saves the document."""
        collection = self.get_collection()
        if hasattr(self, "_id") and self._id:
            collection.update_one({"_id": ObjectId(self._id)}, {"$set": self.to_dict()})
        else:
            result = collection.insert_one(self.to_dict())
            self._id = str(result.inserted_id)

    def delete(self):
        """Deletes the document."""
        if hasattr(self, "_id") and self._id:
            collection = self.get_collection()
            collection.delete_one({"_id": ObjectId(self._id)})

    def to_dict(self):
        """Converts the model to a dictionary."""
        data = self.__dict__.copy()
        if "_id" in data:
            data["_id"] = ObjectId(data["_id"])
        return data

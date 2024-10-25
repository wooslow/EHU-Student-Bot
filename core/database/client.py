import os

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from dotenv import load_dotenv
from pydantic import BaseModel

from .service import DataBaseAdapter

load_dotenv()


class DataBaseClient:
    def __init__(self) -> None:
        self.client: MongoClient = AsyncIOMotorClient(os.getenv("MONGO_URI"))['EHU']

    async def save_object(self, obj: BaseModel) -> None:
        """
        Function to save an object to the database.

        :param obj: BaseModel: The object to be saved
        :return: None
        """

        await self.client[obj.__class__.__name__].update_one(
            {'_id': obj.id},
            {'$set': obj.model_dump(by_alias=True)},
            upsert=True
        )

    async def get_object_by_id(self, unique_id: str | int, model: BaseModel) -> DataBaseAdapter | None:
        """
        Function to get an object from the database by its ID.

        :param unique_id: str | int: The ID of the object
        :param model: BaseModel: The model of the object
        :return: DataBaseAdapter | None: The object
        """

        data = await self.client[model.__name__].find_one({'_id': unique_id})

        if data is None:
            return None

        return DataBaseAdapter.data_to_object(data, model)  # noqa: ignore

from pydantic import BaseModel


class DataBaseAdapter(BaseModel):
    @staticmethod
    async def execute_query(function: str, *args) -> None | dict:
        """
        Execute a database operation.

        :param function: str: The name of the function to be called
        :param args: Any arguments to be passed to the function
        :return: None | dict: The result of the operation
        """
        from .client import DataBaseClient

        client = DataBaseClient()
        return await client.__getattribute__(function)(*args)

    @staticmethod
    def data_to_object(data: dict, model: BaseModel) -> object:
        """
        Convert a dictionary to a Pydantic model.

        :param data: dict: The data to be converted
        :param model: BaseModel: The model to be converted to
        :return: BaseModel: The converted model
        """
        return model.model_validate(data)

    async def save(self) -> None:
        """
        Save the object to the database.
        """
        await self.execute_query('save_object', self)

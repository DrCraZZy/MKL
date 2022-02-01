from datetime import datetime

from project.app.repositories.base_repository import BaseRepository
from project.app.schema.transporter import TransporterSchema
from project.app.db.tables.transporter import transporter_data
from project.app.helper.log import logger
from project.app.helper.endpoint_answer import EndpointAnswer


class TransporterRepository(BaseRepository):

    @logger.catch
    async def create_transporter(self, transporter: TransporterSchema) -> EndpointAnswer:
        query = transporter_data.insert().values(
            inn=transporter.inn,
            kpp=transporter.kpp,
            ogrn=transporter.ogrn,
            name=transporter.name,
            date_of_formation=transporter.date_of_formation,
            director=transporter.director,
            legal_address=transporter.legal_address,
            address=transporter.address,
            email=transporter.email,
            telephone=transporter.telephone,
            payment_account=transporter.payment_account,
            corporate_account=transporter.corporate_account,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        try:
            await self.database.execute(query)
            # check for data insertion, is data with new inn in the table
            query = transporter_data.select().where(transporter_data.c.inn == transporter.inn)
            new_transporter = await self.database.fetch_one(query)

            if not new_transporter:
                message: str = "Transporter can't be inserted. Please try it again."
                result = EndpointAnswer(status="success", message=message)
                logger.info(message)
            else:
                message: str = f"New transporter with inn:'{transporter.inn}' was created."
                result = EndpointAnswer(status="success", message=message, result=new_transporter)
                logger.info(message)
        except Exception as e:
            message: str = str(e)
            result = EndpointAnswer(status="fail", message=message)
            logger.error(message)

        return result

    @logger.catch
    async def get_all_transporters(self, limit: int = 100, skip: int = 0) -> EndpointAnswer:
        query = transporter_data.select().limit(limit).offset(skip)
        try:
            transporter_list = await self.database.fetch_all(query)
            transporter_list_object = []
            for c in transporter_list:
                transporter_list_object.append(TransporterSchema.parse_obj(c))
            message: str = "List of transporters is created."
            result = EndpointAnswer(status="success", message=message, result=transporter_list_object)
            logger.info(message)
        except Exception as e:
            message: str = str(e)
            result = EndpointAnswer(status="fail", message=message)
            logger.error(message)

        return result

    @logger.catch
    async def get_transporter_by_inn(self, transporter_inn: str) -> EndpointAnswer:
        query = transporter_data.select().where(transporter_data.c.inn == transporter_inn)
        try:
            transporter = await self.database.fetch_one(query=query)
            if transporter:
                transporter_obj = TransporterSchema.parse_obj(transporter)
                message = f"Return transporter with inn {transporter_inn}"
                result = EndpointAnswer(status="success", message=message, result=transporter_obj)
                logger.info(message)
            else:
                message = f"There is no transporter with inn {transporter_inn}"
                result = EndpointAnswer(status="success", message=message)
                logger.info(message)
        except Exception as e:
            message: str = str(e)
            result = EndpointAnswer(status="fail", message=message)
            logger.error(message)

        return result

    @logger.catch
    async def get_transporter_by_email(self, transporter_email: str) -> EndpointAnswer:
        query = transporter_data.select().where(transporter_data.c.email == transporter_email).first()

        try:
            transporter = await self.database.fetch_one(query=query)
            if transporter:
                transporter_obj = TransporterSchema.parse_obj(transporter)
                message = f"Return transporter with email {transporter_email}"
                result = EndpointAnswer(status="success", message=message, result=transporter_obj)
                logger.info(message)
            else:
                message = f"There is no transporter with email {transporter_email}"
                result = EndpointAnswer(status="success", message=message)
                logger.info(message)
        except Exception as e:
            message: str = str(e)
            result = EndpointAnswer(status="fail", message=message)
            logger.error(message)

        return result

    @logger.catch
    async def update_transporter_by_inn(self, transporter_inn: str, transporter: TransporterSchema) -> EndpointAnswer:
        updated_transporter = TransporterSchema(
            inn=transporter_inn,
            kpp=transporter.kpp,
            ogrn=transporter.ogrn,
            name=transporter.name,
            date_of_formation=transporter.date_of_formation,
            director=transporter.director,
            legal_address=transporter.legal_address,
            address=transporter.address,
            email=transporter.email,
            telephone=transporter.telephone,
            payment_account=transporter.payment_account,
            corporate_account=transporter.corporate_account,
            updated_at=datetime.utcnow()
        )

        values = {**updated_transporter.dict()}
        values.pop("created_at")
        values.pop("inn")
        query = transporter_data.update().where(transporter_data.c.inn == transporter_inn).values(**values)

        try:
            await self.database.execute(query)
            message: str = f"Transporter with inn:'{transporter_inn}' was updated."
            result = EndpointAnswer(status="success", message=message, result=updated_transporter)
            logger.info(message)
        except Exception as e:
            message: str = str(e)
            result = EndpointAnswer(status="fail", message=message)
            logger.error(message)

        return result

    @logger.catch
    async def delete_transporter_by_inn(self, transporter_inn: str) -> EndpointAnswer:
        query = transporter_data.delete().where(transporter_data.c.inn == transporter_inn)
        try:
            await self.database.execute(query)
            message: str = f"Transporter with inn:'{transporter_inn}' was deleted."
            result = EndpointAnswer(status="success", message=message)
            logger.info(message)
        except Exception as e:
            message: str = str(e)
            result = EndpointAnswer(status="fail", message=message)
            logger.error(message)

        return result

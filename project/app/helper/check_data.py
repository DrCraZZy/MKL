from sqlalchemy import Table
from databases import Database
from project.app.helper.log import logger
from project.app.helper.message_parser import parse_message


async def is_inn_exists(inn: str, table: Table, database: Database) -> bool:
    query = table.select().where(table.c.inn == inn)
    try:
        item = await database.fetch_one(query=query)
        if item:
            return True
        return False
    except Exception as e:
        logger.error(parse_message(str(e)))
        return False

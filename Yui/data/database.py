# Copyright (c) 2021 Itz-fork

from sqlite3 import connect


class Yui_Database():
    """
    Database of Yui Chat bot
        This database won't be used if you're hosting this on heroku
    """

    def __init__(self) -> None:
        self.yui_db = connect("yui-x.db")
        self.curs = self.yui_db.cursor()
        # Creates a table for storing ai engine details
        self.curs.execute(
            """
            CREATE TABLE
            IF NOT EXISTS
            engine (engine_name text)
            """
        )

    async def set_engine(self, engine_name):
        is_exists = await self.get_engine()
        if not is_exists:
            self.curs.execute(
                """
                INSERT INTO engine(engine_name)
                VALUES (?)
                """, (engine_name,)
            )
        else:
            self.curs.execute(
                """
                UPDATE engine
                SET engine_name=?
                """, (engine_name,)
            )
        return self.yui_db.commit()
    
    async def get_engine(self):
        selct = self.curs.execute(
            """
            SELECT engine_name
            FROM engine
            """
        ).fetchone()
        if selct:
            return selct[0]
        else:
            return None
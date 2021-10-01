import db_base as db

class quizDB(db.DBbase):

    def __init__(self):
        super().__init__("question.sqlite")

    def add(self, question,answer,trickA,trickb,trickc):
        # insert in to part (name) values ()
        try:
            self.connect()
            super().get_cursor.execute("""insert into questions (question,answer,trickA,trickb,trickc) values (?,?,?,?,?);""", (question,answer,trickA,trickb,trickc))
            super().get_connection.commit()
            super().close_db()
            print(question, "was added to the parts collum")
        except Exception as a:
            print("something did not go right: ", a)
    def fetch(self, id):
        #trickA
        try:
            self.connect()
            if id is not None:
                question =  super().get_cursor.execute("""select question from questions where id = ?;""",(id,)).fetchone()
                answer = super().get_cursor.execute("""select answer from questions where id = ?;""", (id,)).fetchone()
                trick1 = super().get_cursor.execute("""select trickA from questions where id = ?;""", (id,)).fetchone()
                trick2 = super().get_cursor.execute("""select trickb from questions where id = ?;""", (id,)).fetchone()
                trick3 = super().get_cursor.execute("""select trickc from questions where id = ?;""", (id,)).fetchone()
                return [str(question).strip('( , ) \' '),str(answer).strip('( , ) \' '),str(trick1).strip('( , ) \' '),str(trick2).strip('( , ) \' '),str(trick3).strip('( , ) \' ')]

        except Exception as a:
            print("something done goofed ", a)
        finally:
            super().close_db()
    def highest_id(self):
        try:
            self.connect()
            return super().get_cursor.execute("SELECT id FROM questions ORDER BY id DESC LIMIT 1;").fetchone()
        except Exception as a:
            print("something went wrong: ",a)
        finally:
            super().close_db()
    def make_database(self):
        sql = """
        DROP TABLE IF EXISTS questions;

        create table questions(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        question text not null,
        answer text not null,
        trickA text not null,
        trickb text not null,
        trickc text not null);
        """

        super().execute_script(sql)


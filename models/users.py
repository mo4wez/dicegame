from peewee import Model, SqliteDatabase, CharField

db = SqliteDatabase(r'C:\Users\moawe\Desktop\dicegame\models\db\users.db')

class User(Model):
    chat_id = CharField(unique=True)
    username = CharField(null=True)
    joined_at = CharField()
    coins = CharField()
    invited_users = CharField()


    class Meta:
        database = db

db.connect()
db.create_tables([User], safe=True)
from peewee import Model, SqliteDatabase, CharField, TextField # type: ignore

db = SqliteDatabase('translations.db')

class TranslationModel(Model):
    text = TextField()
    base_lang = CharField()
    final_lang = CharField()
    translation = TextField(null=True)

    class Meta:
        database = db #object relational mapper

db.create_tables([TranslationModel])

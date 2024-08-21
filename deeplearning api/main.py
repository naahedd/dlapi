from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel, field_validator
import tasks


app = FastAPI()

languages = ["English", "French", "German"]

class Translation(BaseModel):
    text: str
    base_lang: str
    final_lang: str

    @field_validator('base_lang', 'final_lang')
    def valid_lang(cls, lang):
        if lang not in languages:
            raise ValueError("Invalid Language")
        return lang

## Route 1: / ##{"messsage": "Hello Wrld"}
@app.get("/")
def get_root():
    return {"message": "Hello Wrld"}


## Route 2: /translate
@app.post("/translate")
def post_translation(t: Translation, background_tasks: BackgroundTasks): #run translation in the background
    # store the translation
    # run translation in background
    t_id = tasks.store_translation(t)
    background_tasks.add_task(tasks.run_translation, t_id)
    return {"task_id": t_id}

## Route 3: /results
@app.get("/results")
def get_translation(t_id: int):
    return {"translation": tasks.final_translation(t_id)}

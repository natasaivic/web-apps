from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
  return {"message": "Hello World"}


# To start the server, you need to run the following command:
# uvicorn main:app --reload
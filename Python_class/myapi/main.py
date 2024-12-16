from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def main():
    return {"res":"hello 1-4 world"}
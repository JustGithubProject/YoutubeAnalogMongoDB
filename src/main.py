from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import (
    user_router,
    video_router,
    auth_router
)

from config import create_database_and_collections


app = FastAPI(
    title="YoutubeAnalogAPI"
)

# Include routes to app
app.include_router(user_router.router)
app.include_router(video_router.router)
app.include_router(auth_router.auth_router)


origins = [
    "http://172.18.0.4:3000",
    "http://0.0.0.0:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
    create_database_and_collections()






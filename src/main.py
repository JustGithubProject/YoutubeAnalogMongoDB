from fastapi import FastAPI

from routes import (
    user_router,
    video_router
)


app = FastAPI(
    title="YoutubeAnalogAPI"
)

# Include routes to app
app.include_router(user_router.router)
app.include_router(video_router.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)










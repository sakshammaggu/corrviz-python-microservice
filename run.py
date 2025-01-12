import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

server_port = int(os.getenv("PORT", 8001))

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=server_port, reload=True)
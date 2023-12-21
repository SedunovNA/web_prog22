from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import uvicorn
load_dotenv()
from accountr.settings import settings
uvicorn.run(    'accountr.app:app',
    host=settings.server_host,
    port=settings.server_port,
    reload=True,)



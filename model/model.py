from typing import Optional
from pydantic import BaseModel

class Config(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    host: Optional[str] = None
    port: Optional[int] = 22
    is_using_proxy: Optional[bool] = False
    proxy_host: Optional[str] = None
    proxy_port: Optional[int] = 8080

class Connection(BaseModel):
    config: Config
    is_connected: bool
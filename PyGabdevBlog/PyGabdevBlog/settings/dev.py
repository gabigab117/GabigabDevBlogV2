from .base import *
from dotenv import load_dotenv

load_dotenv()

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]


try:
    from .local import *
except ImportError:
    pass



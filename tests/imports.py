"""
This module tests that all of orca can be imported, mostly to help reduce issues
with untested code that will not even parse/run on Py2/3
"""
from orca.api.client import *
from orca.api.http import *
from orca.api.ratelimit import *
from orca.bot.bot import *
from orca.bot.command import *
from orca.bot.parser import *
from orca.bot.plugin import *
from orca.bot.storage import *
from orca.gateway.client import *
from orca.gateway.events import *
from orca.gateway.ipc import *
from orca.gateway.packets import *

# Not imported, GIPC is required but not provided by default
# from orca.gateway.sharder import *
from orca.types.base import *
from orca.types.channel import *
from orca.types.guild import *
from orca.types.invite import *
from orca.types.message import *
from orca.types.permissions import *
from orca.types.user import *
from orca.types.voice import *
from orca.types.webhook import *
from orca.util.backdoor import *
from orca.util.config import *
from orca.util.functional import *
from orca.util.hashmap import *
from orca.util.limiter import *
from orca.util.logging import *
from orca.util.serializer import *
from orca.util.snowflake import *
from orca.util.websocket import *

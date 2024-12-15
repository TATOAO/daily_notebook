

# Window event loop 需要额外配置 

import asyncio
import sys

if sys.platform:
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

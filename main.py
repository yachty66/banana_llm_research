import asyncio
from scraper import lmsys, tatsu_lab, huggingface
import nest_asyncio

# Apply nest_asyncio to enable support for asyncio event loops
nest_asyncio.apply()

# Call the main function from each module concurrently
asyncio.run(asyncio.gather(
    lmsys.main(),
    tatsu_lab.main(),
    huggingface.main()
))
from ArchMusic import archdb
from ArchMusic.Helpers import remove_active_chat


async def _clear_(chat_id):
    try:
        archdb[chat_id] = []
        await remove_active_chat(chat_id)
    except:
        return

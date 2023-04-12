from ArchMusic import archdb


async def put(
    chat_id,
    title,
    duration,
    videoid,
    file_path,
    ruser,
    user_id,
):
    put_f = {
        "title": title,
        "duration": duration,
        "file_path": file_path,
        "videoid": videoid,
        "req": ruser,
        "user_id": user_id,
    }
    get = archdb.get(chat_id)
    if get:
        archdb[chat_id].append(put_f)
    else:
        archdb[chat_id] = []
        archdb[chat_id].append(put_f)

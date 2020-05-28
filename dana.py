from telethon import events
from datetime import datetime


@command(pattern="^.dana")
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("Dana 0816264712 Atas Nama David")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit("Pong!\n{}".format(ms))

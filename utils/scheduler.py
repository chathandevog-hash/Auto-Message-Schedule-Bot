import asyncio
from database.mongodb import get_all_running

async def schedule_loop(app):
    print("⏰ Scheduler started")

    while True:
        msgs = get_all_running()

        for m in msgs:
            try:
                await app.send_message(
                    chat_id=m["chat_id"],
                    text=m["text"]
                )
                await asyncio.sleep(m["interval"])
            except Exception as e:
                print("Scheduler error:", e)

        await asyncio.sleep(2)

import asyncio
import importlib
import os
from pyrogram import idle
from aiohttp import web

from FallenMusic import (
    ASS_ID,
    ASS_NAME,
    ASS_USERNAME,
    BOT_ID,
    BOT_NAME,
    BOT_USERNAME,
    LOGGER,
    SUNAME,
    app,
    app2,
    pytgcalls,
)
from FallenMusic.Modules import ALL_MODULES

# Port by SayXSee
PORT = int(os.environ.get("PORT", 8080))

async def handle_requests(request):
    """A simple handler for the web server."""
    return web.Response(text="Bot is running!")

async def start_web_server():
    """Starts the aiohttp web server in the background."""
    app_server = web.Application()
    app_server.router.add_get("/", handle_requests)
    runner = web.AppRunner(app_server)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', PORT)
    await site.start()
    LOGGER.info(f"[•] Web server started on port {PORT}")


async def fallen_startup():
    """Main function to start the bot and its components."""
    # Start the web server as a background task
    web_server_task = asyncio.create_task(start_web_server())

    LOGGER.info("[•] Loading Modules...")
    for module in ALL_MODULES:
        importlib.import_module("FallenMusic.Modules." + module)
    LOGGER.info(f"[•] Loaded {len(ALL_MODULES)} Modules.")

    LOGGER.info("[•] Refreshing Directories...")
    if "downloads" not in os.listdir():
        os.mkdir("downloads")
    if "cache" not in os.listdir():
        os.mkdir("cache")
    LOGGER.info("[•] Directories Refreshed.")

    try:
        await app.send_message(
            SUNAME,
            f"✯ ғᴀʟʟᴇɴ ᴍᴜsɪᴄ ʙᴏᴛ ✯\n\n𖢵 ɪᴅ : {BOT_ID}\n𖢵 ɴᴀᴍᴇ : {BOT_NAME}\n𖢵 ᴜsᴇʀɴᴀᴍᴇ : @{BOT_USERNAME}",
        )
    except:
        LOGGER.error(
            f"{BOT_NAME} failed to send message at @{SUNAME}, please go & check."
        )

    try:
        await app2.send_message(
            SUNAME,
            f"✯ ғᴀʟʟᴇɴ ᴍᴜsɪᴄ ᴀss ✯\n\n𖢵 ɪᴅ : {ASS_ID}\n𖢵 ɴᴀᴍᴇ : {ASS_NAME}\n𖢵 ᴜsᴇʀɴᴀᴍᴇ : @{ASS_USERNAME}",
        )
    except:
        LOGGER.error(
            f"{ASS_NAME} failed to send message at @{SUNAME}, please go & check."
        )

    await app2.send_message(BOT_USERNAME, "/start")

    LOGGER.info(f"[•] Bot Started As {BOT_NAME}.")
    LOGGER.info(f"[•] Assistant Started As {ASS_NAME}.")

    LOGGER.info(
        "[•] \x53\x74\x61\x72\x74\x69\x6e\x67\x20\x50\x79\x54\x67\x43\x61\x6c\x6c\x73\x20\x43\x6c\x69\x65\x6e\x74\x2e\x2e\x2e"
    )
    await pytgcalls.start()
    await idle()


if __name__ == __"main"__:
    asyncio.get_event_loop().run_until_complete(fallen_startup())
    LOGGER.error("Fallen Music Bot Stopped.")

import threading
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from pyrogram import Client
from config.config import BOT_TOKEN, API_ID, API_HASH

from handlers.start import register_start_handler
from handlers.add import register_add_handlers
from handlers.stop import register_stop_handlers
from handlers.status import register_status_handlers
from handlers.broadcast import register_broadcast_handlers


# ================== UPTIME SERVER ==================
class PingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Bot is alive!")

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()


def run_http_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(("0.0.0.0", port), PingHandler)
    server.serve_forever()
# ==================================================

app = Client(
    "AutoMessageBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

register_start_handler(app)
register_add_handlers(app)
register_stop_handlers(app)
register_status_handlers(app)
register_broadcast_handlers(app)

print("🤖 Bot started successfully")

app.run()

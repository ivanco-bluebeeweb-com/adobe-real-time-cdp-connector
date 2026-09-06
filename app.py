"""Extension declaration, capabilities, health check for Adobe Real-Time CDP Connector."""
from __future__ import annotations
import json
from imperal_sdk import ChatExtension, Extension

ext = Extension(
    "adobe-real-time-cdp-connector",
    version="0.1.0",
    display_name="Adobe Real-Time CDP",
    icon="icon.svg",
    capabilities=["adobe_real_time_cdp:manage"],
    description="Official Imperal connector for Adobe Real-Time CDP (C30. Email Marketing & Newsletter). Manage operations securely."
)

chat = ChatExtension(ext)

@ext.health_check
async def health_check(ctx) -> dict:
    raw = await ctx.secrets.get("adobe_real_time_cdp_connections")
    try:
        count = len(json.loads(raw)) if raw else 0
    except Exception:
        count = 0
    return {
        "healthy": True,
        "detail": f"{count} Adobe Real-Time CDP connection(s) configured." if count else "Not connected yet."
    }

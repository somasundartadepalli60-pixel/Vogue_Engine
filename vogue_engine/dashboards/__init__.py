"""Dashboards package initialization."""
from vogue_engine.dashboards.crypto import StatelessTokenManager
from vogue_engine.dashboards.router import app
from vogue_engine.dashboards.user import user_router, REPORT_CACHE
from vogue_engine.dashboards.admin import admin_router

__all__ = [
    "StatelessTokenManager",
    "app",
    "user_router",
    "admin_router",
    "REPORT_CACHE",
]

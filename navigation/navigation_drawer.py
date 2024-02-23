import flet as ft
from typing import List

def navigation_drawer_open_method(controls: List[ft.Control], on_change):
    drawer = ft.NavigationDrawer(
        controls=controls,
        on_change=on_change
    )
    
    async def open_drawer(e):
        e.control.page.drawer = drawer
        drawer.open = True
        await e.control.page.update_async()
    
    return open_drawer
        
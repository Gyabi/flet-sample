import flet as ft
from map.flat_map import FletMap

def map() -> ft.Control:
    list_view = ft.ListView(
        controls=[
            FletMap(
                expand=True,
                latitude=38.8749,
                longtitude=-122.4194,
                zoom=12,
                screenView=[8,4]
            )
        ]
    )
    
    return list_view
import flet as ft
from navigation import navigation_drawer
from framework.navigation_view import navigation_view, NavigationContent
from map.map import map
from sample.sample import SampleControl

async def main(page: ft.Page):
    page.title = "Flet Sample"

    page.fonts = {
        "Roboto Mono": "RobotoMono-VariableFont_wght.ttf",
    }
    
    
        
    view = navigation_view(
        page=page,
        contents=[
            NavigationContent(title="Item 1", icon=ft.icons.ADD_TO_HOME_SCREEN_SHARP, view=map()),
            NavigationContent(title="Item 2", icon=ft.icons.ADD_COMMENT, view=ft.Text("Item 2")),
            NavigationContent(title="Item 3", icon=ft.icons.ADD_COMMENT, view=SampleControl())
        ]
    )
    
    await page.add_async(view)



if __name__ == "__main__":
    ft.app(target=main)
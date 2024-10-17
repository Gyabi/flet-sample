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
    
    
        
    # view = navigation_view(
    #     page=page,
    #     contents=[
    #         NavigationContent(title="Item 1", icon=ft.icons.ADD_TO_HOME_SCREEN_SHARP, view=map()),
    #         NavigationContent(title="Item 2", icon=ft.icons.ADD_COMMENT, view=ft.Text("Item 2")),
    #         NavigationContent(title="Item 3", icon=ft.icons.ADD_COMMENT, view=SampleControl())
    #     ]
    # )
    
    # await page.add_async(view)
    
    button1 = ft.CupertinoFilledButton("sample1", padding=2)
    button2 = ft.CupertinoFilledButton("sample2", padding=2)
    button3 = ft.CupertinoFilledButton("sample3", padding=2)
    
    col = ft.Column([
        ft.Text("sample"),
        ft.Container(content=
            ft.Column(
                [
                    ft.Row([
                        ft.Row([
                            ft.Text("aaaaaaaa", expand=1),
                            ft.Text("lasdjflsa", expand=1),
                        ], expand=2),
                        ft.Row([
                            button1,
                            button2,
                            button3,
                        ], expand=3, alignment=ft.MainAxisAlignment.CENTER)
                    ]),
                    ft.Row([
                        ft.Row([
                            ft.Text("aaaaaaaa", expand=1),
                            ft.Text("lasdjflsa", expand=1),
                        ], expand=2),
                        ft.Row([
                            button1,
                            button2,
                            button3,
                        ], expand=3, alignment=ft.MainAxisAlignment.CENTER)
                    ]),
                    ft.Row([
                        ft.Row([
                            ft.Text("aaaaaaaa", expand=1),
                            ft.Text("lasdjflsa", expand=1),
                        ], expand=2),
                        ft.Row([
                            button1,
                            button2,
                            button3,
                        ], expand=3, alignment=ft.MainAxisAlignment.CENTER)
                    ]),
                    ft.Row([
                        ft.Row([
                            ft.Text("aaaaaaaa", expand=1),
                            ft.Text("lasdjflsa", expand=1),
                        ], expand=2),
                        ft.Row([
                            button1,
                            button2,
                            button3,
                        ], expand=3, alignment=ft.MainAxisAlignment.CENTER)
                    ]),
                    ft.Row([
                        ft.Row([
                            ft.Text("aaaaaaaa", expand=1),
                            ft.Text("lasdjflsa", expand=1),
                        ], expand=2),
                        ft.Row([
                            button1,
                            button2,
                            button3,
                        ], expand=3, alignment=ft.MainAxisAlignment.CENTER)
                    ]),
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER,
                scroll=ft.ScrollMode.ALWAYS
            ),
            bgcolor=ft.colors.AMBER,
            expand=1,
            padding=10,),
        ft.Container(content=ft.Row([]), bgcolor=ft.colors.INDIGO, expand=4),
    ], expand=True)


    page.add(col)


if __name__ == "__main__":
    ft.app(target=main)
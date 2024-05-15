from ReactiveText import ReactiveText
from state import State
import flet as ft

async def main(page: ft.Page):
    page.title = "Flet Sample"

    page.fonts = {
        "Roboto Mono": "RobotoMono-VariableFont_wght.ttf",
    }

    title = State("Sample Control")
    view = ReactiveText(title)

    await page.add_async(view)
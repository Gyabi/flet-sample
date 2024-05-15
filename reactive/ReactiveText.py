import flet as ft
from state import State

class ReactiveText(ft.UserControl):
    def __init__(self, title: State[str]) -> None:
        super().__init__()
        self.title:State[str] = title
        self.title.bind(self.update)
        
    def build(self):
        self.control = ft.Text(self.title.get())
        
        # クリックしたらタイトルを変更し、再描画する
        return ft.CupertinoButton(
            content=self.control,
            on_click=self.on_click
        )
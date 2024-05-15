from flet import UserControl, Text, CupertinoButton


class SampleControl(UserControl):
    def __init__(self):
        self.title = "Sample Control"
        super().__init__()
        
    def build(self):
        self.a = Text(self.title)
        
        # クリックしたらタイトルを変更し、再描画する
        return CupertinoButton(
            content=self.a,
            on_click=self.on_click
        )
        
    def on_click(self, e):
        self.title = "Clicked!"
        self.a.update()
        

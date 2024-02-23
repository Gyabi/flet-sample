import flet as ft
from typing import List
from navigation import navigation_drawer

class NavigationContent():
    def __init__(self, title:str, icon:str, view:ft.Control) -> None:
        """constructor

        Args:
            title (str): Navigationに表示するタイトル
            icon (str): Navigationに表示するアイコン
            view (ft.Control): Navigationをクリックしたときに表示する要素
        """
        self.title = title
        self.icon = icon
        self.view = view
    
    
def navigation_view(page: ft.Page, contents:List[NavigationContent]) -> ft.Control:
    # メインの表示エリアを定義(初期状態はcontentsの先頭のviewを表示)
    main_view = ft.Column(
        controls=[contents[0].view if len(contents) > 0 else None]
    )
    
    # navigationメニューを作成
    navigation_menu_contents: List[ft.Control] = [
        ft.NavigationDrawerDestination(
            icon=content.icon,
            label=content.title,
        ) for i, content in enumerate(contents)
    ]
    
    # 押下時の処理
    async def on_click_navigation_drawer_item(e:ft.ControlEvent):
        index = int(e.data)
        if len(contents) <= index:
            return
        # drawerを閉じる
        page.drawer = None
        # indexに一致したコンテンツを表示するように変更する
        main_view.controls = [contents[index].view]
        # 画面の更新
        await page.update_async()
        
    
    # 作成したメニューを元に、navigation_drawerを作成
    on_click_navigation_drawer_button = navigation_drawer.navigation_drawer_open_method(
        controls=navigation_menu_contents,
        on_change=on_click_navigation_drawer_item
    )
    
    # ハンバーガーボタンへ設定
    humburger = ft.TextButton(
        icon=ft.icons.MENU_SHARP,
        on_click=on_click_navigation_drawer_button
    )
    
    # 単一コントロールにまとめる
    col = ft.Column(
        controls=[
            humburger,
            main_view
        ]
    )
    
    return col
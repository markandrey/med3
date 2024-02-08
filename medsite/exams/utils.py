menu = [{'title': "О сайте", 'url_name': 'home'},
        {'title': "Показать все данные", 'url_name': 'all'},
        {'title': "Переслать фото результата", 'url_name': 'send_info'},
        ]


# side_menu = [
#         {'title': "Питание", 'url_name': '#'},
#         {'title': "Физическая активность", 'url_name': '#'},
#         {'title': "ИМТ", 'url_name': '#'},
#         {'title': "О препаратах", 'url_name': '#'},
# ]


cats_db = [
    {'id': 1, 'name': 'Питание'},
    {'id': 2, 'name': 'Физическая активность'},
    {'id': 3, 'name': 'ИМТ'},
    {'id': 4, 'name': 'О препаратах'},
]


class DataMixin:
    title_page = None
    message = None
    cat_selected = None
    extra_context = {}

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page

        if self.message:
            self.extra_context['message'] = self.message

        if self.cat_selected is not None:
            self.extra_context['cat_selected'] = self.cat_selected

    def get_mixin_context(self, context, **kwargs):
        context.update(kwargs)
        return context

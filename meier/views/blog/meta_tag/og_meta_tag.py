class OpenGraphMetaTagGenerator(object):
    def __init__(
        self,
        site_name='',
        title='',
        description='',
        url='',
        image='',
        type_='website',
    ):
        self.site_name = site_name if site_name else ''
        self.title = title if title else ''
        self.description = description if description else ''
        from meier.commons.utils import clean_html

        self.description = clean_html(self.description)

        self.url = url if url else ''
        self.image = image if image else ''
        self.types = type_ if type_ else 'website'

    def __call__(self):
        template = '<meta property="og:{}" content="{}"/>'
        meta_html_list = []
        for k, v in vars(self).items():
            meta_html_list.append(template.format(k, v))

        return '\n'.join(meta_html_list)

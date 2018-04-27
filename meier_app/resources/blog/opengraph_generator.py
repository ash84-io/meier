
class OpenGraphGenerator(object):
    def __init__(self, site_name='', title='', description='', url='', image='', type='website'):
        self.site_name = site_name if site_name else ''
        self.title = title if title else ''
        self.description = description if description else ''
        self.url = url if url else ''
        self.image = image if image else ''
        self.type = type if type else 'website'

    def __call__(self):
        template = '<meta property="og:{}" content="{}"/>'
        meta_html_list = []
        for k, v in vars(self).items():
            meta_html_list.append(template.format(k, v))

        return '\n'.join(meta_html_list)



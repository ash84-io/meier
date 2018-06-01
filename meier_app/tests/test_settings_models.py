from mixer.backend.flask import mixer
from meier_app.extensions import db
from meier_app.models.settings import Settings
from meier_app.tests.base import BaseModelTestCase
from meier_app.tests.base import app as mock_app


class TestSettingsModels(BaseModelTestCase):

    def setUp(self):
        super(TestSettingsModels).setUp()
        with mock_app.app_context():
            ran_setting = mixer.blend(Settings)

    def test_insert(self):
        with mock_app.app_context():
            spec_setting = mixer.blend(Settings,
                                       blog_title='test',
                                       blog_desc='test',
                                       theme='test',
                                       domain='test')

            assert spec_setting.blog_title == 'test'
            assert spec_setting.blog_desc == 'test'
            assert spec_setting.theme == 'test'
            assert spec_setting.domain == 'test'
            assert spec_setting.post_per_page == 10

            assert Settings.query.count() == 2

    def test_update(self):
        with mock_app.app_context():
            s = Settings.query.scalar()
            s.blog_title = "blog"
            s.blog_desc = "blog"
            s.post_per_page = 0
            db.session.commit()
            assert s.blog_title == 'blog'
            assert s.blog_desc == 'blog'
            assert s.post_per_page == 0

    def test_delete(self):
        with mock_app.app_context():
            s = Settings.query.scalar()
            db.session.delete(s)
            db.session.commit()
            assert Settings.query.count() == 0

    def test_for_dict(self):
        with mock_app.app_context():
            spec_setting = mixer.blend(Settings,
                                       blog_title='test',
                                       blog_desc='test',
                                       theme='test',
                                       domain='test')

            test_dict = {
                'blog_title': "test",
                'blog_desc': "test",
                'theme': "test",
                'post_per_page': 10,
                'domain': "test",
            }
            assert spec_setting.for_dict == test_dict



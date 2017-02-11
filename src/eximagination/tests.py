from __future__ import print_function

import os
import unittest

from . import obtain_image
from .helpers import project_dir

__title__ = 'eximagination.tests'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'

LOG_INFO = True


def log_info(func):
    """Log some useful info."""
    if not LOG_INFO:
        return func

    def inner(self, *args, **kwargs):
        result = func(self, *args, **kwargs)

        print('\n\n%s' % func.__name__)
        print('============================')
        if func.__doc__:
            print('""" %s """' % func.__doc__.strip())
        print('----------------------------')
        if result is not None:
            print(result)
        print('\n++++++++++++++++++++++++++++')

        return result
    return inner


class EximaginationUtilsTest(unittest.TestCase):
    """Tests of ``eximagination.utils.obtain_image`` function."""

    def setUp(self):
        """Set up."""
        self.image_url = 'http://www.google.com/intl/en/images/logo.gif'
        self.force_update = False

        # Where eximagination cached images will be stored
        self.media_root = project_dir('tmp')
        self.media_url = '/tmp/'  # Media URL for stored images
        self.media_relative_root = 'tmp/'  # Relative root for images
        # After 30 days we re-fetch the file anyway.
        self.expiration_interval = 2592000
        self.debug = True

        try:
            os.stat(self.media_root)
        except Exception:
            os.mkdir(self.media_root)

    @log_info
    def test_01_obtain_image(self):
        """Test obtain image."""
        file_data = obtain_image(
            image_source=self.image_url,
            save_to=self.media_root,
            media_url=self.media_relative_root,
            force_update=self.force_update,
            expiration_interval=self.expiration_interval,
            debug=self.debug
        )

        try:
            filename = file_data[0]
            ei_width = file_data[1]  # Original width of the obtained image
            ei_height = file_data[2]  # Original height of the obtained image
        except Exception as err:
            print(file_data)
            print(err)
            filename = None
            ei_width = None
            ei_height = None

        res = {
            'filename': filename,
            'ei_width': ei_width,
            'ei_height': ei_height
        }

        self.assertTrue(filename is not None)
        self.assertTrue(ei_width is not None)
        self.assertTrue(ei_height is not None)

        return res


# Skipping from non-Django tests.
if os.environ.get("DJANGO_SETTINGS_MODULE", None):
    from django.conf import settings
    from django.test import LiveServerTestCase
    from django.core.management import call_command

    from selenium import webdriver
    from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

    class EximaginationTemplatetagsTest(LiveServerTestCase):
        """Tests of ``exinagination.templatetags.eximaginate`` module."""

        @classmethod
        def setUpClass(cls):
            """Set up."""
            firefox_bin_path = getattr(settings, 'FIREFOX_BIN_PATH', None)
            phantom_js_executable_path = getattr(
                settings, 'PHANTOM_JS_EXECUTABLE_PATH', None
            )
            if phantom_js_executable_path is not None:
                if phantom_js_executable_path:
                    cls.selenium = webdriver.PhantomJS(
                        executable_path=phantom_js_executable_path
                    )
                else:
                    cls.selenium = webdriver.PhantomJS()
            elif firefox_bin_path:
                binary = FirefoxBinary(firefox_bin_path)
                cls.selenium = webdriver.Firefox(firefox_binary=binary)
            else:
                cls.selenium = webdriver.Firefox()
            super(EximaginationTemplatetagsTest, cls).setUpClass()

        @classmethod
        def tearDownClass(cls):
            """Tear down."""
            try:
                cls.selenium.quit()
            except Exception as err:
                print(err)
            super(EximaginationTemplatetagsTest, cls).tearDownClass()
            call_command('flush', verbosity=0, interactive=False,
                         reset_sequences=False,
                         allow_cascade=False,
                         inhibit_post_migrate=False)

        @log_info
        def test_templatetags(self):
            """Test template tags."""
            workflow = []

            self.selenium.get(self.live_server_url)

            img1 = self.selenium.find_element_by_id("image1")
            self.assertTrue(img1.get_attribute('src').endswith('gif'))
            workflow.append(img1.get_attribute('src'))

            img2 = self.selenium.find_element_by_id("image2")
            self.assertTrue(img2.get_attribute('src').endswith('gif'))
            workflow.append(img2.get_attribute('src'))

            return workflow


if __name__ == "__main__":
    # Tests
    unittest.main()

from __future__ import print_function

__title__ = 'eximagination.utils'
__version__ = '0.7'
__build__ = 0x000007
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'

import unittest
import os

PROJECT_DIR = lambda base : os.path.join(os.path.dirname(__file__), base).replace('\\','/')

from eximagination import obtain_image

PRINT_INFO = True

def print_info(func):
    """
    Prints some useful info.
    """
    if not PRINT_INFO:
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
    """
    Tests of ``eximagination.utils.obtain_image`` function.
    """
    def setUp(self):
        self.image_url = 'http://www.google.com/intl/en/images/logo.gif'
        self.force_update = False
        
        self.MEDIA_ROOT = PROJECT_DIR('tmp') # Where eximagination cached images will be stored
        self.MEDIA_URL = '/tmp/' # Media URL for stored images
        self.MEDIA_RELATIVE_ROOT = 'tmp/' # Relative root for images
        self.EXPIRATION_INTERVAL = 2592000 # After 30 days we re-fetch the file anyway.
        self.DEBUG = True

        try:
            os.stat(self.MEDIA_ROOT)
        except:
            os.mkdir(self.MEDIA_ROOT)

    @print_info
    def test_01_obtain_image(self):
        """
        Test obtain image.
        """
        #import ipdb; ipdb.set_trace()
        file_data = obtain_image(
            image_source = self.image_url,
            save_to = self.MEDIA_ROOT,
            media_url = self.MEDIA_RELATIVE_ROOT,
            force_update = self.force_update,
            expiration_interval = self.EXPIRATION_INTERVAL,
            debug = self.DEBUG
            )

        try:
            filename = file_data[0]
            ei_width = file_data[1] # Original width of the obtained image
            ei_height = file_data[2] # Original height of the obtained image
        except Exception as e:
            print(file_data)
            print(e)
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
    from django.test import LiveServerTestCase

    from selenium.webdriver.firefox.webdriver import WebDriver

    class EximaginationTemplatetagsTest(LiveServerTestCase): #unittest.TestCase
        """
        Tests of ``exinagination.templatetags.eximaginate`` module.
        """
        @classmethod
        def setUpClass(cls):
            cls.selenium = WebDriver()
            super(EximaginationTemplatetagsTest, cls).setUpClass()

        @classmethod
        def tearDownClass(cls):
            cls.selenium.quit()
            super(EximaginationTemplatetagsTest, cls).tearDownClass()

        @print_info
        def test_templatetags(self):
            """
            Test template tags.
            """
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

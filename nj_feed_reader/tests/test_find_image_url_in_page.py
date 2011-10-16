from django.test import TestCase
from nj_feed_reader.fetch_twitter import find_image_url_in_page

class TestFindImageUrlInPage(TestCase):
    def test_find_image_url_in_twitpic_page__found(self):
        page_url = 'http://twitpic.com/6m2t75'
        image_url = find_image_url_in_page(page_url)
        expected_url = 'http://s1.proxy03.twitpic.com/photos/large/399879761.jpg'
        self.assertEqual(expected_url, image_url)

    def test_find_image_url_in_lockerz_page__found(self):
        page_url = 'http://lockerz.com/s/139778407'
        image_url = find_image_url_in_page(page_url)
        expected_url = 'http://c0013959.cdn1.cloudfiles.rackspacecloud.com/x2_854d967'
        self.assertEqual(expected_url, image_url)

    def test_find_image_url_in_yfrog_page__found(self):
        page_url = 'http://yfrog.com/kiqyuofj'
        image_url = find_image_url_in_page(page_url)
        expected_url = 'http://desmond.yfrog.com/Himg738/scaled.php?tn=0&server=738&filename=qyuof.jpg&xsize=640&ysize=640'
        self.assertEqual(expected_url, image_url)

    def test_find_image_url_in_molome_page__found(self):
        page_url = 'http://molo.me/p/2uvG77'
        image_url = find_image_url_in_page(page_url)
        expected_url = 'http://p.molo.me/2uvG77?'
        self.assertIn(expected_url, image_url)

    def test_find_image_url_in_picplz_page__found(self):
        page_url = 'http://picplz.com/user/ajaxming/pic/t28r9/'
        image_url = find_image_url_in_page(page_url)
        expected_url = 'http://s1.i1.picplzthumbs.com/upload/img/46/8e/d0/468ed098796b97a0fc28ee8bb47462f098dfe660_400r.jpg'
        self.assertEqual(expected_url, image_url)

    def test_find_image_url_in_instagram_page__found(self):
        page_url = 'http://instagr.am/p/Ncasw/'
        image_url = find_image_url_in_page(page_url)
        expected_url = 'http://distillery.s3.amazonaws.com/media/2011/09/18/4df983fd4f6d4496bf0a496ab30f74e0_7.jpg'
        self.assertEqual(expected_url, image_url)

    def test_find_image_url_in_flickr_page__found(self):
        page_url = 'http://www.flickr.com/photos/63701352@N06/6158805817/'
        image_url = find_image_url_in_page(page_url)
        expected_url = 'http://farm7.static.flickr.com/6151/6158805817_2c547be8aa_z.jpg'
        self.assertEqual(expected_url, image_url)

    def test_find_image_url_in_twitgoo_page__found(self):
        page_url = 'http://twitgoo.com/4j88ih'
        image_url = find_image_url_in_page(page_url)
        expected_url = 'http://i54.twitgoo.com/1zpp35u.jpg'
        self.assertEqual(expected_url, image_url)

    def test_find_image_url_in_imgly_page__found(self):
        page_url = 'http://img.ly/8mZP'
        image_url = find_image_url_in_page(page_url)
        expected_url = 'http://s3.amazonaws.com/imgly_production/1995025/large.jpg'
        self.assertEqual(expected_url, image_url)

    def test_find_image_url_in_mobypicture_page__found(self):
        page_url = 'http://www.mobypicture.com/user/marnixamsterdam/view/10743416'
        image_url = find_image_url_in_page(page_url)
        expected_url = 'http://a2.img.mobypicture.com/2ea0c3d9b51adeb8e12245db4eebab3a_view.jpg'
        self.assertEqual(expected_url, image_url)

    def test_find_image_url_in_owly_page__found(self):
        page_url = 'http://ow.ly/i/e0gW'
        image_url = find_image_url_in_page(page_url)
        expected_url = 'http://static.ow.ly/photos/normal/e0gW.jpg'
        self.assertEqual(expected_url, image_url)

    def test_find_image_url_in_brizzly_page__found(self):
        page_url = 'http://brizzly.com/pic/2SE5'
        image_url = find_image_url_in_page(page_url)
        expected_url = 'http://pics.brizzly.com/thumb_lg_2SE5.jpg'
        self.assertEqual(expected_url, image_url)

#    def test_find_image_url_in_pic_twitter_page__found(self):
#        page_url = 'http://twitter.com/#!/igoyz/status/114975438018842624/photo/1'
#        image_url = find_image_url_in_page(page_url)
#        expected_url = 'http://p.twimg.com/AZh5jT2CEAAXyR-.jpg'
#        self.assertEqual(expected_url, image_url)


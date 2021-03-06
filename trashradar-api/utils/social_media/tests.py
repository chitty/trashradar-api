import mock
import unittest

from utils.social_media.twitter import Twitter
from twitter import Status, TwitterError


class TwitterTest(unittest.TestCase):
    def setUp(self):
        self.status = Status(
            id=4212713,
            created_at='Fri Jan 26 17:28:19 +0000 2007',
            text='"Select all" and archive your Gmail inbox. '
                 ' The page loads so much faster!'
        )
        self.twitter = Twitter()

    @mock.patch('twitter.Api.PostUpdate')
    def test_status_list_success(self, twitter_mock):
        """
        tweet() will return an array of successful tweets
        """
        twitter_mock.return_value = self.status
        status_list = [self.status.id]

        response = self.twitter.tweet('"Select all" and archive your Gmail inbox. The page loads so much faster!')
        self.assertEqual(status_list, response, 'The status response is different')

    @mock.patch('twitter.Api.PostUpdate')
    def test_status_list_more_than_140_chars(self, twitter_mock):
        """
        If the tweet has more than 140 chars will be split in more tweets and return
        more than one status
        """
        twitter_mock.return_value = self.status

        response = self.twitter.tweet(
            '"Select all" and archive your Gmail inbox. The page loads so much faster!'
            '"Select all" and archive your Gmail inbox. The page loads so much faster!'
        )
        self.assertGreater(len(response), 1, 'The response array has less or equal than one status')

    @mock.patch('twitter.Api.PostUpdate')
    def test_status_with_image(self, twitter_mock):
        """
        If the tweet has an image url should return the status
        """
        twitter_mock.return_value = self.status
        status_list = [self.status.id]

        response = self.twitter.tweet(
            '"Select all" and archive your Gmail inbox. The page loads so much faster!',
            media='https://google.com'
        )
        self.assertEqual(status_list, response, 'The status response is different')

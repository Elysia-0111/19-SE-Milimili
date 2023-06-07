from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import logging
import os

"""上传文件至腾讯云接口"""


class Bucket:
    base_path = os.path.dirname(os.path.dirname(__file__))
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    def __init__(self):
        self.secret_id = 'AKIDGMuJWYRPESUItWn6FIJfXO8zwnbP8h7R'
        self.secret_key = 'Y0MZcZM0VpBRXcj6VpLwcCe8WjnfPAmH'
        self.region = 'ap-beijing'
        self.token = None
        self.scheme = 'https'
        self.config = CosConfig(Region=self.region, SecretId=self.secret_id, SecretKey=self.secret_key,
                                Token=self.token, Scheme=self.scheme)
        self.client = CosS3Client(self.config)

    def upload_video(self, title):
        try:
            self.client.upload_file(
                Bucket='milimili-1317998312',
                LocalFilePath=self.base_path + '/media/' + title,
                Key=title,
            )
        except Exception:
            return -1
        else:
            return 1

    def upload_file(self, title):
        try:
            self.client.upload_file(
                Bucket='milimili-file-1317998312',
                LocalFilePath=self.base_path + '/media/' + title,
                Key=title,
            )
        except Exception:
            return -1
        else:
            return 1

    def delete_video(self, title):
        response = self.client.delete_object(
            Bucket='milimili-1317998312',
            Key=title,
        )

    def get_video_url(self, title):
        url = self.client.get_object_url(
            Bucket='milimili-1317998312',
            Key=title
        )

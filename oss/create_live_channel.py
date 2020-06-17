# -*-encoding=utf-8-*-

from oss2 import *
from oss2.models import *

host = "http://oss-cn-beijing.aliyuncs.com"
accessid = "accessid"
accesskey = "accesskey"
bucket_name = "gaox-av"
channel_name = "videos"
playlist_name = "playlist.m3u8"
auth = Auth(accessid, accesskey)
bucket = Bucket(auth, host, bucket_name)
channel = bucket.create_live_channel(
    channel_name,
    LiveChannelInfo(status='enabled',
                    description='测试使用的直播频道',
                    target=LiveChannelInfoTarget(playlist_name=playlist_name,
                                                 frag_count=1,
                                                 frag_duration=1)))

# 推流频道
print(channel.publish_url)
# 推流签名
print(bucket.sign_rtmp_url(channel_name, playlist_name, 36000))
# 直播地址
print(channel.play_url)

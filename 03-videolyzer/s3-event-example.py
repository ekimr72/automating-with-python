# coding: utf-8
event = {'Records': [{'eventVersion': '2.1', 'eventSource': 'aws:s3', 'awsRegion': 'us-east-1', 'eventTime': '2019-10-29T06:57:45.294Z', 'eventName': 'ObjectCreated:Put', 'userIdentity': {'principalId': 'AWS:AIDATNBMYG635HJC37IEW'}, 'requestParameters': {'sourceIPAddress': '84.248.78.123'}, 'responseElements': {'x-amz-request-id': '3F88255F199656A9', 'x-amz-id-2': 'pXkLZQp/6/XT03gdY7BMo1/Nal1+2vojDqAF2K+6IeLWQQTThNNTuiD/pc6d8/YTnl2d/wae/UI='}, 's3': {'s3SchemaVersion': '1.0', 'configurationId': '6e2a7d1b-7746-4c25-8fb7-e8e3a1d5695e', 'bucket': {'name': 'ekivideolyzervideos123', 'ownerIdentity': {'principalId': 'A10RSZYBZNNWCI'}, 'arn': 'arn:aws:s3:::ekivideolyzervideos123'}, 'object': {'key': 'Pexels+Videos+1416907.mp4', 'size': 2771231, 'eTag': 'd0ecfa5c3ed004bb305587603bba3878', 'sequencer': '005DB7E2E40F6D6325'}}}]}
event
event['Records'][0]
event['Records'][0]['s3']['bucket']['name']
event['Records'][0]['s3']['object']['key']
import urllib
urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])

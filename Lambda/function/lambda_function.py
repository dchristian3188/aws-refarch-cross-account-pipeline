import os
import logging
import boto3
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info('## ENVIRONMENT VARIABLES\r' + json.dumps(dict(**os.environ)))
    logger.info('## EVENT\r' + json.dumps(event))
    return "Hello World! Version: 1"
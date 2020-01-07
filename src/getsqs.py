import boto3

QUEUE_NAME = 'getEntitlementQueue1'
MAIN_QUEUE_URL = 'YOUR_QUEUE_ARN'

def sqs_client():
    sqs = boto3.client('sqs', region_name='YOUR_REGION')
    """ :type : pyboto3.sqs """
    return sqs


def create_sqs_queue():
    return sqs_client().create_queue(
        QueueName=QUEUE_NAME
    )

def send_message_to_queue():
    return sqs_client().send_message(
        QueueUrl=MAIN_QUEUE_URL,
        MessageAttributes={
            'Title': {
                'DataType': 'String',
                'StringValue': 'Message Title'
            },
            'Author': {
                'DataType': 'String',
                'StringValue': 'User'
            },
            'WeeksOn': {
                'DataType': 'Number',
                'StringValue': '6'
            }
        },
        MessageBody='This is my first SQS Message!'
    )


if __name__ == '__main__':
    print(create_sqs_queue())
    print(send_message_to_queue())
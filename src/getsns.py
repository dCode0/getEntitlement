import boto3

TOPIC_NAME = 'MySubscriptionTopic'
TOPIC_ARN = 'YOUR_TOPIC_ARN'
QUEUE_ARN = 'YOUR_QUEUE_ARN'


def sns_client():
    sns = boto3.client('sns', region_name='us-east-1')
    """ :type : pyboto3.sns """
    return sns


def create_topic():
    sns_client().create_topic(
        Name=TOPIC_NAME
    )
def get_topics():
    return sns_client().list_topics()

def create_email_subscription(topic_arn, email_address):
    return sns_client().subscribe(
        TopicArn=topic_arn,
        Protocol='email',
        Endpoint=email_address
    )

def create_sqs_queue_subscription(topic_arn, queue_arn):
    return sns_client().subscribe(
        TopicArn=topic_arn,
        Protocol='sqs',
        Endpoint=queue_arn
    )

def publish_message(topic_arn):
    return sns_client().publish(
        TopicArn=topic_arn,
        Message="Hello, you're receiving this because you've subscribed!"
    )


if __name__ == '__main__':
    create_topic()
    # print(get_topics())
    create_email_subscription(TOPIC_ARN, 'YOUR_EMAIL_ADDRESS')
    create_sqs_queue_subscription(TOPIC_ARN, QUEUE_ARN)
    publish_message(TOPIC_ARN)



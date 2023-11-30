import requests
from bs4 import BeautifulSoup
 
def statusAWS():
   
    servicosStatus = {
        "Amazon API Gateway": "",
        "Amazon AppFlow":"",
        "Amazon AppStream 2.0":"",
        "Amazon Athena":"",
        "Amazon Chime":"",
        "Amazon CloudFront":"",
        "Amazon CloudSearch":"",
        "Amazon CloudWatch Application Insights":"",
        "Amazon CloudWatch Internet Monitor":"",
        "Amazon CloudWatch":"",
        "Amazon CloudWatch Synthetics":"",
        "Amazon Cognito": "",
        "Amazon Data Lifecycle Manager":"",
        "Amazon DataZone":"",
        "Amazon Detective":"",
        "Amazon DevOps Guru":"",
        "Amazon DocumentDB":"",
        "Amazon DynamoDB":"",
        "Amazon EC2 Instance Connect":"",
        "Amazon Elastic Compute Cloud":"",
        "Amazon Elastic Container Registry Public":"",
        "Amazon Elastic Container Registry":"",
        "Amazon Elastic Container Service": "",
        "Amazon Elastic File System":"",
        "Amazon Elastic Load Balancing":"",
        "Amazon Elastic MapReduce":"",
        "Amazon ElastiCache":"",
        "Amazon EMR Serverless":"",
        "Amazon EventBridge":"",
        "Amazon EventBridge Scheduler":"",
        "Amazon FreeRTOS":"",
        "Amazon FSx":"",
        "Amazon GameLift":"",
        "Amazon Glacier": "",
        "Amazon GuardDuty":"",
        "Amazon Inspector":"",
        "Amazon Inter-Region VPC Peering":"",
        "Amazon Keyspaces":"",
        "Amazon Kinesis Analytics":"",
        "Amazon Kinesis Data Streams":"",
        "Amazon Kinesis Firehose":"",
        "Amazon Kinesis Video Streams":"",
        "Amazon Location Service":"",
        "Amazon Macie":"",
        "Amazon Managed Streaming for Apache Kafka":"",
        "Amazon Managed Workflows for Apache Airflow":"",
        "Amazon MemoryDB for Redis":"",
        "Amazon MQ":"",
        "Amazon Neptune":""
        }
 
    link = "https://health.aws.amazon.com/health/status"
 
    requisicao = requests.get(link)
 
    site = BeautifulSoup(requisicao.text, "html.parser")
 
    statusRaiz = str(site.find(class_="awsui_icon_h11ix_109ey_98 awsui_size-normal-mapped-height_h11ix_109ey_151 awsui_size-normal_h11ix_109ey_147 awsui_variant-normal_h11ix_109ey_219"))

    print(statusRaiz)
 
    for p in range(48):
   
        statusRaizStr = str(statusRaiz[p])
 
        open = False
 
        status = ''
 
        for i in statusRaizStr:
            if(i == '>'):
                open = True
            else:
                if(i == '<'):
                    open = False
                else:
                    if(open == True):
                        status += i
 
        status = status.strip()
 
        if(status == 'awsui_icon_1cbgc_socsa_97'):
            respost = True
        else:
            respost = False
 
        for v in servicosStatus:
            servicosStatus[v] = respost
 
    return servicosStatus

print(statusAWS())
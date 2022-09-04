from diagrams import Cluster, Diagram
from diagrams.gcp.analytics import BigQuery, Dataflow, PubSub
from diagrams.gcp.compute import AppEngine, Functions, Run
from diagrams.gcp.database import BigTable
from diagrams.gcp.iot import IotCore
from diagrams.gcp.storage import GCS
from diagrams.aws.compute import ECS, EB
from diagrams.aws.storage import S3

with Diagram("Message Collecting", show=True):
    pubsub = PubSub("pubsub")

    with Cluster("Source of Data"):
        [Run("Game 1"),
         Run("Game 2"),
         Run("Game 3")] >> pubsub
    
    with Cluster("Targets"):
        with Cluster("Data Lake"):
            bq = [BigQuery("bq")]
        with Cluster("Storage"):
            gcs = GCS("storage")

    with Cluster("AWS"):
        ecs = [ECS("Game 4"), EB("Game 5")]
        ecs >> pubsub

    pubsub >> bq 
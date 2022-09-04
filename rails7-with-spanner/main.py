from diagrams import Cluster, Diagram
from diagrams.gcp.analytics import BigQuery, Dataflow, PubSub
from diagrams.gcp.compute import AppEngine, Functions, Run
from diagrams.gcp.network import *
from diagrams.gcp.database import BigTable,Memorystore,Spanner
from diagrams.gcp.operations import Monitoring
from diagrams.gcp.iot import IotCore
from diagrams.gcp.storage import GCS

with Diagram("Cloud Run with Cloud Spanner", show=True):

    lb = LoadBalancing("Google Cloud Load Balancing")
    with Cluster("Data"):
        bq = BigQuery("BigQuery")

    with Cluster("Application"):
        run = Run("user-api")
        spanner = Spanner("game")
    
    monitoring = Monitoring("Logging")
    
    with Cluster("Cache Layer"):
        with Cluster("VPC"):
            redis = Memorystore("Redis")
    
    lb >> run
    run >> spanner
    run >> redis
    run >> monitoring
    monitoring << bq


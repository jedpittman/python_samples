from diagrams import Diagram
from diagrams.aws.compute import EC2

with Diagram("Sample Diagram"):
    EC2("Web")
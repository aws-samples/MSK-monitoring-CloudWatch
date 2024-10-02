# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 08:59:22 2024

@authors: kirkumt, swapnaba
"""

import yaml
import time
import os

###############################################  Input  Parameters########################################
"""
ClusterName     = 'ClusterName'                 #-- your MSK provisioned cluster name
MSKRegion       = 'us-east-1'                   #-- your MSK cluster region
DashboardName   = 'AWS_MSK_Metrics_Dashboard'   #-- Name of the CloudWach dashboard
NumberOfBrokers = 4                             #-- Interger value - Number of brokers in the cluster to be monitored.
Topics          = 'topic1,topic2,topic3'        #-- Comma seperated list of Topic names
"""
###########################################################################################################



ClusterName     = input('MSK provisioned cluster name: ')   #-- your MSK provisioned cluster name
MSKRegion       = input('MSK provisioned cluster region: ')    #-- your MSK cluster region
DashboardName   = input('CloudWatch dashboard name: ')   #-- Name of the CloudWach dashboard
NumberOfBrokers = int(input('Number of brokers: ') )  #-- Interger value - Number of brokers in the cluster to be monitored.
Topics          = input('Topics (comma seperated values): ')   #-- Comma seperated list of Topic names
print("""
Executing the script ...          
     """)


Brokers_list = list(range(1, NumberOfBrokers+1))
Topics_list = [a.strip() for a in Topics.split(',')]

BurstBalance_list                   = []
TrafficShaping_list                 = []
ConnectionCount_list                = []
CpuSystem_list                      = []
CpuUser_list                        = []
CpuIOWait_list                      = []
TotalCpuUtilization_list            = []
MemoryUsed_list                     = []
HeapMemoryAfterGC_list              = []
PartitionCount_list                 = []
UnderMinIsrPartitionCount_list      = []
UnderReplicatedPartitions_list      = []
MessagesInPerSec_list               = []
KafkaDataLogsDiskUsed_list          = []
ZooKeeperRequestLatencyMsMean_list  = []
RequestHandlerAvgIdlePercent_list   = []
RequestHandlerAvgIdlePercent1_list  = []
RequestHandlerAvgUtilization_list   = []
BytesInPerSecBroker_list            = []
BytesOutPerSecBroker_list           = []								
BytesInPerSecTopic_list             = []
BytesOutPerSecTopic_list            = []

for z in Brokers_list:
    i = str(z)
    BurstBalance_list.append   					('["AWS/Kafka", "BurstBalance", 								    "Cluster Name", "'  + ClusterName + '", "Broker ID", "' + i + '", { "region": "' + MSKRegion + '" } ] ')
    TrafficShaping_list.append 					('["AWS/Kafka", "TrafficShaping", 								"Cluster Name", "'  + ClusterName + '", "Broker ID", "' + i + '", { "region": "' + MSKRegion + '" } ] ')
    ConnectionCount_list.append					('["AWS/Kafka", "ConnectionCount", 								"Cluster Name", "'  + ClusterName + '", "Broker ID", "' + i + '", { "region": "' + MSKRegion + '" } ] ')    
    CpuSystem_list.append				        ('["AWS/Kafka", "CpuSystem", 			                        "Cluster Name", "'  + ClusterName + '", "Broker ID", "' + i + '", { "region": "' + MSKRegion + '", "id": "s' + i + '", "visible": false } ] ')
    CpuUser_list.append				            ('["AWS/Kafka", "CpuUser", 			                            "Cluster Name", "'  + ClusterName + '", "Broker ID", "' + i + '", { "region": "' + MSKRegion + '", "id": "u' + i + '", "visible": false } ] ')
    CpuIOWait_list.append				        ('["AWS/Kafka", "CpuIOWait", 			                        "Cluster Name", "'  + ClusterName + '", "Broker ID", "' + i + '", { "region": "' + MSKRegion + '", "id": "w' + i + '", "visible": false } ] ')
    TotalCpuUtilization_list.append				('[ { "expression": "s' + i +  '+u' + i +  '+w' + i + '", "label": "' + i +  ' Total CPU Utilization", "id": "e' + i +  '", "region": "' + MSKRegion + '" } ]')
    MemoryUsed_list.append						('["AWS/Kafka", "MemoryUsed", 						"Cluster Name", "'  + ClusterName + '", "Broker ID", "' + i + '", { "region": "' + MSKRegion + '" } ] ')
    HeapMemoryAfterGC_list.append				('["AWS/Kafka", "HeapMemoryAfterGC", 				"Cluster Name", "'  + ClusterName + '", "Broker ID", "' + i + '", { "region": "' + MSKRegion + '" } ] ')
    PartitionCount_list.append					('["AWS/Kafka", "PartitionCount", 					"Cluster Name", "'  + ClusterName + '", "Broker ID", "' + i + '", { "region": "' + MSKRegion + '" } ] ')
    UnderReplicatedPartitions_list.append		('["AWS/Kafka", "UnderReplicatedPartitions", 		"Cluster Name", "'  + ClusterName + '", "Broker ID", "' + i + '", { "region": "' + MSKRegion + '" } ] ')
    UnderMinIsrPartitionCount_list.append		('["AWS/Kafka", "UnderMinIsrPartitionCount", 		"Cluster Name", "'  + ClusterName + '", "Broker ID", "' + i + '", { "region": "' + MSKRegion + '" } ] ')
    MessagesInPerSec_list.append				('["AWS/Kafka", "MessagesInPerSec", 				"Cluster Name", "'  + ClusterName + '", "Broker ID", "' + i + '", { "region": "' + MSKRegion + '" } ] ')
    KafkaDataLogsDiskUsed_list.append			('["AWS/Kafka", "KafkaDataLogsDiskUsed", 			"Cluster Name", "'  + ClusterName + '", "Broker ID", "' + i + '", { "region": "' + MSKRegion + '" } ] ')
    ZooKeeperRequestLatencyMsMean_list.append	('["AWS/Kafka", "ZooKeeperRequestLatencyMsMean", 	"Cluster Name", "'  + ClusterName + '", "Broker ID", "' + i + '", { "region": "' + MSKRegion + '" } ] ')
    RequestHandlerAvgIdlePercent_list.append	('["AWS/Kafka", "RequestHandlerAvgIdlePercent",    "Cluster Name", "'  + ClusterName + '", "Broker ID", "' + i + '", { "region": "' + MSKRegion + '" } ] ')
    RequestHandlerAvgIdlePercent1_list.append	('["AWS/Kafka", "RequestHandlerAvgIdlePercent", 	"Cluster Name", "'  + ClusterName + '", "Broker ID", "' + i + '", { "region": "' + MSKRegion + '", "id": "r' + i + '", "visible": false } ] ')
    RequestHandlerAvgUtilization_list.append    ('[ { "expression": "1-r' + i +  '", "label": "' + i +  ' Request Handler Average Utilization", "id": "x' + i +  '", "region": "' + MSKRegion + '" } ]')
    BytesInPerSecBroker_list.append				('["AWS/Kafka", "BytesInPerSec", 			    "Cluster Name", "'  + ClusterName + '", "Broker ID", "' + i + '", { "region": "' + MSKRegion + '" } ] ')
    BytesOutPerSecBroker_list.append			('["AWS/Kafka", "BytesOutPerSec", 			"Cluster Name", "'  + ClusterName + '", "Broker ID", "' + i + '", { "region": "' + MSKRegion + '" } ] ')
                                                                 
    for y in Topics_list:
        BytesInPerSecTopic_list.append			('[ "AWS/Kafka", "BytesInPerSec",                                "Cluster Name", "'  + ClusterName + '", "Broker ID", "' + i + '", "Topic", "' + y + '", { "region": "' + MSKRegion + '", "label": "' + i + y + '" } ]')
        BytesOutPerSecTopic_list.append			('[ "AWS/Kafka", "BytesOutPerSec",                               "Cluster Name", "'  + ClusterName + '", "Broker ID", "' + i + '", "Topic", "' + y + '", { "region": "' + MSKRegion + '", "label": "' + i + y + '" } ]')
        
        
BurstBalance					= ', \n'.join(BurstBalance_list                 )
TrafficShaping                  = ', \n'.join(TrafficShaping_list               )
ConnectionCount                 = ', \n'.join(ConnectionCount_list              )
TotalCpuUtilization             = ', \n'.join(TotalCpuUtilization_list          ) + ',\n' + ', \n'.join(CpuSystem_list) + ',\n' + ', \n'.join(CpuUser_list) + ',\n' + ', \n'.join(CpuIOWait_list) 
MemoryUsed                      = ', \n'.join(MemoryUsed_list                   )
HeapMemoryAfterGC               = ', \n'.join(HeapMemoryAfterGC_list            )
PartitionCount                  = ', \n'.join(PartitionCount_list               )
UnderReplicatedPartitions       = ', \n'.join(UnderReplicatedPartitions_list    )
UnderMinIsrPartitionCount       = ', \n'.join(UnderMinIsrPartitionCount_list    )
MessagesInPerSec                = ', \n'.join(MessagesInPerSec_list             )
KafkaDataLogsDiskUsed           = ', \n'.join(KafkaDataLogsDiskUsed_list        )
ZooKeeperRequestLatencyMsMean   = ', \n'.join(ZooKeeperRequestLatencyMsMean_list)
RequestHandlerAvgIdlePercent    = ', \n'.join(RequestHandlerAvgIdlePercent_list )
RequestHandlerAvgUtilization    = ', \n'.join(RequestHandlerAvgUtilization_list ) + ',\n' + ', \n'.join(RequestHandlerAvgIdlePercent1_list)
BytesInPerSecBroker             = ', \n'.join(BytesInPerSecBroker_list          )
BytesOutPerSecBroker            = ', \n'.join(BytesOutPerSecBroker_list         )
BytesInPerSecTopic              = ', \n'.join(BytesInPerSecTopic_list           )
BytesOutPerSecTopic             = ', \n'.join(BytesOutPerSecTopic_list          )


#print (BurstBalance				  )
#print (TrafficShaping                )
#print (ConnectionCount               )
#print (TotalCpuUtilization           )
#print (MemoryUsed                    )
#print (HeapMemoryAfterGC             )
#print (PartitionCount                )
#print (UnderReplicatedPartitions     )
#print (UnderMinIsrPartitionCount     )
#print (MessagesInPerSec              )
#print (KafkaDataLogsDiskUsed         )
#print (ZooKeeperRequestLatencyMsMean )
#print (RequestHandlerAvgIdlePercent_list  )
#print (RequestHandlerAvgIdlePercent1_list  )
#print (RequestHandlerAvgUtilization  )
#print (BytesInPerSecBroker           )
#print (BytesOutPerSecBroker          )
#print (BytesInPerSecTopic            )
#print (BytesOutPerSecTopic           )


DashboardBody     = '''
                        {
                            "variables": [
                                {
                                    "type": "property",
                                    "property": "Cluster Name",
                                    "inputType": "input",
                                    "id": "Cluster",
                                    "label": "Cluster Name",
                                    "defaultValue": "''' + ClusterName + '''",
                                    "visible": true
                                },
                                {
                                    "type": "property",
                                    "property": "region",
                                    "inputType": "input",
                                    "id": "region",
                                    "label": "region",
                                    "defaultValue": "''' + MSKRegion + '''",
                                    "visible": true
                                }
                            ],
                            "widgets": [
                                {
                                    "height": 10,
                                    "width": 8,
                                    "y": 1,
                                    "x": 0,
                                    "type": "metric",
                                    "properties": {
                                        "metrics": [
                                            [ "AWS/Kafka", "GlobalTopicCount", "Cluster Name", "''' + ClusterName + '''", { "region": "''' + MSKRegion + '''" } ]
                                        ],
                                        "view": "timeSeries",
                                        "stacked": false,
                                        "title": "Global Topic Count",
                                        "region": "''' + MSKRegion + '''",
                                        "period": 300,
                                        "stat": "Maximum"
                                    }
                                },
                                {
                                    "height": 10,
                                    "width": 8,
                                    "y": 1,
                                    "x": 8,
                                    "type": "metric",
                                    "properties": {
                                        "metrics": [
                                            [ "AWS/Kafka", "GlobalPartitionCount", "Cluster Name", "''' + ClusterName + '''", { "region": "''' + MSKRegion + '''" } ]
                                        ],
                                        "view": "timeSeries",
                                        "stacked": false,
                                        "title": "Global Partition Count",
                                        "region": "''' + MSKRegion + '''",
                                        "period": 300,
                                        "stat": "Maximum"
                                    }
                                },
                                {
                                    "height": 10,
                                    "width": 8,
                                    "y": 1,
                                    "x": 16,
                                    "type": "metric",
                                    "properties": {
                                        "metrics": [
                                            [ "AWS/Kafka", "OfflinePartitionsCount", "Cluster Name", "''' + ClusterName + '''", { "region": "''' + MSKRegion + '''", "id": "m1" } ]
                                        ],
                                        "view": "timeSeries",
                                        "stacked": false,
                                        "title": "Offline Partitions Count",
                                        "region": "''' + MSKRegion + '''",
                                        "period": 300,
                                        "stat": "Maximum",
                                        "yAxis": {
                                            "left": {
                                                "showUnits": true
                                            }
                                        },
                                        "annotations": {
                                            "horizontal": [
                                                {
                                                    "label": "Recommended Threshold",
                                                    "value": 0,
                                                    "fill": "above"
                                                }
                                            ]
                                        },
                                        "legend": {
                                            "position": "bottom"
                                        }
                                    }
                                },
                                {
                                    "height": 10,
                                    "width": 8,
                                    "y": 11,
                                    "x": 0,
                                    "type": "metric",
                                    "properties": {
                                        "metrics": [
                                            [ "AWS/Kafka", "KafkaDataLogsDiskUsed", "Cluster Name", "''' + ClusterName + '''", { "region": "''' + MSKRegion + '''" } ]
                                        ],
                                        "view": "timeSeries",
                                        "stacked": false,
                                        "region": "''' + MSKRegion + '''",
                                        "title": "Kafka Data Logs Disk Used",
                                        "period": 300,
                                        "annotations": {
                                            "horizontal": [
                                                {
                                                    "label": "Recommended Threshold",
                                                    "value": 85,
                                                    "fill": "above"
                                                }
                                            ]
                                        },
                                        "stat": "Maximum"
                                    }
                                },
                                {
                                    "height": 10,
                                    "width": 8,
                                    "y": 11,
                                    "x": 8,
                                    "type": "metric",
                                    "properties": {
                                        "metrics": [
                                            [ "AWS/Kafka", "ActiveControllerCount", "Cluster Name", "''' + ClusterName + '''", { "region": "''' + MSKRegion + '''" } ]
                                        ],
                                        "view": "timeSeries",
                                        "stacked": false,
                                        "region": "''' + MSKRegion + '''",
                                        "stat": "Maximum",
                                        "period": 300,
                                        "title": "Active Controller Count",
                                        "annotations": {
                                            "horizontal": [
                                                {
                                                    "label": "Recommended Threshold",
                                                    "value": 1,
                                                    "fill": "above"
                                                }
                                            ]
                                        }
                                    }
                                },
                                {
                                    "height": 10,
                                    "width": 8,
                                    "y": 23,
                                    "x": 0,
                                    "type": "metric",
                                    "properties": {
                                        "metrics": [
                                            ''' + BurstBalance + '''
                                        ],
                                        "view": "timeSeries",
                                        "stacked": false,
                                        "region": "''' + MSKRegion + '''",
                                        "title": "Burst Balance",
                                        "period": 300,
                                        "stat": "Maximum"
                                    }
                                },
                                {
                                    "height": 10,
                                    "width": 8,
                                    "y": 23,
                                    "x": 8,
                                    "type": "metric",
                                    "properties": {
                                        "metrics": [
                                            ''' + TrafficShaping + '''                                           
                                        ],
                                        "view": "timeSeries",
                                        "stacked": false,
                                        "region": "''' + MSKRegion + '''",
                                        "period": 300,
                                        "stat": "Maximum"
                                    }
                                },
                                {
                                    "height": 10,
                                    "width": 8,
                                    "y": 23,
                                    "x": 16,
                                    "type": "metric",
                                    "properties": {
                                        "metrics": [
                                            ''' + ConnectionCount + '''    
                                        ],
                                        "view": "timeSeries",
                                        "stacked": false,
                                        "region": "''' + MSKRegion + '''",
                                        "title": "Connection Count",
                                        "period": 300,
                                        "stat": "Maximum"
                                    }
                                },
                                {
                                    "height": 10,
                                    "width": 8,
                                    "y": 33,
                                    "x": 0,
                                    "type": "metric",
                                    "properties": {
                                        "metrics": [
                                            ''' + TotalCpuUtilization + '''                                             
                                        ],
                                        "view": "timeSeries",
                                        "stacked": false,
                                        "region": "''' + MSKRegion + '''",
                                        "period": 300,
                                        "stat": "Maximum",
                                        "title": "Total CPU Utilization (CpuIoWait + CpuSystem + CpuUser)",
                                        "annotations": {
                                            "horizontal": [
                                                {
                                                    "label": "Recommended Threshold",
                                                    "value": 60,
                                                    "fill": "above"
                                                }
                                            ]
                                        },
                                        "yAxis": {
                                            "left": {
                                                "label": "Percent",
                                                "showUnits": false
                                            },
                                            "right": {
                                                "showUnits": true
                                            }
                                        },
                                        "legend": {
                                            "position": "bottom"
                                        }
                                    }
                                },
                                {
                                    "height": 10,
                                    "width": 8,
                                    "y": 33,
                                    "x": 8,
                                    "type": "metric",
                                    "properties": {
                                        "metrics": [
                                            ''' + MemoryUsed + '''                                            
                                        ],
                                        "view": "timeSeries",
                                        "stacked": false,
                                        "region": "''' + MSKRegion + '''",
                                        "period": 300,
                                        "stat": "Maximum",
                                        "title": "Memory Used"
                                    }
                                },
                                {
                                    "height": 11,
                                    "width": 8,
                                    "y": 53,
                                    "x": 16,
                                    "type": "metric",
                                    "properties": {
                                        "metrics": [
                                            ''' + MessagesInPerSec + '''  
                                        ],
                                        "view": "timeSeries",
                                        "stacked": false,
                                        "region": "''' + MSKRegion + '''",
                                        "period": 300,
                                        "stat": "Maximum",
                                        "title": "Messages In Per Sec"
                                    }
                                },
                                {
                                    "height": 10,
                                    "width": 8,
                                    "y": 43,
                                    "x": 0,
                                    "type": "metric",
                                    "properties": {
                                        "metrics": [
                                            ''' + PartitionCount + '''  
                                        ],
                                        "view": "timeSeries",
                                        "stacked": false,
                                        "region": "''' + MSKRegion + '''",
                                        "period": 300,
                                        "stat": "Maximum",
                                        "title": "Partition Count"
                                    }
                                },
                                {
                                    "height": 10,
                                    "width": 8,
                                    "y": 43,
                                    "x": 8,
                                    "type": "metric",
                                    "properties": {
                                        "metrics": [
                                            ''' + UnderReplicatedPartitions + '''  
                                        ],
                                        "view": "timeSeries",
                                        "stacked": false,
                                        "region": "''' + MSKRegion + '''",
                                        "period": 300,
                                        "stat": "Maximum",
                                        "title": "Under Replicated Partitions"
                                    }
                                },
                                {
                                    "height": 10,
                                    "width": 8,
                                    "y": 43,
                                    "x": 16,
                                    "type": "metric",
                                    "properties": {
                                        "metrics": [
                                            ''' + UnderMinIsrPartitionCount + '''  
                                        ],
                                        "view": "timeSeries",
                                        "stacked": false,
                                        "region": "''' + MSKRegion + '''",
                                        "period": 300,
                                        "stat": "Maximum",
                                        "title": "Under Minimum Isr Partitions",
                                        "annotations": {
                                            "horizontal": [
                                                {
                                                    "label": "Recommended Threshold",
                                                    "value": 0,
                                                    "fill": "above"
                                                }
                                            ]
                                        }
                                    }
                                },
                                {
                                    "height": 11,
                                    "width": 8,
                                    "y": 53,
                                    "x": 0,
                                    "type": "metric",
                                    "properties": {
                                        "metrics": [
                                            ''' + KafkaDataLogsDiskUsed + '''  
                                        ],
                                        "view": "timeSeries",
                                        "stacked": false,
                                        "region": "''' + MSKRegion + '''",
                                        "period": 300,
                                        "stat": "Maximum",
                                        "annotations": {
                                            "horizontal": [
                                                {
                                                    "label": "Recommended Threshold",
                                                    "value": 85,
                                                    "fill": "above"
                                                }
                                            ]
                                        }
                                    }
                                },
                                {
                                    "height": 10,
                                    "width": 8,
                                    "y": 33,
                                    "x": 16,
                                    "type": "metric",
                                    "properties": {
                                        "metrics": [
                                            ''' + HeapMemoryAfterGC + '''  
                                        ],
                                        "view": "timeSeries",
                                        "stacked": false,
                                        "region": "''' + MSKRegion + '''",
                                        "title": "Heap Memory After GC",
                                        "period": 300,
                                        "stat": "Maximum",
                                        "annotations": {
                                            "horizontal": [
                                                {
                                                    "label": "Recommended Threshold",
                                                    "value": 60,
                                                    "fill": "above"
                                                }
                                            ]
                                        }
                                    }
                                },
                                {
                                    "height": 1,
                                    "width": 24,
                                    "y": 0,
                                    "x": 0,
                                    "type": "text",
                                    "properties": {
                                        "markdown": "# Cluster Level Metrics\\n",
                                        "background": "transparent"
                                    }
                                },
                                {
                                    "height": 2,
                                    "width": 24,
                                    "y": 21,
                                    "x": 0,
                                    "type": "text",
                                    "properties": {
                                        "markdown": "# Cluster, Broker Level Metrics\\n(Edit the panels to add/remove any additional brokers to monitor)",
                                        "background": "transparent"
                                    }
                                },
                                {
                                    "height": 11,
                                    "width": 8,
                                    "y": 53,
                                    "x": 8,
                                    "type": "metric",
                                    "properties": {
                                        "metrics": [
                                            ''' + ZooKeeperRequestLatencyMsMean + '''  
                                        ],
                                        "view": "timeSeries",
                                        "stacked": false,
                                        "region": "''' + MSKRegion + '''",
                                        "title": "ZooKeeper Request Latency Ms Mean",
                                        "period": 300,
                                        "stat": "p99"
                                    }
                                },
                                {
                                    "height": 2,
                                    "width": 24,
                                    "y": 85,
                                    "x": 0,
                                    "type": "text",
                                    "properties": {
                                        "markdown": "# Cluster, Broker, Topic Level Metrics\\n(Edit the panels to add/remove any additional topics to monitor)",
                                        "background": "transparent"
                                    }
                                },
                                {
                                    "height": 11,
                                    "width": 12,
                                    "y": 87,
                                    "x": 0,
                                    "type": "metric",
                                    "properties": {
                                        "metrics": [
                                            ''' + BytesInPerSecTopic + '''  
                                        ],
                                        "view": "timeSeries",
                                        "stacked": false,
                                        "region": "''' + MSKRegion + '''",
                                        "period": 300,
                                        "stat": "Maximum",
                                        "title": "Bytes In Per Sec",
                                        "yAxis": {
                                            "left": {
                                                "label": "Bytes/Second",
                                                "showUnits": false
                                            }
                                        }
                                    }
                                },
                                {
                                    "height": 11,
                                    "width": 12,
                                    "y": 87,
                                    "x": 12,
                                    "type": "metric",
                                    "properties": {
                                        "metrics": [
                                            ''' + BytesOutPerSecTopic + '''                          					
                                        ],
                                        "view": "timeSeries",
                                        "stacked": false,
                                        "region": "''' + MSKRegion + '''",
                                        "period": 300,
                                        "stat": "Maximum",
                                        "title": "Bytes Out Per Sec",
                                        "yAxis": {
                                            "left": {
                                                "showUnits": false,
                                                "label": "Bytes/Second"
                                            }
                                        }
                                    }
                                },
                                {
                                    "height": 11,
                                    "width": 12,
                                    "y": 74,
                                    "x": 0,
                                    "type": "metric",
                                    "properties": {
                                        "metrics": [
                                            ''' + BytesInPerSecBroker + '''  
                                        ],
                                        "view": "timeSeries",
                                        "stacked": false,
                                        "region": "''' + MSKRegion + '''",
                                        "period": 300,
                                        "stat": "Maximum",
                                        "title": "Bytes In Per Sec"
                                    }
                                },
                                {
                                    "height": 11,
                                    "width": 12,
                                    "y": 74,
                                    "x": 12,
                                    "type": "metric",
                                    "properties": {
                                        "metrics": [
                                            ''' + BytesOutPerSecBroker + '''  
                                        ],
                                        "view": "timeSeries",
                                        "stacked": false,
                                        "region": "''' + MSKRegion + '''",
                                        "period": 300,
                                        "stat": "Maximum",
                                        "title": "Bytes Out Per Sec"
                                    }
                                },
                                {
                                    "height": 10,
                                    "width": 12,
                                    "y": 64,
                                    "x": 0,
                                    "type": "metric",
                                    "properties": {
                                        "metrics": [
                                            ''' + RequestHandlerAvgIdlePercent + '''  
                                        ],
                                        "view": "timeSeries",
                                        "stacked": false,
                                        "region": "''' + MSKRegion + '''",
                                        "title": "Request Handler Avg Idle Percent",
                                        "period": 300,
                                        "stat": "Maximum"
                                    }
                                },
                                {
                                    "height": 10,
                                    "width": 12,
                                    "y": 64,
                                    "x": 12,
                                    "type": "metric",
                                    "properties": {
                                        "metrics": [
                                            ''' + RequestHandlerAvgUtilization + '''                                             
                                        ],
                                        "view": "timeSeries",
                                        "stacked": false,
                                        "region": "''' + MSKRegion + '''",
                                        "period": 300,
                                        "stat": "Maximum",
                                        "title": "Request Handler Average Utilization (1-RequestHandlerAvgIdlePercent)",
                                        "annotations": {
                                            "horizontal": [
                                                {
                                                    "label": "Recommended Threshold",
                                                    "value": 0.6,
                                                    "fill": "above"
                                                }
                                            ]
                                        },
                                        "yAxis": {
                                            "left": {
                                                "label": "Percent",
                                                "showUnits": false
                                            },
                                            "right": {
                                                "showUnits": true
                                            }
                                        },
                                        "legend": {
                                            "position": "bottom"
                                        }
                                    }
                                }
                            ]
                        }
                    '''


#print(DashboardBody)

with open("monitoring-dashboard-amazon-msk_source.yaml", 'r') as file:
    try:
        loaded = yaml.safe_load(file)
    except yaml.YAMLError as exc:
        print(exc)

# Modify the fields from the di
Topics_list_str = ','.join(Topics_list)
Topics_ls_str = Topics_list_str.split(' ')

loaded['Parameters']['ClusterName']['AllowedValues']    =  ClusterName.split()
loaded['Parameters']['MSKRegion']['AllowedValues']      =  MSKRegion.split()
loaded['Parameters']['NumberOfBrokers']['AllowedValues']        =  str(NumberOfBrokers).split()
loaded['Parameters']['Topics']['AllowedValues']         =  Topics_ls_str
loaded['Parameters']['DashboardName']['AllowedValues']        =  DashboardName.split()

loaded['Parameters']['ClusterName']['Default']    =  ClusterName
loaded['Parameters']['MSKRegion']['Default']      =  MSKRegion
loaded['Parameters']['NumberOfBrokers']['Default']        =  NumberOfBrokers
loaded['Parameters']['Topics']['Default']         =  Topics_list_str
loaded['Parameters']['DashboardName']['Default']  =  DashboardName

loaded['Resources']['CloudwatchDashboard']['Properties']['DashboardName']        =  DashboardName
loaded['Resources']['CloudwatchDashboard']['Properties']['DashboardBody']        =  DashboardBody

loaded['Outputs']['CloudwatchDashboard']['Value']        =  'https://' + MSKRegion+ '.console.aws.amazon.com/cloudwatch/home#dashboards:name=' + DashboardName

timestr = time.strftime("%Y%m%d_%H%M%S")
cwd_path = os.path.abspath(os.getcwd())

# Save it again
with open("monitoring-dashboard-amazon-msk_modified_" + timestr + ".yaml", 'w') as stream:
    try:
        yaml.dump(loaded, stream, default_flow_style=False)
        print('Output file path: ' ,cwd_path)
        print('Output file name:' + 'monitoring-dashboard-amazon-msk_modified_' + timestr + '.yaml')
    except yaml.YAMLError as exc:
        print(exc)
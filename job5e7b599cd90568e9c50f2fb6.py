import traceback
import sys
from operations import TopOperation
from operations import JoinOperation
from operations import AggregationOperation
from operations import FormulaOperation
from operations import FilterOperation
from connectors import DBFSConnector
from connectors import CosmosDBConnector
from datatransformations import TranformationsMainFlow
from automl import tpot_execution
from core import PipelineNotification
import json

try: 
	PipelineNotification.PipelineNotification().started_notification('5e7b599dd90568e9c50f2fb7','5e39734e0204cd465d4d2e10','http://40.83.140.93:3200/pipeline/notify')
	newmltestcommitapp_DBFS = DBFSConnector.DBFSConnector.fetch([], {}, "5e7b599dd90568e9c50f2fb7", spark, "{'url': '', 'file_type': 'Delimeted', 'dbfs_token': '', 'dbfs_domain': '', 'delimiter': ',', 'is_header': 'Use Header Line'}")

	PipelineNotification.PipelineNotification().completed_notification('5e7b599dd90568e9c50f2fb7','5e39734e0204cd465d4d2e10','http://40.83.140.93:3200/pipeline/notify')
except Exception as ex: 
	PipelineNotification.PipelineNotification().failed_notification(ex,'5e7b599dd90568e9c50f2fb7','5e39734e0204cd465d4d2e10','http://40.83.140.93:3200/pipeline/notify','http://40.83.140.93:3200/logs/getProductLogs')
	sys.exit(1)
try: 
	PipelineNotification.PipelineNotification().started_notification('5e7b599dd90568e9c50f2fb8','5e39734e0204cd465d4d2e10','http://40.83.140.93:3200/pipeline/notify')
	newmltestcommitapp_AutoFE = TranformationsMainFlow.TramformationMain.run(["5e7b599dd90568e9c50f2fb7"],{"5e7b599dd90568e9c50f2fb7": newmltestcommitapp_DBFS}, "5e7b599dd90568e9c50f2fb8", spark,json.dumps( {"FE": []}))

	PipelineNotification.PipelineNotification().completed_notification('5e7b599dd90568e9c50f2fb8','5e39734e0204cd465d4d2e10','http://40.83.140.93:3200/pipeline/notify')
except Exception as ex: 
	PipelineNotification.PipelineNotification().failed_notification(ex,'5e7b599dd90568e9c50f2fb8','5e39734e0204cd465d4d2e10','http://40.83.140.93:3200/pipeline/notify','http://40.83.140.93:3200/logs/getProductLogs')
	sys.exit(1)
try: 
	PipelineNotification.PipelineNotification().started_notification('5e7b599dd90568e9c50f2fb9','5e39734e0204cd465d4d2e10','http://40.83.140.93:3200/pipeline/notify')
	newmltestcommitapp_AutoML = tpot_execution.Tpot_execution.run(["5e7b599dd90568e9c50f2fb8"],{"5e7b599dd90568e9c50f2fb8": newmltestcommitapp_AutoFE}, "5e7b599dd90568e9c50f2fb9", spark,json.dumps( {"model_type": "classification", "label": "", "features": [], "percentage": "10", "executionTime": "5", "ProjectName": "zeshan_test", "PipelineName": "newmltestcommitapp", "pipelineId": "5e7b599cd90568e9c50f2fb6", "userid": "5e39734e0204cd465d4d2e10", "runid": "", "url_ResultView": "http://40.83.140.93:3200", "experiment_id": "551308251382540"}))

	PipelineNotification.PipelineNotification().completed_notification('5e7b599dd90568e9c50f2fb9','5e39734e0204cd465d4d2e10','http://40.83.140.93:3200/pipeline/notify')
except Exception as ex: 
	PipelineNotification.PipelineNotification().failed_notification(ex,'5e7b599dd90568e9c50f2fb9','5e39734e0204cd465d4d2e10','http://40.83.140.93:3200/pipeline/notify','http://40.83.140.93:3200/logs/getProductLogs')
	sys.exit(1)


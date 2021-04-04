import os
from grnhse import Harvest
from greenhouse_jobs import greenhouse_job
from greenhouse_applications import greenhouse_application
from prometheus_client import Gauge, CollectorRegistry, push_to_gateway

## API KEY - Green House 
API_KEY = os.environ.get("HARVEST_API_KEY",'Your-API-Key')

class HarvestClient:
    def __init__(self):
        self.registry = CollectorRegistry()
        self.gauge = Gauge('metric', 'Green house job object', ["type"], registry = self.registry)    
        self.hvst = Harvest(API_KEY)

    def getGreenHouseJobObject(self, department_id_list):
        g_hvst_job_obj = greenhouse_job(self.hvst)
        g_hvst_job_obj.job_processing(department_id_list)
        job_obj=vars(g_hvst_job_obj)
        
        ## Total Open Jobs Engineering
        openJobsEng = job_obj.get('total_opened_jobs_eng')
        self.gauge.labels("openJobsEng").set(openJobsEng)

        ## Total Closed Jobs Engineering
        closeJobsEng = job_obj.get('total_closed_jobs_eng')
        self.gauge.labels("closeJobsEng").set(closeJobsEng)

        ## Total Jobs Openings
        totalJobsOpening = job_obj.get('total_job_openings')
        self.gauge.labels("totalJobsOpening").set(totalJobsOpening) 

        ## No. of Open Job
        openJobs = job_obj.get('number_of_opened_job_openings')
        self.gauge.labels("openJobs").set(openJobs) 

        ## No. of Closed Job
        closeJobs = job_obj.get('number_of_closed_job_openings')
        self.gauge.labels("closeJobs").set(closeJobs)

        ##Push to Prometheus Gateway
        push_to_gateway('localhost:9091', job='push_metrics', registry = self.registry)


if __name__=="__main__":
    department_id_list = [4035937002,4035954002,4035955002,4035956002,4035957002,4035966002,4036782002,4049081002]

    harvestClient = HarvestClient()

    ## Green House Job Object
    harvestClient.getGreenHouseJobObject(department_id_list)

    #print(vars(g_hvst_job_obj))
    # g_hvst_app_obj = greenhouse_application(hvst)
    # g_hvst_app_obj.initialise_application_processing(g_hvst_job_obj.Ids_of_jobs_eng)
    # print(vars(g_hvst_app_obj))

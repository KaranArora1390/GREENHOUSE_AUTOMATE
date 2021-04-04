import os
from grnhse import Harvest
from greenhouse_jobs import greenhouse_job
from greenhouse_applications import greenhouse_application

API_KEY = os.environ.get("HARVEST_API_KEY")

hvst = Harvest(API_KEY)

if __name__=="__main__":
    department_id_list = [4035937002,4035954002,4035955002,4035956002,4035957002,4035966002,4036782002,4049081002]
    g_hvst_job_obj = greenhouse_job(hvst)
    g_hvst_job_obj.job_processing(department_id_list)
    print(vars(g_hvst_job_obj))
    g_hvst_app_obj = greenhouse_application(hvst)
    g_hvst_app_obj.initialise_application_processing(g_hvst_job_obj.Ids_of_jobs_eng)
    print(vars(g_hvst_app_obj))

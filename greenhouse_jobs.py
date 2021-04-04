

class greenhouse_job:

    def __init__(self,hvst):
        self.jobs = hvst.jobs
        self.Ids_of_jobs_eng = []
        self.total_opened_jobs_eng = 0
        self.total_closed_jobs_eng = 0
        self.total_job_openings = 0
        self.number_of_opened_job_openings = 0
        self.number_of_closed_job_openings = 0

    def job_processing(self,dept_id_list):
        
        all_jobs = [job for page in self.jobs for job in page]
        
        for job in all_jobs:
            for job_department in job['departments']:
                if job_department['id'] in dept_id_list:
                    
                    if (job['status'] == 'open'):
                        self.total_opened_jobs_eng+=1
                        self.Ids_of_jobs_eng.append(job['id'])
                        for position in  job['openings']:
                            if position['status']=='open':
                                self.number_of_opened_job_openings+=1
                            if position['status']=='closed':
                                self.number_of_closed_job_openings+=1
                        
                    elif(job['status'] == 'closed'):
                        self.total_closed_jobs_eng+=1
                        self.Ids_of_jobs_eng.append(job['id'])
                        for position in  job['openings']:
                            if position['status']=='open':
                                self.number_of_opened_job_openings+=1
                            if position['status']=='closed':
                                self.number_of_closed_job_openings+=1

        self.total_job_openings = self.number_of_opened_job_openings +  self.number_of_closed_job_openings       
        
        # print(Ids_of_jobs_eng)
        # return (total_jobs_eng,total_opened_jobs_eng,len(number_of_job_openings_ids))

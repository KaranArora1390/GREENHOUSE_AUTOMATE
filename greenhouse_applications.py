

class greenhouse_application:

    def __init__(self,hvst):
        self.current_stage_list = ['Application Review','Hiring Manager Review','Recruiter Evaluation',
                                    'Phone Interview','Case Study & Task','Face to Face',
                                    'Executive Interview','HR Discussion','offer','hired']
        self.total_apps_current_stages_dict = {'Application Review':0,
                        'Hiring Manager Review':0,
                        'Recruiter Evaluation':0,
                        'Phone Interview':0,
                        'Case Study & Task':0,
                        'Face to Face':0,
                        'Executive Interview':0,
                        'HR Discussion':0,
                        'Offer':0,
                        'Hired':0,
                        }
        self.current_stages_rejected_dict = {'Application Review':0,
                        'Hiring Manager Review':0,
                        'Recruiter Evaluation':0,
                        'Phone Interview':0,
                        'Case Study & Task':0,
                        'Face to Face':0,
                        'Executive Interview':0,
                        'HR Discussion':0,
                        'Offer':0,
                        'Hired':0,
                        }
        self.current_stages_hired_dict = {'Application Review':0,
                        'Hiring Manager Review':0,
                        'Recruiter Evaluation':0,
                        'Phone Interview':0,
                        'Case Study & Task':0,
                        'Face to Face':0,
                        'Executive Interview':0,
                        'HR Discussion':0,
                        'Offer':0,
                        'Hired':0,
                        }
        self.current_stages_active_dict = {'Application Review':0,
                        'Hiring Manager Review':0,
                        'Case Study & Task':0,
                        'Recruiter Evaluation':0,
                        'Phone Interview':0,
                        'Face to Face':0,
                        'Executive Interview':0,
                        'HR Discussion':0,
                        'Offer':0,
                        'Hired':0,
                        }
        self.applications = hvst.applications
        self.total_apps_eng = 0
        self.total_app_rejected=0
        self.total_app_active=0
        self.total_app_hired=0
    
    def initialise_application_processing(self,eng_job_id_list):

        apps = self.applications.get(per_page=500)
        self.application_processing(apps,eng_job_id_list)                      
        while self.applications.records_remaining:
            self.application_processing(self.applications.get_next(),eng_job_id_list) 


    def application_processing(self,apps,eng_job_id_list):
        
        if apps:
            for app in apps:
                if len(app['jobs'])>0:
                    if app['jobs'][0]['id'] in eng_job_id_list:
                        self.total_apps_eng+=1
                        if app['current_stage']:
                            if app['current_stage']['name'] in self.current_stage_list:
                                self.total_apps_current_stages_dict[app['current_stage']['name']]+=1
                        if app['status']=='rejected':
                            self.total_app_rejected+=1
                            if app['current_stage']:
                                if app['current_stage']['name'] in self.current_stage_list:
                                    self.current_stages_rejected_dict[app['current_stage']['name']]+=1
                        elif app['status']=='active':
                            self.total_app_active+=1        
                            if app['current_stage']:
                                if app['current_stage']['name'] in self.current_stage_list:      
                                    self.current_stages_active_dict[app['current_stage']['name']]+=1
                        elif app['status'] == 'hired':
                            self.total_app_hired+=1
                            if app['current_stage']:
                                if app['current_stage']['name'] in self.current_stage_list:        
                                    self.current_stages_hired_dict[app['current_stage']['name']]+=1

                          
        

# print(total_apps_eng)
# print(total_apps_current_stages_dict)
# print(total_app_rejected)
# print(current_stages_rejected_dict)
# print(total_app_active)
# print(current_stages_active_dict)
# print(total_app_hired)
# print(current_stages_hired_dict)

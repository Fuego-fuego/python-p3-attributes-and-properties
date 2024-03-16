#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__ (self, name ="Jon Doe" , job ="Admin"):
        self.name = name
        self.job = job
    

    @property
    def name(self):        
        return self._name
    
    @name.setter
    def name(self,name): 
        if(type(name) is str and ( 0 < len(name) < 26 ) ):
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")
    @property
    def job(self):
        return self._job
    
    @job.setter
    def job(self,job_title):
        if( job_title in APPROVED_JOBS  ):
            self._job= job_title
        else:
            print("Job must be in list of approved jobs.")




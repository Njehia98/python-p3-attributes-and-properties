#!/usr/bin/env python3#!/usr/bin/env python3

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
   def __init__(self, name="Unknown", job="Unknown"):
        self.name = name
        self.job = job

   def name(self):
        return self._name

   def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 25):
            print("Name must be a string between 1 and 25 characters.")
        else:
            self._name = value.title()

   def job(self):
        return self._job

   def job(self, value):
        if value not in self.approved_jobs:
            print("Job must be in list of approved jobs.")
        else:
            self._job = value
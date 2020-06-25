import csv

def stack_save(jobs):
    file = open(f'stackoverflow.csv', mode='w')
    writer = csv.writer(file)
    writer.writerow(['title','company','link'])
    for job in jobs:
        writer.writerow(list(job.values()))
    return

def wework_save(jobs):
    file = open(f'weworkremotely.csv', mode='w')
    writer = csv.writer(file)
    writer.writerow(['title','company','link'])
    for job in jobs:
        writer.writerow(list(job.values()))
    return

def remote_save(jobs):
    file = open(f'remoteok.csv', mode='w')
    writer = csv.writer(file)
    writer.writerow(['title','company','link'])
    for job in jobs:
        writer.writerow(list(job.values()))
    return
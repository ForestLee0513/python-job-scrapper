from flask import Flask, render_template, request,redirect,send_file
import os
from scrapper import get_stack,get_wework,get_remoteok
from export import stack_save, wework_save, remote_save
from rank import get_rank
os.system('clear')
app = Flask("Job Scrapper")

db_stack = {}
db_wework = {}
db_remoteok = {}
db_rank = {}

@app.route('/')
def home():
    fromRank = db_rank.get('curr')
    if fromRank:
        rank = fromRank
    else:
        rank = get_rank()
        db_rank['curr']=rank
    return render_template('home.html', rank=rank)

@app.route('/404')
def notFound():
    return render_template('404.html')

@app.errorhandler(404)
def resource_not_found(e):
    return redirect('/404')


@app.route('/search')
def result(): 
    args = request.args.get('job')
    if args:
        args = args.lower()
        from_stack = db_stack.get(args)
        from_wework = db_wework.get(args)
        from_remoteok = db_remoteok.get(args)
        if from_stack:
            stack = from_stack
        else:
            stack=get_stack(args)
            db_stack[args]=stack

        if from_wework:
            wework = from_wework
        else:
            wework=get_wework(args)
            db_wework[args]=wework

        if from_remoteok:
            remoteok = from_remoteok
        else:
            remoteok=get_remoteok(args)
            db_remoteok[args]=remoteok
        result_length = len(stack) + len(wework) + len(remoteok)
    else:
        return redirect('/')

    return render_template('search.html',args=args,stack=stack,wework=wework,remoteok=remoteok, result_length = result_length)

@app.route('/export/stackoverflow')
def stack():
    try:
        args = request.args.get('job')
        if not args:
            raise Exception()
        args = args.lower()
        jobs = db_stack.get(args)
        if not jobs:
            raise Exception()
        stack_save(jobs)
        return send_file('stackoverflow.csv')
    except:
        return redirect('/')
@app.route('/export/weworkremotely')
def wework():
    try:
        args = request.args.get('job')
        if not args:
            raise Exception()
        args = args.lower()
        jobs = db_wework.get(args)
        if not jobs:
            raise Exception()
        wework_save(jobs)
        return send_file('weworkremotely.csv')
    except:
        return redirect('/')

@app.route('/export/remoteok')
def remoteok():
    try:
        args = request.args.get('job')
        if not args:
            raise Exception()
        args = args.lower()
        jobs = db_remoteok.get(args)
        if not jobs:
            raise Exception()
        remote_save(jobs)
        return send_file('remoteok.csv')
    except:
        return redirect('/')

app.run(host='0.0.0.0')
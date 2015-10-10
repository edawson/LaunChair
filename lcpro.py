import multiprocessing
import sys
import argparse

## TODO pipelines and tasks should interchangeable
## in missions.

## A mission is a dataset and a
## collection of Tasks (or a pipeline)
## to run on that data. It's a "Job" in
## cluster-manager speak.
class Mission:
    def __init__(self, total_cores=None):
        self.system_cores = total_cores if total_cores is not None else mp.cpu_count()
        self.data_file = None
        self.Pipelines = {}
        self.tasks = {}
        self.name = None

    def parse_data_file(data_file):
        data_list = []
        with open(data_file, "r") as fi:
            for line in fi:
                if len(line.split("\t")) == 1:
                    data_list.append(line.strip())
                else:
                    data_list.append([x for x in line.strip().split("\t")])
        return data_list

    ## Iterates over tasks / pipelines, respecting the ordering requirements of each.
    ## Iterates over DATA, applying command-line substitution for
    ## input variables. Passes outputs to next Task if needed.
    ## Kicks off logging and restart marking as well.
    def run(self):
        return

## A pipeline is a collection of Tasks
## linked together by intermediate inputs/outputs
class Pipeline:
    def __init__(self, n):
        self.tasks = {}
        self.name = n
        self.do_line = None
        self.log = True

    def add_task(self, task):
        self.tasks[task.name] = task

    def run():
        return

    def __repr__(self):
        return "Pipeline: " + self.name + "\n"

## A task is a single command (and its parameters)
## performed on a single data object.
class Task:
    def __init__(self, n):
        self.name = n
        self.cmd = None
        self.params = None
        self.inputs = None
        self.outputs = None

    def get_outputs(self):
        return outputs
    def set_name(self, n):
        self.name = n

    def set_cmd(self, c):
        self.cmd = c

    def set_params(self, p):
        self.params = p

    def set_inputs(self, i):
        self.inputs = i

    def set_outputs(self, o):
        self.outputs = o

    def get_name(self):
        return self.name

    def __repr__(self):
        return "Task: " + self.name + "\n" \
        + "\tCommand: " + self.cmd  + "\n" \
        + "\tParams: " + self.params
        #"Params: " + self.params


## A Work object is a task paired with its data.
## It is essentially a single shell command which could be run from
## the command line.
class Work:
    def __init__(self, task, data):
        return

    def do(self):
        try:
            subprocess.call("task")
        except:
            pass

## The master class to handle all of the LCPro functions
class LCPro:
    def __init__(self):
        self.missions = {}
        return
    def run(self):
        return
    def restart(self):
        return
    def log(self):
        return


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--lcfile", dest="lcfile", required=True)
    parser.add_argument("-i", "--datafile", dest="datafile", required=True)
    parser.add_argument("-c", "--systemcores", dest="cores", required=False)
    parser.add_argument("-d", "--debug", dest="debug", required=False, default=False)
    #parser.add_argument("run", dest="runner", required=False)
    return parser.parse_args()

def parse_restart_file(restart_file):
    return

## Build Tasks, Pipelines, and Missions
## These may be contained in separate files if you desire.
def parse_lc_file(lc_file, debug=False):
    d = {}
    d["tasks"] = {}
    d["pipelines"] = {}
    d["missions"] = {}

    with open(lc_file, "r") as fi:
        
        #for line in fi:
        while True:
            x = fi.readline()
            if x.startswith("task"):
                ## create a new named task
                t = Task(str((x.split(":")[1]).strip()))
                x = fi.readline()
                while not x.startswith("\n"):
                    if x.strip().startswith("cmd"):
                        t.set_cmd( x.split(":")[1].strip() )
                    elif x.strip().startswith("params"):
                        t.set_params( x.split(":")[1].strip() )
                    elif x.strip().startswith("inputs"):
                        t.inputs = x.split(":")[1].strip()
                    elif x.strip().startswith("outputs"):
                        t.outputs = x.split(":")[1].strip()
                    x = fi.readline()
                d["tasks"][t.name] = t
                if debug:
                    print t
            elif x.startswith("pipeline"):
                p = Pipeline(str((x.split(":")[1]).strip()))
                x = fi.readline()
                while not x.startswith("\n"):
                    if x.strip().startswith("do"):
                        p.do_line = (x.strip().split(":")[1]).strip()
                    elif x.strip().startswith("log"):
                        do_log = (x.strip().split(":")[1]).lower()
                        p.log = True if "true" in do_log else False
                    x = fi.readline()
                d["pipelines"][p.name] = p
                if debug:
                    print p
            elif x.startswith("mission"):
                continue
            elif x.strip().startswith("end"):
                break
            elif x.strip().startswith("#"):
                continue
            else:
                if debug:
                    print "Warning: invalid input."
                continue
                #raise Exception("Invalid input in lcfile. Please see the specs.")
    return




if __name__ == "__main__":
    args = parse_args()
    parse_lc_file(args.lcfile, args.debug)

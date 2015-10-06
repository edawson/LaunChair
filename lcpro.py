import multiprocessing
import sys
import argparse

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

## A pipeline is a collection of Tasks
## linked together by intermediate inputs/outputs
class Pipeline:
    def __init__(self):
        self.tasks = []

    def add_task(task):
        return
    def run():
        return

## A task is a single command (and its parameters)
## performed on a single data object.
class Task:
    def __init__(self, n):
        self.name = n
        self.cmd = None
        self.params = None
        self.inputs = None
        self.outputs = None

    def get_outputs():
        return
    def set_name(self, n):
        self.name = n
    def set_cmd(self, c):
        self.cmd = c
    def set_params(self, p):
        self.params = p
    def set_inputs(self, i):
        return
    def set_outputs(self, o):
        return
    def get_name(self):
        return self.name
    def __repr__(self):
        return "Name: " + self.name + "\n" 
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
        x = fi.readline()
        #for line in fi:
        #while x:
        if x.startswith("task"):
            ## create a new named task
            t = Task(str((x.split(":")[1]).strip()))
            #x = fi.readline()
            while not x.startswith("\n"):
                if x.startswith("cmd"):
                    t.set_cmd( x.split(":")[1].strip() )
                elif x.startswith("params"):
                    t.set_params( x.split(":")[1].strip() )
                elif x.startswith("inputs"):
                    t.inputs = x.split(":")[1].strip()
                elif x.startswith("outputs"):
                    t.outputs = x.split(":")[1].strip()
                x = fi.readline()
            d["tasks"][t.name] = t
            if debug:
                print t.cmd
        elif x.startswith("pipeline"):
            pass
        elif x.startswith("mission"):
            pass
        #x = fi.readline()
    return

def parse_data_file(data_file):
    data_list = []
    with open(data_file, "r") as fi:
        for line in fi:
            if len(line.split("\t")) == 1:
                data_list.append(line.strip())
            else:
                data_list.append([x for x in line.strip().split("\t")])
    return data_list


if __name__ == "__main__":
    args = parse_args()
    parse_lc_file(args.lcfile, args.debug)

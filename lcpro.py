import multiprocessing
import sys

## A mission is a dataset and a
## collection of Tasks (or a pipeline)
## to run on that data. It's a "Job" in
## cluster-manager speak.
class Mission():
    return

## A pipeline is a collection of Tasks
## linked together by intermediate inputs/outputs
class Pipeline():
    def add_task(task):
        return
    def run():
        return
    return

## A 
class Data():
    return

## A task is a single command (and its parameters)
## performed on a single data object.
class Task(name, command, params, inputs, outputs):
    def get_outputs():
        return

    def set_inputs():
        return
    return

## A worker is an executor of a Task or Pipeline,
## which is performed on Data.
class Worker():
    return

## The master class to handle all of the LCPro functions
class LCPro():
    def __init__(self):
        return
    def run(self):
        return
    def restart(self):
        return
    def log(self):
        return
    return


def parse_restart_file(restart_file):
    return

## Build Tasks, Pipelines, and Missions
## These may be contained in separate files if you desire.
def parse_lc_file(lc_file):
    d = {}
    with open(lc_file, "r") as fi:
        for line in fi:
            
    return

def parse_data_file(data_file):
    return


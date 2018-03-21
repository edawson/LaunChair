__author__ = 'Eric T Dawson'
import subprocess
import multiprocessing as mp
import os
import math


def func(task):
    # subprocess.Popen(task, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
    try:
        subprocess.call(task, shell=True)
    except (KeyboardInterrupt, Exception):
        raise KeyboardInterrupt
    return

class LaunChair:
    def __init__(self):
        self.jobfile = None
        self.work = None
        self.n_cpus = 0
        return

    def set_file(self, jobfile):
        self.jobfile = jobfile
        self.set_work()

    def set_work(self):
        work = []
        with open(self.jobfile, "r") as fi:
            for line in fi:
                work.append(line)
        self.work = work

    def set_n_cpus(self, n):
        if n == 0:
            self.n_cpus = mp.cpu_count()
        else:
            self.n_cpus = int(n)

    def run(self, cores_per_task):
        if cores_per_task > self.n_cpus:
            raise ValueError("The number of cores per task must be less than the number of CPUs.")
        size = math.floor(self.n_cpus / cores_per_task)

        p = mp.Pool(size)
        try:
            ret = p.map_async(func, self.work).get(100000)
        except (KeyboardInterrupt):
            p.terminate()
            exit(1)

        return

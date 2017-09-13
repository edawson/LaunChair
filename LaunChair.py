__author__ = 'Eric T Dawson'
import subprocess
import multiprocessing as mp
import os


def func(task):
    # subprocess.Popen(task, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
    try:
        subprocess.call(task, shell=True)
    except KeyboardInterrupt, Exception:
        raise KeyboardInterrupt
    return

class LaunChair:
    def __init__(self):
        self.jobfile = None
        self.work = None
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

    def run(self, cores_per_task):
        n_cpus = mp.cpu_count()
        if cores_per_task > n_cpus:
            raise ValueError("The number of cores per task must be less than the number of CPUs.")
        size = n_cpus / cores_per_task

        p = mp.Pool(size)
        try:
            ret = p.map_async(func, self.work).get(100000)
            p.wait()
        except KeyboardInterrupt:
            p.terminate()
            exit(1)

        return

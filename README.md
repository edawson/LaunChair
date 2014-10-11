LaunChair: A Barebones Pure-Python Parallel Job Launcher
---------------------------------------------
Eric T Dawson  
October 2014

## Background
There is a lot of computational power out there that never gets utilized.
Nearly every digital device today, be it a cell phone or supercomputer,
has multiple cores.  But sometimes we single-threaded human beings do
things that waste all this power at our fingertips. Worst of all, we
waste our own time when we do inherently parallel tasks in serial.


LaunChair makes it easy to run a list of independent serial or multithreaded
tasks in parallel on your laptop or workstation. It can make things like
parameter sweeps much faster with just one or two extra lines of code. It owes
its pedigree and the vast majority of its design to PyLauncher, a project by
Viktor Eijkhout (available [here](https://bitbucket.org/VictorEijkhout/pylauncher)).


LaunChair is developed and maintained on Linux but should work on Mac OS X
out of the box. While nothing in LaunChair prevents it from working on Windows,
it has not been tested on the platform.

## What LaunChair is:
1. A simple framework for running shell commands in parallel.
2. A pure-Python module with no dependencies.
3. A way to utilize all of the cores on a single machine.

## What LaunChair isn't:
1. A replacement for a real job scheduler like SLURM or SGE.
2. An MPI-based parallel job launcher.
3. Complicated; LaunChair is simple first and foremost.
   There should be almost no learning curve, and that is
   undoubtedly its best attribute.
4. Omniscient: LaunChair doesn't know a lot about your
   system or what you're doing with it. And for most tasks,
   that's okay!
5. Perfect. LaunChair is a work in progress and developed
   mostly for personal use. If you have suggestions for how
   to improve it please contact me!
   
## Using LaunChair
LaunChair is designed to get you up and running quick so you
can kick back and relax while your job runs. Let's do a quick example
by echoing all the numbers from 1 to 10000. In BASH, that goes like:

        for i in {1..10000}
        do
            echo "This is my number: ${i}"
        done

Let's say we don't care about order and we want to make this process faster.
LaunChair can help us with this. Let's see how:

        ## First, we write all of our commands to a single command file
        ## each line is a command.
        for i in {1..10000}
        do
            echo "echo 'This is my number: ${i}'" >> jobfile.txt
        done
        
        ## Now we just feed LaunChair our file and (optionally) the number of
        ## cores per task, and we're off!
        python launcher.py -i jobfile.txt
        
That's it! By default LaunChair assigns one core per task, so for something like
```echo``` we don't need to specifiy a core count. But if we had a parallel program
we wanted to do a parameter sweep on, we could explicitly tell it how many cores to use
like so:

        python launcher.py -i jobfile.txt -c 4
        
This would launch each command with 4 cores. At this point you can kick back, relax,
and let LaunChair do the work for you.
 
## Common Questions and Answers
Q: I used LaunChair and my job didn't get faster. Why?!
A: Real computers don't have an infinite number of cores. LaunChair will very likely
speed up serial tasks and those that don't scale well, but it isn't designed for all
problems. For problems that are already multithreaded or when giving a number of cores
per task equal to the number of cores on your system, you should reconsider using LaunChair.


Q: There are fewer than 100 lines of code in this whole package...
A: Yep! LaunChair is simple. It may grow in size in the future. Because
   it began as something for personal use it's really not meant as a sophisticated
   solution to every problem. I just got tired of doing parameter sweeps by hand.
   
Q: Will there be future improvements?
A: I sure hope so!
LaunChair: A Barebones Pure-Python Parallel Job Launcher
---------------------------------------------
Eric T Dawson  
October 2014

## Background
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
        
This would launch each command with 4 cores. To specify the number of cores on a machine (rather than
automatically using all of them), use the `-n` flag.  
```
        # Give each task four cores and specify that a machine has 8 total cores.
        python launcher.py -i jobfile.txt -c 4 -n 8
```

**N.B.: Make sure to delete or rename your jobfile.txt (or other launcher file) between runs, so that 
you don't concat them all together.**
 
## Common Questions and Answers

Q: There are fewer than 100 lines of code in this whole package...
A: Yep! LaunChair is simple. It may grow in size in the future. Because
   it began as something for personal use it's really not meant as a sophisticated
   solution to every problem. I just got tired of doing parameter sweeps by hand.


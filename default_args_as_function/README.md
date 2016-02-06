# default_args_as_function
------
It is possible to use functions to supply default arguments via functions.  These files let you explore this behaviour.

Run the examples like
* python3 simple.py 
	* Uses the system time as the default value for the argument.  Calls are made 1 second apart.  Notice how the time does not change.
* python3 primary_module.py
	* Uses a random number generator.  As distributed essentially demonstrates simple.py using randoms instead of time.  Use this file to see what happens if you comment out the function that supplies the default value or try raising an exception in the function.  Interesting failure modes.

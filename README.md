# clicker

An OSX/python based script for playing idle/incremental games that
require mouse clicks.

## tl;dr

You can just run this as a standard python script, and it will
happily start clicking away at the current mouse position, and will
end when you move your mouse, or after 10,000 clicks.

## requirements

This requires the OSX provided version of python, or at least a
version that includes the Quartz system modules.

There is a slight delay when the script starts up, as there is some
initialization when the Quartz.CoreGraphics module is initialized.
I prefer to run python interactively, then import clicker and run
the functions explicitly:

```
$ /usr/bin/python
Python 2.7.10 (default, Jul 14 2015, 19:46:27)
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.39)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import clicker
>>> clicker.clicklots(x={x-position},y={y-position})
```

## module definitions

There are only two definitions which you'll really care about:

### currentpos

Gets the current mouse position, prints out the text for calling
the clicklots function with populated definition, and returns the
coordinates as a tuple.

### clicklots

Clicks.  Lots.

#### parameters

 x | horizontal position for mouse
 y | vertical position for mouse
 z | click delay
 l | number of iterations (loops)

## caveats

Depending on what application you're clicking on, the mouse events
may be buffered.  This will cause a delay in exiting the function
while the application processes the backlog of events.  You may
want to adjust the timing of the clicks with the z parameter
accordingly.

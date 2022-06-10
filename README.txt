Simply a basic python-based display generator that uses a Windows OS cmd as the gui.

There were a few iterations created before this, some with more complexity (look at /Chess for example). However, this was created for the sole purpose of being simple to manage.

NewBase holds all of the array generation and graphical array constuction. At the subsection '# Array Updater Function', a function from newFunctions can be selected to be used to update the numerical array (which is then used to build the graphical display later in NewBase).

There are a few simple examples in newFunctions presently. The most complex example being mathGraph which can graph any single-variable function in the first quadrant. It is set by default to graph a modified sine wave into the center of the display.
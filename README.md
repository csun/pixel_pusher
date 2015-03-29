# pixel_pusher
A toolkit and visualizer for the Optimization question @ Northeastern's Code Showdown 2015

## Requirements
Any system with python installed can run the crucial scripts. If you're running Windows, run the scripts with `python` instead of invoking them directly. 

The `time` script is designed for *nix systems only.

## File Formats
All pixel_pusher scripts either input or output files of the following types:

### Palette
Defines an ordering of pixels in the palette. The first line is N, the number of rows / columns the square palette has. The next N lines contain N space-separated values of each pixel. An asterisk is used for the hole in the palette.
	
	4
	1 2 3 4
	5 6 7 8	
	9 10 11 *
	13 14 15 12

### Pushes
Defines an ordered list of pixel-pushes. The first line is M, the number of pushes contained in the file. The next M lines contain R and C, two space separated integers denoting the row and column of the pixel to be moved
	
	1
	3 3

Note that this push list solves the palette above.

## Scripts
There are four scripts included in this repository to help you get started.

### check
`./check PALETTE_PATH PUSHES_PATH`

Takes in a path to a palette file and a pushes file and outputs wheter or not the palette has been solved, and in how many moves.

### generate
`./generate PALETTE_SIZE NUM_PUSHES OUTPUT_FILE`

Takes in two integers and a file path. Generates a palette with PALETTE_SIZE rows and columns, performs NUM_PUSHES random pushes, and writes the result to OUTPUT_FILE. If you do not specify an OUTPUT_FILE, generate will write to `in.palette`.

### visualize
`./visualize PALETTE_PATH PUSHES_PATH`

Arguments are the same as `check`. Lets you watch all the moves happen in real time.

### time
`./time COMMAND`

Times your program and kills it if it takes longer than 15 seconds. This is what we will be using to actually run programs. If your program takes less than 15 seconds, the time it took to run will be printed.

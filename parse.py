#!/usr/bin/env python3

# This file parses adudump output
# It expects 2 arguments:
#  Minimum size, and filename.

import sys

# If the wrong number of arguments, print usage
if(len(sys.argv) != 3):
    print("Usage: "+sys.argv[0]+" minSize filename")
    print("Example: "+sys.argv[0]+" 100000 example.adu")

# If the first argument isn't only [0-9], print error
elif(not sys.argv[1].isdigit()):
    print("Error: Parameter is not a digit")

# Otherwise parse the file
else:
    # Gather command line parameters
    minSize = int(sys.argv[1])
    filename = sys.argv[2]

    #Try to open the file, if an error is encounter, print an error and halt
    try:
        file = open(filename, 'r')
        lines = file.readlines()
        fileOut = open(filename+".out", 'w')
    except:
        print("Unexpected error: ", sys.exc_info()[0])
        raise

    #For each line in the file, split it into an array
    for line in lines:
        fields = line.split()

        #We only want lines that begin with ADU
        lineType = fields[0][0:3]
        if(lineType != "ADU"):
            continue

        #We only want lines that surpass the minimum size
        size = int(fields[5])
        if(size < minSize):
            continue

        timestamp = fields[1]

        #Get the direction (first character only)
        direction = fields[3][0]

        #Set the source and destination based on direction
        if(direction == ">"):
            srcInd = 2
            dstInd = 4
        else:
            srcInd = 4
            dstInd = 2

        #These fields are formatted like this: 123.123.123.123.123 with the last portion as the port
        #This splits the port from the rest of the string, creating an array with [0] as ip and [1] as port
        src = fields[srcInd].rsplit('.', 1)
        dest = fields[dstInd].rsplit('.', 1)

        if(src[1] != "443"):
            continue

        #Write the result to the output file
        fileOut.write(timestamp+"\t"+src[0]+":"+src[1]+"\t>\t"+dest[0]+":"+dest[1]+"\t"+str(size)+"\n")

    # Close the output file when we are done
    fileOut.close()
# aduparse

This python script does a quick parsing of data from adudump.

It accepts 2 parameters, the first is an integer to use for the minimum size (other ADU entries are filtered out). THe second parameter is the filename. The resulting parse is output to filename+".out". To see an example of this parsing have a look at the test data.

### Generating Data
To generate the data to be used by the script, the following commands are used:

```
sudo tcpdump -i wlp1s0 -s 0 -w ./testdata.tcp
```
```
./adudump ./testdata.tcp -l 123.123.123.123/16 -q 500 ./testdata.adu
```
_Note:_ Replace `wlp1s0` with your own interface and the ip/mask with your own. You may use the command `ip a` to gather this information.

### Run the Script
```
./parse.py 50000 ./testdata.adu
```

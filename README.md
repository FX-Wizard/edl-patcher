# EDL patcher

Fixes EDL files exported from Avid so they can be imported into Shotgrid.

## How does it work
For each "SHOT" in the EDL it replaces the "Tape ID" with the "Shot code".

## How to use it
1. Enter a search pattern to match the shot names, regex is supported for the search
2. Open one or more EDL file(s)

### For example

If you have a shot called 

`VFX_101028_500`

enter a regex search pattern like 

`VFX_[0-9]{6}_[0-9]{3}`

This will allow the tool to find all the shots with that pattern in the EDL and put them in place of the tape ids.

Next open an EDL file and it will save out a new EDL fixed EDL file with the prefix _fixed.edl
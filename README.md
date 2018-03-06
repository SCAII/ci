# ci
Common continuous integration scripts for all SCAII environments and libraries

## gen_protos.py
General-purpose protobuf compile scipt for SCAII and Sky-RTS. 
Requires Python 3

### Usage:
1. Clone SCAII and Sky-RTS repos into desired location
2. Clone this repo (CI) into both SCAII and Sky-RTS
3. Execute this script with command `python gen_protos.py`
    - In SCAII, this script will find the directory containing `scaii.proto`, `cfg.proto`, and `viz.proto`. It will then output `vizProtos.js` into `SCAII/viz/js` and `scaii_pb2.py`, `cfg_pb2.py`, `viz_pb2.py` into `SCAII/glue/python/scaii/protos/`
    - In Sky_RTS, this script will find the directory containing `sky-rts.proto`. It will then output `sky_rts_pb2.py` into `Sky-RTS/game_wrapper/python/protos/`.
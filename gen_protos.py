#!/usr/bin/env python3
import os, fnmatch

def gen_protos(input_path, output_path, target, lang):
    if(os.path.isdir(input_path)):
        all_proto = ''
        if target != '':
            for proto in os.listdir(input_path):
                all_proto += ' '+ input_path + proto
            cmd = 'protoc --proto_path='+ input_path +' --'+lang+'_out=library='+target+':'+output_path+ " "+ all_proto
            if (os.system(cmd) != 0):
                print('ERROR: '+ target + ' proto generation failed')
            else:
                print(cmd)
                print('Success ' + target + '.' + lang)
        else:
            for proto in os.listdir(input_path):
                cmd = 'protoc --proto_path='+ input_path +' --'+lang+'_out=library:' + output_path +' '+input_path+proto
                if (os.system(cmd) != 0):
                    print(cmd)
                    print('ERROR: '+ proto + ' generation failed')
                else:
                    print(cmd)
                    print('Success ' + proto)

# Find a file and return the directory
def find(pattern, path):
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                return os.path.join(root)

# Get path and make sure the first directory found has all the files in it.
def check_paths(files_arr):
    dir = find(files_arr[0], os.getcwd())
    if (len(files_arr) > 1):
        for p in range(1, len(files_arr)):
            current = find(files_arr[p], os.getcwd())
            if dir == current:
                return str(dir) + "/"
            else:
                print("ERROR: Could not find directory with files: " + str(files_arr))
                exit(1)
    else:
        return str(dir) + "/"

# Assume the script is cloned into SCAII or Sky_RTS.
# Get curent directory and go up one level.
if "ci" not in str(os.getcwd()):
    os.chdir(os.path.basename(os.path.dirname(os.path.realpath(__file__))))
os.chdir('..')

# Array that holds all raw protos in SCAII
# Identifies /SCAII/protos/
SCAII_protos = ['scaii.proto', 'cfg.proto', 'viz.proto']

# Array that holds compiled names for SCAII
# Identifies /SCAII/viz/js
SCAII_vizProtos = ['vizProtos.js']

# Array that holds compiled protos names for SCAII
# Identifies /SCAII/glue/python/scaii/protos/
SCAII_python = ['scaii_pb2.py', 'cfg_pb2.py', 'viz_pb2.py']

# Array that holds raw protos names for Sky-RTS 
# Identifies /Sky-RTS/protos/
sky_rts_protos = ['sky-rts.proto']

# Array that holds compiled protos names for Sky_RTS
# Identifies /Sky-RTS/game_wrapper/python/protos/
sky_rts_python = ['sky_rts_pb2.py']

# Generate vizProtos.js for SCAII
input_path = check_paths(SCAII_protos)
output_path = check_paths(SCAII_vizProtos)
target = 'vizProtos'
lang = 'js'
gen_protos(input_path, output_path, target, lang)

# Generate all python protos for SCAII
input_path = input_path
output_path = check_paths(SCAII_python)
target = ''
lang = 'python'
gen_protos(input_path, output_path, target, lang)

# Generate all python protos for Sky-rts
input_path = check_paths(sky_rts_protos)
output_path = check_paths(sky_rts_python)
target = ''
lang = 'python'
gen_protos(input_path, output_path, target, lang)

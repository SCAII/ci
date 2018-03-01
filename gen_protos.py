#!/usr/bin/env python3
import os
from sys import platform
from subprocess import call

def get_platform():
    if platform == "linux" or platform == "linux2":
        return "linux"

    elif platform == "darwin":
        return "macos"

    elif platform == "win32":
        return "windows"

def check_age(proto):
    age = os.stat(proto).st_mtime
    print(age)

def usage():
    print("\t\tUsage:")
    print("\tproto to python \t\t -p")
    print("\tproto to javascript \t-j")

def gen_viz_protos():
    path = '../common_protos/'
    if(os.path.isdir(path)):
        all_proto = ''
        for proto in os.listdir(path):
            all_proto += ' '+ path + proto

        cmd = 'protoc --proto_path='+ path +' --js_out=library=vizProtos:.' + all_proto
        os.system(cmd)

def gen_python_protos():
    path = '../game_wrapper/'
    if(os.path.isdir(path)):
        all_proto = ''
        for proto in os.listdir(path):
            all_proto += ' ' + path + proto
        cmd = 'protoc --proto_path='+ path +' --python_out=library=vizProtos:.' + all_proto
        print(cmd)


gen_viz_protos()
gen_python_protos()
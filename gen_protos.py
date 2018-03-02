#!/usr/bin/env python3
import os

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

# Generate vizProtos.js for SCAII
input_path = '../common_protos/'
output_path = '../viz/js/'
target = 'vizProtos'
lang = 'js'
gen_protos(input_path, output_path, target, lang)

# Generate all python protos for SCAII
input_path = '../common_protos/'
output_path = '../glue/python/scaii/protos/'
target = ''
lang = 'python'
gen_protos(input_path, output_path, target, lang)

# Generate all python protos for Sky-rts
input_path = '../protos/'
output_path = '../game_wrapper/python/protos/'
target = ''
lang = 'python'
gen_protos(input_path, output_path, target, lang)

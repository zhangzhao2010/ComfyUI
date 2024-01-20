#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""uvicorn main module"""
import time
import os
import subprocess

reload=os.environ.get("reload", False)
if __name__ == '__main__':
    process = subprocess.Popen(
                ["python3","/opt/program/main.py","--listen","0.0.0.0","--port","8080"],
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, preexec_fn=os.setpgrp)
    if process.returncode is not None:
            raise RuntimeError("Failed to start ComfyUI process.")
    time.sleep(10)
    print("comfyui started!")

    #uvicorn.run('api_server:app',host='0.0.0.0',port=8080,reload=reload,log_level='info')
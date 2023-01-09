#!/usr/bin/env python3

import shutil
import psutil


du = shutil.disk_usage('/')
print(du)
print(du.free/du.total*100)
percent = psutil.cpu_percent(0.5)
print(percent)

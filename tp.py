

#import subprocess

#out0 = subprocess.check_output("cd ..", shell = True)
#print(out0)

#out1 = subprocess.check_output("git init", shell=True)
#print(out1)

#out2 = subprocess.check_output(["git", "add", "tp.py"])
#print(out2)

#out3 = subprocess.check_output("git status", shell=True)
#print(out3)

#out4 = subprocess.check_output(["git", "commit", "-m", "'adding tp.py'"])
#print(out4)

#cmd = subprocess.Popen('cmd.exe /K cd /')

#os.system("start cmd")
#os.system("git init")

#os.system("git add readME.txt")
#os.system("git status")
#os.system("git rm --cached -f tp.py")
#o = os.system('dir C:')
#print(o)
#os.system('git commit -m "adding readME"')

#import subprocess
#process = subprocess.Popen('cmd /k ', shell=True, stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=None)
#process.stdin.write(b"dir C:")                 #passing command
#stdOutput,stdError = process.communicate()
#print(stdOutput)
#process.stdin.close()
#####################################################################################################################


import os

address = os.getcwd().replace('\\', '/')
print(address)
os.chdir(address)

cwd = os.getcwd()
print(cwd)



#os.system('git init')
#os.system('git pull https://github.com/ame-madhekar-7/sorcerers-code.git')
#os.system('git add readME.txt')
#os.system('git commit -m "adding readME.txt"')
#os.system('git push https://github.com/ame-madhekar-7/sorcerers-code.git master')



#import sys
#import re
#import requests
#import os

#url = 'https://files.slack.com/files-pri/T015A1GPAL8-F015NJLMQ95/_nludates.md'

#token = 'xoxb-1180050792688-1160281224518-0fv56r6W4CVZaGsBTzOviMKX'
#resp = requests.get(url, headers={'Authorization': 'Bearer %s' % token})

#fname = 'config.txt'

#assert not os.path.exists(fname), print("File already exists. Please remove/rename and re-run")
#out_file = open(fname, mode="wb+")
#out_file.write(resp.content)
#out_file.close()



#parameter = {'token':'xoxb-1180050792688-1160281224518-0fv56r6W4CVZaGsBTzOviMKX'}
#response = requests.get(
#    'https://slack.com/api/files.list',
#    params = parameter,
#    headers={'content-type': 'application/x-www-form-urlencoded'},
#)
#json_response = response.json()
#print(json_response)





# deleting pulled repo and .git ???
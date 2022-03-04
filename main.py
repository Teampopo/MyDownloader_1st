import time
import pandas as pd
import os
import clipboard

workingDir = ('F:/ffmpeg')
executeFile = ('F:/ffmpeg/downloader.bat')

def run(path):
    os.chdir(workingDir)
    os.system(path)

dataset1 = pd.read_excel('C:/Users/upica/Documents/excel/downloader.xlsx')
df = pd.DataFrame(dataset1)
print(len(df.index))

i = 0
#
# for index, row in df.iterrows():
#     print(row[0])
#     clipboard.copy(str(row[1]))
#     run(executeFile)

for index, row in df.iterrows():
    print(str(workingDir) + '/ffmpeg -i ' + str(row[1] + ' -c copy -bsf:a aac_adtstoasc ' + str(row[0]) + str(time.strftime('%Y%m%d%H%M%S')) + '.mkv'))
    os.popen(str(workingDir) + '/ffmpeg -i ' + str(row[1] + ' -c copy -bsf:a aac_adtstoasc ' + str(row[0]) + str(time.strftime('%Y%m%d%H%M%S')) + '.mkv'))
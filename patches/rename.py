import glob

for f in sorted(glob.glob('./*')):
    patchpath = f + '/'
    patchname = f[2:] + '.py'
    #print patchname
    #print patchpath
    for fn in sorted(glob.glob(patchpath + '*.py')):
        print 'mv ' + fn + ' ' + patchpath + patchname

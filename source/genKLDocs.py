import os
import sphinx

from ASTWrapper import *

# note: the extsDir also has to be on the FABRIC_EXTS_PATH env var
extsDir = os.path.join(os.environ.get('KRAKEN_PATH'), 'Exts')
tmpDir = 'c:\\temp\\build'
srcDir = os.path.dirname(os.path.realpath(__file__))
extSrcDir = os.path.join(srcDir, 'kl', 'extensions')
stageDir = 'c:\\temp\\docs'

print "============================"
print type(srcDir)
print "============================"

for d in [tmpDir, srcDir, stageDir]:
    if not os.path.exists(d):
        os.makedirs(d)

        os.environ['RST_DOC_SOURCE_EXTS_DIR'] = os.path.join(stageDir, 'Extensions')
os.environ['RST_DOC_TARGET_EXTS_DIR'] = extSrcDir

# create the ast manager
manager = KLManager(paths=[extsDir], header=[])

# create all extension rst files
extensions = manager.getKLExtensions()
for extension in extensions:
    srcExtDir = os.path.join(extSrcDir, extension.getName())
    if not os.path.exists(srcExtDir):
        os.makedirs(srcExtDir)
    extTmpDir = os.path.join(tmpDir, extension.getName())
    if not os.path.exists(extTmpDir):
        os.makedirs(extTmpDir)
    manager.generateKLExtensionRST(extension, srcExtDir, extTmpDir)

# invoke sphinx
sphinx.main(['-b html', '-E', '-a', srcDir, stageDir])

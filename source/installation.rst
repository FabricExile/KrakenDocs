============
Installation
============

.. contents::
   :local:

|

##############
Pre-Requisites
##############
* Fabric Engine 2.0.x
* PySide 1.2.2
* Python 2.7.x
* PyWin32 (Softimage requirement)
* PyQtForSoftimage (PySide compatible version)

|

########
Download
########
Get the latest version of Kraken here:
`Kraken Downloads <http://fabric-engine.github.io/Kraken/#download>`_

|

################
DCC Installation
################

|

.. _installation-softimage:

**********************
Softimage Installation
**********************
Users must download the PyQtForSoftimage workgroup found here:
http://www.steven-caron.com/downloads/tools/PyQtForSoftimage_beta6.xsiaddon

Once the pre-requisites have been installed, you need to connect to a few workgroups.

**The order of the workgroups should be:**

1. Fabric Engine
2. PyQtForSoftimage
3. Kraken

|

.. _installation-maya:

*****************
Maya Installation
*****************
Once the pre-requisites have been installed, you need to add Fabric and Kraken to the MAYA_MODULE_PATH. See the example launcher script below or see teh Maya documentation on how to add paths to the MAYA_MODULE_PATH.

Once added, you'll have to activate the plug-ins by going to Window > Settings / Preferences > Plug-in Manager. There you should activate:

1. FabricSplice.mll
2. kraken_maya.py

|

.. _installation-envvars:

#####################
Environment Variables
#####################
|


.. envvar:: KRAKEN_PATH

   Base directory where Kraken is installed.

.. envvar:: KRAKEN_PATHS

   Paths to custom components and configs.

.. envvar:: KRAKEN_LOAD_MENU

   If set to False, the Kraken Menu will not load in the DCC's. However the commands will still be registered.

|

########################
Example Launcher Scripts
########################
|

******************
Windows Standalone
******************
|

.. highlight:: bash

::

   call D:\fabric\FabricEngine-2.0.1-Windows-x86_64\environment.bat


   set KRAKEN_PATH=D:\dev\kraken
   set FABRIC_EXTS_PATH=%FABRIC_EXTS_PATH%;%KRAKEN_PATH%\Exts;
   set FABRIC_DFG_PATH=%FABRIC_DFG_PATH%;%KRAKEN_PATH%\Presets\DFG;
   set PYTHONPATH=%PYTHONPATH%;%KRAKEN_PATH%\Python;

   cd /d %KRAKEN_PATH%

   call cmd

**************
Softimage 2015
**************
|

.. highlight:: bash

::

   call D:\fabric\FabricEngine-2.0.1-Windows-x86_64\environment.bat

   set KRAKEN_PATH=D:\dev\kraken
   set FABRIC_EXTS_PATH=%FABRIC_EXTS_PATH%;%KRAKEN_PATH%\Exts;
   set FABRIC_DFG_PATH=%FABRIC_DFG_PATH%;%KRAKEN_PATH%\Presets\DFG;
   set PYTHONPATH=%PYTHONPATH%;%KRAKEN_PATH%\Python;

   call "C:\Program Files\Autodesk\Softimage 2015 SP1\Application\bin\XSI.bat"

   echo OFF

*********
Maya 2016
*********
|

.. highlight:: bash

::

   call D:\fabric\FabricEngine-2.0.1-Windows-x86_64\environment.bat

   set KRAKEN_PATH=D:\dev\kraken
   set FABRIC_EXTS_PATH=%FABRIC_EXTS_PATH%;%KRAKEN_PATH%\Exts;
   set FABRIC_DFG_PATH=%FABRIC_DFG_PATH%;%KRAKEN_PATH%\Presets\DFG;
   set PYTHONPATH=%PYTHONPATH%;%KRAKEN_PATH%\Python;

   set MAYA_MODULE_PATH=%MAYA_MODULE_PATH%;%FABRIC_DIR%\DCCIntegrations\FabricMaya2016;%KRAKEN_PATH%\DCCIntegrations\maya;

   start /d "C:\Program Files\Autodesk\Maya2016\bin" maya.exe


.. include:: footer.rst
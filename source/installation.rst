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

.. envvar:: KRAKEN_DCC

   The DCC that Kraken is being used by. This environment variable is used in a few places, mainly for acquiring the correct builder and synchronizer.

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

Example launcher scripts can be found in ``%KRAKEN_DIR%\extras\launcher_scripts\windows``

******************
Windows Standalone
******************
|

.. highlight:: bash

::

   call C:\Users\Eric\Documents\fabric\FabricEngine-2.2.0-Windows-x86_64\environment.bat

   set KRAKEN_PATH=C:\Users\Eric\Documents\dev\kraken
   set FABRIC_EXTS_PATH=%FABRIC_EXTS_PATH%;%KRAKEN_PATH%\Exts;
   set FABRIC_DFG_PATH=%FABRIC_DFG_PATH%;%KRAKEN_PATH%\Presets\DFG;
   set PYTHONPATH=%PYTHONPATH%;%KRAKEN_PATH%\Python;

   cd /d %KRAKEN_PATH%\Python\kraken\ui

   call cmd /k "python kraken_window.py"


   PAUSE

**************
Softimage 2015
**************
|

.. highlight:: bash

::

   @ECHO OFF
   ECHO "Releasing The Kraken!"

   set FABRIC_EXTS_PATH=C:\Users\Eric\Documents\CustomExts;
   set FABRIC_DFG_PATH=C:\Users\Eric\Documents\CustomPresets;

   call "C:\Program Files\Autodesk\Softimage 2015 SP1\Application\bin\XSI.bat"

   echo OFF

*********
Maya 2016
*********
|

.. highlight:: bash

::

   @ECHO OFF
   ECHO "Releasing The Kraken!"

   set FABRIC_EXTS_PATH=C:\Users\Eric\Documents\CustomExts
   set FABRIC_DFG_PATH=C:\Users\Eric\Documents\CustomPresets

   set MAYA_MODULE_PATH=C:\Users\Eric\Documents\fabric\FabricEngine-2.2.0-Windows-x86_64\DCCIntegrations\FabricMaya2016;C:\Users\Eric\Documents\dev\kraken\DCCIntegrations\maya;

   start /d "C:\Program Files\Autodesk\Maya2016\bin" maya.exe

   echo OFF


.. include:: footer.rst
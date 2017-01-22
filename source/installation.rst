============
Installation
============

.. contents::
   :local:

|

.. _pre-requisites-core:

###################
Core Pre-Requisites
###################
* PySide 1.2.2
* Python 2.7.x
* Fabric Engine 2.2.x or greater (2.3.x for Softimage)

|

.. _pre-requisites-maya:

########################
Maya Pre-Requisites
########################
* Core Pre-requisites

|

.. _pre-requisites-softimage:

########################
Softimage Pre-Requisites
########################
* Core Pre-requisites
* PyWin32 (Softimage requirement)
* PyQtForSoftimage (PySide compatible version)

|

########
Download
########
Get the latest version of Kraken here:
`Kraken Downloads <http://fabric-engine.github.io/Kraken/#download>`_

|

######
Un-Zip
######
Un-zip the Kraken archive to a folder of your choice. We DO NOT recommend putting it into the ``Program Files`` directory on Windows as it is not in installed application. It is also HIGHLY recommended NOT to put it into the Fabric Engine directory.

Kraken is a stand alone application that relies on Fabric Engine but does not need to be in the same directory. Additionally, this also helps in the instance where you want to upgrade Fabric Engine but leave the current version of Kraken where it is.


########################
Stand Alone Installation
########################
Once the :ref:`pre-requisites <pre-requisites-core>` have been installed and Kraken has been un-zipped you can run the Kraken stand alone.

On Windows, you can do this by finding the sample launcher batch file in ``%KRAKEN_DIR/extras/launcher_scripts/windows`` and copying it to the desktop. Then edit it to reflect the valid locations of the Fabric Engine ``environment.bat`` and also the directory path for Kraken.

.. seealso:: :ref:`Stand Alone Launcher Sample <launcher-stand-alone>`

Once complete you can double click the ``kraken_launcher.bat`` to launch the Kraken stand alone application.

################
DCC Installation
################

|

.. _installation-softimage:

**********************
Softimage Installation
**********************

**Supported versions:** 2015 SP2

Users must download the PyQtForSoftimage workgroup found here:
http://www.steven-caron.com/downloads/tools/PyQtForSoftimage_beta6.xsiaddon

Once the :ref:`pre-requisites <pre-requisites-softimage>` have been installed, you need to connect to a few workgroups.

**The order of the workgroups should be:**

1. Fabric Engine
2. PyQtForSoftimage
3. Kraken

.. seealso:: :ref:`Softimage Launcher Sample <launcher-softimage>`

|

.. _installation-maya:

*****************
Maya Installation
*****************

**Supported versions:** 2015, 2016, 2017

Once the :ref:`pre-requisites <pre-requisites-maya>` have been installed, you need to add Fabric Engine's Maya plug-in path and the Kraken Maya plugin's path to the ``MAYA_MODULE_PATH`` environment variable.

This can be done in a few ways but we suggest using a ``*.bat`` or ``*.sh`` script to set the ``PYTHONPATH`` AND ``MAYA_MODULE_PATH`` environment variables and to also call Maya's executable to launch it with the correct environment. See the example launcher script below or see the Maya documentation on how to add paths to the ``MAYA_MODULE_PATH``.

.. seealso:: :ref:`Maya Launcher Sample <launcher-maya>`

Once you've launched Maya with the evironment variables set, you'll have to activate the plug-ins by going to ``Window > Settings / Preferences > Plug-in Manager``. There you should activate:

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

.. _launcher-stand-alone:

******************
Windows Standalone
******************

|

.. code:: bash

   call C:\Users\Eric\Documents\fabric\FabricEngine-2.2.0-Windows-x86_64\environment.bat

   set KRAKEN_PATH=C:\Users\Eric\Documents\dev\kraken
   set FABRIC_EXTS_PATH=%FABRIC_EXTS_PATH%;%KRAKEN_PATH%\Exts;
   set FABRIC_DFG_PATH=%FABRIC_DFG_PATH%;%KRAKEN_PATH%\Presets\DFG;
   set PYTHONPATH=%PYTHONPATH%;%KRAKEN_PATH%\Python;

   cd /d %KRAKEN_PATH%\Python\kraken\ui

   call cmd /k "python kraken_window.py"


   PAUSE

.. _launcher-softimage:

**************
Softimage 2015
**************

|

.. code:: bash

   @ECHO OFF
   ECHO "Releasing The Kraken!"

   set FABRIC_EXTS_PATH=C:\Users\Eric\Documents\CustomExts;
   set FABRIC_DFG_PATH=C:\Users\Eric\Documents\CustomPresets;

   call "C:\Program Files\Autodesk\Softimage 2015 SP1\Application\bin\XSI.bat"

   echo OFF

.. _launcher-maya:

*********
Maya 2016
*********

|

.. code:: bash

   @ECHO OFF
   ECHO "Releasing The Kraken!"

   set FABRIC_EXTS_PATH=C:\Users\Eric\Documents\CustomExts
   set FABRIC_DFG_PATH=C:\Users\Eric\Documents\CustomPresets

   set MAYA_MODULE_PATH=C:\Users\Eric\Documents\fabric\FabricEngine-2.2.0-Windows-x86_64\DCCIntegrations\FabricMaya2016;C:\Users\Eric\Documents\dev\kraken\DCCIntegrations\maya;

   start /d "C:\Program Files\Autodesk\Maya2016\bin" maya.exe

   echo OFF


.. include:: footer.rst
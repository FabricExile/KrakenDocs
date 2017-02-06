.. _py_unittests:

================
Python Unittests
================


.. contents:: Usage Documentation
   :local:


What are unit tests?
====================
Unit tests are python scripts that test the expected functionality for the Python package they are included in. This ensure that while developing and changing code within the Python package, that the changes don't break previous functionality. Any time changes are pushed to the Kraken repository through a pull requests, will be required to run the unit tests to ensure changes haven't broken functionality.


Running Unit Tests
==================
To run the unit tests, you can copy the ``run_unittest.bat`` (Windows) or the ``run_unittest.sh`` (OSX / Linux) from ``%KRAKEN_DIR/extras/launcher_scripts/`` to the ``KRAKEN_PATH/unittests`` directory and update the ``FABRIC_DIR`` to point to the version of Fabric you are using.
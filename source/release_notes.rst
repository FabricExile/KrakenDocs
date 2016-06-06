=============
Release Notes
=============


.. release:: 0.1.0
    :date: 2015-01-01

    .. change:: new
        :tags: interface

        Added a fantastic new feature to the interface that you will all
        love.





*************
Version 1.2.0
*************

*Released 2016-06-01*


New Features
   * Generic Biped Rig now buildable via the DCC plug-ins. ``Softimage`` ``Maya``
   * Canvas Builder implemented ***WIP***. Canvas nodes can now be generated from ``*.krg`` files and can be instanced in Canvas. ``canvas`` ``builder``
   * KL Builder implemented ***WIP***.
   * Splash screen now shows KL loading progress via live logging from stdout. ``ui``
   * Implemented a proper logger via the Python logging module. Reports to stdout and UI output log. ``ui``
   * Added preference to ensure that the already built rig will be deleted before re-building a new one. ``ui``
   * Kraken now determines what plug-in to load based on the `KRAKEN_DCC` environment variable. ``core``
   * Traverser class now properly determines the order in which to build objects within a rig. This ensures that objects are built and evaluated in the correct order to ensure that objects are in the correct place when building dependent objects. ``core``
   * Twist Component used for wrist twist and other parts of bipeds now included. ``components``
   * Unit tests for all KL based solvers were created. ``kl`` ``unittest``


Fixed
   * Tentacle component woulnd't build due to port name restriction. Recently fix in Fabric. ``components``
   * Need to be able to connect object visibility to other attributes ``builder``
   * Kraken menu is removed when unloading the Kraken plug-in. ``Maya`` ``ui``
   * Kraken plug-in will now load Fabric plug-in if not loaded when it itself is loaded. ``Maya``\
   * Inline drawing ports are skipped when trying to make port connections. ``builder``


Changed
   * Builder acquisition code is now completely abstracted from the core modules. Now utilizes the plug-in structure. ``core``
   * Knee deformer now added to the leg component. ``components``
   * Re-designed the head and neck components. ``components``
   * Added hand component with more robust guide solver. ``components``
   * Re-organized components into biped and generic directories.
   * DCC builders now set constraint offset values and don't rely on DCC's to set them. ``Maya`` ``Softimage``
   * When launching Kraken, you know longer need to call the environment.bat / .sh.


*************
Version 1.1.0
*************

*Released 2016-01-15*


New Features
   * Added sample .bat launcher files. ``extras``
   * Core graph code extracted to PyflowGraph repo and added as a sub-tree. ``ui``
   * Backdrops have been added for grouping nodes. ``ui``
   * Add Color Attribute ``core``
   * Control object needs method "setShape". ``core``
   * Ability to refresh the Component list manually. ``core`` ``ui``
   * Use resource file for images. ``ui``
   * Snap to Grid. ``ui``
   * Node color should be taken from component .py files. ``ui``
   * Add Recent Files Menu. ``ui``


Fixed
   * Kraken Maya plugin auto loads matrixNodes plugin automatically now. ``Maya``
   * Spine pop fix. ``solvers``
   * Doing Save As doesn't update file path in title bar. ``ui``
   * Kraken UI won't open if one kraken path not found. ``ui``
   * Kraken UI Slow, and slowing the host UI. ``ui``


Changed
   * Use KRAKEN_PATH instead of KRAKEN_DIR in core and in launcher scripts. ``core``
   * Component Library widget to folder tree widget. ``ui``
   * Tracks opened file, save command simply saves file. ``ui``
   * When doing a save as / open, file name isn't stored or restored next time. ``ui``
   * Output log widget added to allow users to see the history. ``ui``
   * Error message is now full length of window and stays on screen longer. ``ui``
   * Renamed KLExts and DFG folders to be consistent with how core Fabric Engine nodes are organized. ``core``


*************
Version 1.0.0
*************

*Released 2015-08-11*

New Features
   * Added a PyQt based user interface for building rigs through nodes and connections. ``ui``
   * New Kraken Solver KL extension implements the base inteface and object that all Kraken solvers will inherit. Kraken Arg also works hand in hand with this new object. ``kl``
   * :doc:`/python/core/synchronizer` module allows synchronoization from DCC to the Python graph. This allows users to create guides, adjust them, then synch back to the graph to have those changes affect the final rig build.
     Also allows saving guides / graphs out as a preset file. ``core`` ``synchronizer``
   * :doc:`/python/core/kraken_system` module is a singleton object used to provide an interface with the FabricEngine Core and RTVal system. ``core`` ``kraken system``
   * :doc:`/python/core/profiler` object is for debugging performance issues during builds. Provides timing and labels. ``profiler``
   * :doc:`/python/core/maths/maths` library now wraps the KL math library to ensure there is a one to one mapping between the types and that the math evaluates exactly the same way. ``math``
   * :doc:`/python/core/objects/rig` object is sub-classed from the *Container* object and is used to load and save out presets of full rigs. Provided additional methods for doing so. ``rig``

Changed
   * Maya plug-in now fully supported. ``plugins`` ``maya``
   * Softimage plug-in now fully supported. ``plugins`` ``softimage``
   * :doc:`/python/core/objects/control` object now takes a *shape* argument and shapes are stored in the config. ``control`` ``config``
   * :doc:`/python/core/configs/config` object now stores the valid colors, sides, mirror mapping, naming template, and control shapes. This object is a singleton and can be sub-classed to provide customized configurations per studio, per project, or even per asset. ``control`` ``config``
   * Swapped names of Object 3D and Scene Item. Scene Item is now the base object for most simple objects without transforms. ``object 3d`` ``scene item``
   * Renamed srt buffer to ctrl space to be more intuitively named. ``srt buffer`` ``ctrl space``


.. include:: footer.rst
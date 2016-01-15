=============
Release Notes
=============


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
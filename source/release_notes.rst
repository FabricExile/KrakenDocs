=============
Release Notes
=============

Release Versions
================

* :ref:`Release 1.2.5 <release-1.2.5>`
* :ref:`Release 1.2.0 <release-1.2.0>`
* :ref:`Release 1.1.0 <release-1.1.0>`
* :ref:`Release 1.0.0 <release-1.0.0>`

|


.. _release-1.2.5:

.. release:: 1.2.5
   :date: 2017-01-16

   .. change:: new
      :tags: core

      Kraken is now included with Fabric Engine 2.4. Those wishing to have custom version will need to modify their environment.bat and launcher files accordingly.

   .. change:: new
      :tags: ui

      Using Qt.py module to have compatibility with PySide2 and Maya 2017.

      Note: Kraken for Maya 2017 is functional, however additional work is needed to fix the node graph.

   .. change:: new
      :tags: maya

      Kraken uses custom ``KrakenConstraint`` Maya node to improve rig performance. Can revert to core Maya constraints via ``UseMayaNativeConstraints`` meta data in config.

   .. change:: new
      :tags: solvers, presets

      Added 2 new solver presets for fk chain collision and spring arrays.

   .. change:: new
      :tags: solvers, core

      Solvers can now have default values set when defining solvers in KL extensions.

   .. change:: new
      :tags: config

      KL, Canvas Ops, and Constraints can now be named via the config.

   .. change:: new
      :tags: objects

      Objects now can now have flags set on creation using the ``flags`` keyword argument.

   .. change:: new
      :tags: joint

      Users can now set the joint radius via a keyword argument.

   .. change:: new
      :tags: utilities

      New utility script to generate Kraken Canvas presets for KL extensions and Solvers.

   .. change:: new
      :tags: core, builders

      Builders now check and report if Solvers and Constraints don't evaluate before build.

   .. change:: new
      :tags: core

      Kraken now uses KL auto namespacing.

   .. change:: fixed
      :tags: ui, preferences

      Config name is now saved in the application QT preferences instead of an index. ``*.krg`` rig files also store and load the config if found.

   .. change:: fixed
      :tags: core, synchronizer

      Skip syncing of Guide Settings.

   .. change:: changed
      :tags: core, maths

      Moved rotation order ``Integer`` to ``String`` mapping to constants module.

   .. change:: changed
      :tags: core, maths

      Rotation Order indices updated and sync'd with changes in Fabric Core.

   .. change:: changed
      :tags: ui

      Conform UX to Canvas interaction. Clicking on nodes move them to the foreground and push other nodes backwards.

   .. change:: changed
      :tags: core, components

      Component ``location`` changed to a String Attribute allowing for the on changed callback.

   .. change:: changed
      :tags: core, ui

      Logic to test if component ports can be connected moved from UI to core.

   .. change:: changed
      :tags: core, config

      Implemented 330-HTMLColors. We now use the standard HTML color strings for defining colors in Kraken. No longer use Maya color indices.

   .. change:: changed
      :tags: components

      Better debug drawing for the Dynamic Chain & FK Chain components, and Multipose Constraint solver.

   .. change:: changed
      :tags: core, maya, softimage

      Combined KL and CanvasOp methods to reduce duplicated code.


.. _release-1.2.0:

.. release:: 1.2.0
   :date: 2016-06-01

   .. change:: new
      :tags: softimage, maya

      Generic Biped Rig now buildable via the DCC plug-ins.

   .. change:: new
      :tags: canvas, builder

      Canvas Builder implemented ***WIP***. Canvas nodes can now be generated from ``*.krg`` files and can be instanced in Canvas.

   .. change:: new
      :tags: rigs

      Guide rig data used to build a rig is now stored on each rig as meta data. Users can re-generate guides from rigs now!

   .. change:: new
      :tags: KL, builder

      KL Builder implemented ***WIP***.

   .. change:: new
      :tags: ui

      Splash screen now shows KL loading progress via live logging from stdout.

   .. change:: new
      :tags: ui

      Implemented a proper logger via the Python logging module. Reports to stdout and UI output log.

   .. change:: new
      :tags: ui

      Added preference to ensure that the already built rig will be deleted before re-building a new one.

   .. change:: new
      :tags: core

      Kraken now determines what plug-in to load based on the `KRAKEN_DCC` environment variable.

   .. change:: new
      :tags: core

      Traverser class now properly determines the order in which to build objects within a rig. This ensures that objects are built and evaluated in the correct order to ensure that objects are in the correct place when building dependent objects.

   .. change:: new
      :tags: components

      Twist Component used for wrist twist and other parts of bipeds now included.

   .. change:: new
      :tags: KL, unittest

      Unit tests for all KL based solvers were created.


   .. change:: fixed
      :tags: components

      Tentacle component woulnd't build due to port name restriction. Recently fix in Fabric.

   .. change:: fixed
      :tags: builder

      Need to be able to connect object visibility to other attributes.

   .. change:: fixed
      :tags: maya, ui

      Kraken menu is removed when unloading the Kraken plug-in.

   .. change:: fixed
      :tags: maya

      Kraken plug-in will now load Fabric plug-in if not loaded when it itself is loaded.

   .. change:: fixed
      :tags: builder

      Inline drawing ports are skipped when trying to make port connections.

   .. change:: changed
      :tags: core

      Builder acquisition code is now completely abstracted from the core modules. Now utilizes the plug-in structure.

   .. change:: changed
      :tags: components

      Knee deformer now added to the leg component.

   .. change:: changed
      :tags: components

      Re-designed the head and neck components.

   .. change:: changed
      :tags: components

      Added hand component with more robust guide solver.

   .. change:: changed
      :tags: structure

      Re-organized components into biped and generic directories.

   .. change:: changed
      :tags: maya, softimage

      DCC builders now set constraint offset values and don't rely on DCC's to set them.

   .. change:: changed
      :tags: extras

      When launching Kraken, you know longer need to call the environment.bat / .sh and only need to set custom paths to custom extensions and dfg presets


.. _release-1.1.0:

.. release:: 1.1.0
   :date: 2016-01-15

   .. change:: new
      :tags: extras

      Added sample .bat launcher files.

   .. change:: new
      :tags: ui

      Core graph code extracted to PyflowGraph repo and added as a sub-tree.

   .. change:: new
      :tags: ui

      Backdrops have been added for grouping nodes.

   .. change:: new
      :tags: core

      Add Color Attribute

   .. change:: new
      :tags: core

      Control object needs method "setShape".

   .. change:: new
      :tags: core, ui

      Ability to refresh the Component list manually.

   .. change:: new
      :tags: ui

      Use resource file for images.

   .. change:: new
      :tags: ui

      Snap to Grid.

   .. change:: new
      :tags: ui

      Node color should be taken from component .py files.

   .. change:: new
      :tags: ui

      Add Recent Files Menu.

   .. change:: fixed
      :tags: maya

      Kraken Maya plugin auto loads matrixNodes plugin automatically now.

   .. change:: fixed
      :tags: solvers

      Spine pop fix.

   .. change:: fixed
      :tags: ui

      Doing Save As doesn't update file path in title bar.

   .. change:: fixed
      :tags: ui

      Kraken UI won't open if one kraken path not found.

   .. change:: fixed
      :tags: ui

      Kraken UI Slow, and slowing the host UI.

   .. change:: fixed
      :tags: core

      Use KRAKEN_PATH instead of KRAKEN_DIR in core and in launcher scripts.

   .. change:: fixed
      :tags: ui

      Component Library widget to folder tree widget.

   .. change:: fixed
      :tags: ui

      Tracks opened file, save command simply saves file.

   .. change:: fixed
      :tags: ui

      When doing a save as / open, file name isn't stored or restored next time.

   .. change:: fixed
      :tags: ui

      Output log widget added to allow users to see the history.

   .. change:: fixed
      :tags: ui

      Error message is now full length of window and stays on screen longer.

   .. change:: fixed
      :tags: core

      Renamed KLExts and DFG folders to be consistent with how core Fabric Engine nodes are organized.

.. _release-1.0.0:

.. release:: 1.0.0
   :date: 2015-08-11

   .. change:: new
      :tags: ui

      Added a PyQt based user interface for building rigs through nodes and connections.

   .. change:: new
      :tags: KL

      New Kraken Solver KL extension implements the base inteface and object that all Kraken solvers will inherit. Kraken Arg also works hand in hand with this new object.

   .. change:: new
      :tags: core, synchronizer

      :doc:`/python/core/synchronizer` module allows synchronoization from DCC to the Python graph. This allows users to create guides, adjust them, then synch back to the graph to have those changes affect the final rig build.

      Also allows saving guides / graphs out as a preset file.

   .. change:: new
      :tags: core, kraken system

      :doc:`/python/core/kraken_system` module is a singleton object used to provide an interface with the FabricEngine Core and RTVal system.

   .. change:: new
      :tags: profiler

      :doc:`/python/core/profiler` object is for debugging performance issues during builds. Provides timing and labels.

   .. change:: new
      :tags: math

      :doc:`/python/core/maths/maths` library now wraps the KL math library to ensure there is a one to one mapping between the types and that the math evaluates exactly the same way.

   .. change:: new
      :tags: rig

      :doc:`/python/core/objects/rig` object is sub-classed from the *Container* object and is used to load and save out presets of full rigs. Provided additional methods for doing so

   .. change:: changed
      :tags: plug-ins, maya

      Maya plug-in now fully supported.

   .. change:: changed
      :tags: plug-ins, softimage

      Softimage plug-in now fully supported.

   .. change:: changed
      :tags: control, config

      :doc:`/python/core/objects/control` object now takes a *shape* argument and shapes are stored in the config.

   .. change:: changed
      :tags: control, config

      :doc:`/python/core/configs/config` object now stores the valid colors, sides, mirror mapping, naming template, and control shapes. This object is a singleton and can be sub-classed to provide customized configurations per studio, per project, or even per asset.

   .. change:: changed
      :tags: object 3d, scene_item

      Swapped names of Object 3D and Scene Item. Scene Item is now the base object for most simple objects without transforms.

   .. change:: changed
      :tags: object 3d, scene_item

      Renamed srt buffer to ctrl space to be more intuitively named.


.. include:: footer.rst
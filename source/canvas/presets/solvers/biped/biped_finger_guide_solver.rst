.. _preset_biped_finger_guide_solver:

Biped Finger Guide Solver
*************************

This solver simply draws planes between each input control and aligns on each of the Y axis. This preset also takes an array of sizes that determins the height of each grid. This allows users to be able to align the guide down the length of each finger and ensure that the alignment is correct in conjunction with the geometry being rigged.


.. function:: BipedFingerGuideSolver(drawDebug, rigScale, controls, planeSizes)

    Draws planes between each control aligned to the Y axis.

    :param drawDebug: Whether to activate debug drawing or not.
    :type drawDebug: Boolean
    :param rigScale: Rig scale value for scaling results of the solver.
    :type rigScale: Scalar[]
    :param controls: Controls used in the guide for aligning each joint in the finger.
    :type controls: Mat44[]
    :param planeSizes: Sizes for each of the planes drawn.
    :type planeSizes: Scalar[]


.. figure:: /images/canvas/solvers/biped/BipedFingerGuideSolver.png
    :align: center
    :width: 600px

    Biped Finger Guide in Maya


.. contents:: Usage Documentation
   :local:


Class Documentation
===================


.. include:: ../../../../footer.rst
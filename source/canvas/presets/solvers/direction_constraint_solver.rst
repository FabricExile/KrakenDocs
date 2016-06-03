.. _preset_direction_constraint_solver:

Direction Constraint Solver
***************************

This solver simply draws planes between each input control and aligns on each of the Y axis. This preset also takes an array of sizes that determins the height of each grid. This allows users to be able to align the guide down the length of each finger and ensure that the alignment is correct in conjunction with the geometry being rigged.


.. function:: DirectionConstraintSolver(drawDebug, rigScale, controls, planeSizes)

    Draws planes between each control aligned to the Y axis.

    :param drawDebug: Whether to activate debug drawing or not.
    :type drawDebug: Boolean
    :param rigScale: Rig scale value for scaling results of the solver.
    :type rigScale: Scalar[]
    :param position: The position from which to aim from / position the object.
    :type position: Mat44
    :param upVector: The transform to align the Y axis to.
    :type upVector: Mat44
    :param atVector: The transform to align the X axis to.
    :type atVector: Mat44


.. figure:: /images/canvas/solvers/DirectionConstraintSolver.png
    :align: center
    :width: 600px

    Biped Finger Guide in Maya


.. contents:: Usage Documentation
   :local:


Class Documentation
===================


.. include:: ../../../footer.rst
.. _kl_biped_foot_pivot_solver:

Biped Foot Pivot Solver
***********************

This solver allows users to control where the front, back, left, and right pivot points of the foot rock and banking occur. Giving users control over these pivot points allows for more dynamic animations and usability of the rig.


.. function:: BipedFootPivotSolver(drawDebug, rigScale, rightSide, footRock, footBank, pivotAll, backPivot, frontPivot, outerPivot, innerPivot)
    :noindex:

    Drives the 4 pivots for the front, back, left, and right side of the foot.

    :param drawDebug: Whether to activate debug drawing or not.
    :type drawDebug: Boolean
    :param rigScale: Rig scale value for scaling results of the solver.
    :type rigScale: Scalar
    :param rightSide: Whether the solver should compute the transforms for being on the right side of the character.
    :type rightSide: Boolean
    :param footRock: Value driving the activation of the foot rock.
    :type footRock: Scalar
    :param footBank: Value driving the activation of the foot banking.
    :type footBank: Scalar
    :param pivotAll: Main foot pivot
    :type pivotAll: Mat44
    :param backPivot: Pivot at the back of the foot.
    :type backPivot: Mat44
    :param frontPivot: Pivot at the fron tof the foot.
    :type frontPivot: Mat44
    :param outerPivot: Pivot on the outer side of the foot.
    :type outerPivot: Mat44
    :param innerPivot: Pivot on the inner side of the foot.
    :type innerPivot: Mat44


.. figure:: /images/canvas/solvers/biped/BipedFootPivotSolver.png
    :align: center
    :width: 600px

    Biped Finger Guide in Maya


.. contents:: Usage Documentation
   :local:


Class Documentation
===================


.. include:: ../../../footer.rst
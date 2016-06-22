.. _preset_biped_foot_solver:

Biped Foot Solver
*****************

This solver usually rides on top of the :ref:`Biped Foot Pivot Solver<preset_biped_foot_pivot_solver>` and drives the ankle and toe bones of the foot. It ensures the ankle and toe keeps their alignment with the foot controls in the rig. It also blends between the IK and FK controls.


.. function:: BipedFootSolver(drawDebug, rigScale, ikBlend, ankleLen, toeLen, legEnd, ankleIK, toeIK, ankleFK, toeFK)

    Drives the ankle and toe bones of a foot between the IK and FK controls.

    :param drawDebug: Whether to activate debug drawing or not.
    :type drawDebug: Boolean
    :param rigScale: Rig scale value for scaling results of the solver.
    :type rigScale: Scalar
    :param ikBlend: Value 0-1 used to blend between IK and FK controls.
    :type ikBlend: Scalar
    :param ankleLen: Length of the ankle bone.
    :type ankleLen: Scalar
    :param toeLen: Length of the toe bone.
    :type toeLen: Scalar
    :param legEnd: Matrix of the end of the leg component.
    :type legEnd: Mat44
    :param ankleIK: Matrix of the Ankle IK control.
    :type ankleIK: Mat44
    :param toeIK: Matrix of the Toe IK control.
    :type toeIK: Mat44
    :param ankleFK: Matrix of the ankle FK control.
    :type ankleFK: Mat44
    :param toeFK: Matrix of the toe FK control.
    :type toeFK: Mat44
    :return: ankle_result
    :return: toe_result
    :rtype: Mat44


.. figure:: /images/canvas/solvers/biped/BipedFootPivotSolver.png
    :align: center
    :width: 600px

    Biped Finger Guide in Maya


.. include:: ../../../../footer.rst
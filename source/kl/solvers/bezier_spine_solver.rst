.. _kl_bezier_spine_solver:

Bezier Spine Solver
*******************

This solver distributes objects along the bezier curve and interpolates the rotation between the base and tip input matrices. Typically used for the spines of bipedal characters.


.. function:: BezierSpineSolver(drawDebug, rigScale, length, base, baseHandle, tipHandle, tip, outputs)

    Distributes objects along the bezier curve and interpolates the rotation between the base and tip input matrices.

    :param drawDebug: Whether to activate debug drawing or not.
    :type drawDebug: Boolean
    :param rigScale: Rig scale value for scaling results of the solver.
    :type rigScale: Scalar
    :param length: Initial length of the spine
    :type length: Scalar
    :param base: Base control matrix.
    :type base: Mat44
    :param baseHandle: Base handle control matrix.
    :type baseHandle: Mat44
    :param tipHandle: Tip handle control matrix.
    :type tipHandle: Mat44
    :param tip: Tip control matrix
    :type tip: Mat44
    :param outputs: Distributed output matrices
    :type outputs: Mat44


.. figure:: /images/kl/solvers/generic/BezierSpineSolver.png
    :align: center
    :width: 600px

    Bezier Spine Component in Maya


.. include:: ../../footer.rst
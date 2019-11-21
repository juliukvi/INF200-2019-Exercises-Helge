# -*- coding: utf-8 -*-

"""
Set of compatibility tests for PA02.
"""

__author__ = 'Helge Helo Klemetsdal, Adam Julius Olof Kviman'
__email__ = 'hegkleme@nmbu.no, juliukvi@nmbu.no'

import chutes_simulation as cs
import pytest
import random


class TestBoard:
    """
    Tests for Board class.
    """

    def test_goal_reached(self):
        """Returns True for position >= 90 and False for position < 90"""
        b = cs.Board()
        output = b.goal_reached(91)
        assert output
        output = b.goal_reached(80)
        assert not output

    def test_position_adjustment(self):
        """Test to check that if position is on a ladder output is positive,
        if position is on a chute output is negative and if position is not on
        a ladder or chute return 0"""
        b = cs.Board()
        output = b.position_adjustment(1)  # 1 is a ladder
        assert output > 0
        output = b.position_adjustment(24)  # 24 is a chute
        assert output < 0
        output = b.position_adjustment(2)  # 2 is not a ladder or chute
        assert output == 0

    def test_position_adjusetment_steps(self):
        """Test to see that the output is the correct amount of steps to adjust
        """
        b = cs.Board()
        output = b.position_adjustment(1)  # ladder goes from 1 to 40
        assert output == 39
        output = b.position_adjustment(24)  # chute goes from 24 to 5
        assert output == -19
        output = b.position_adjustment(2)  # not a ladder or chute
        assert output == 0



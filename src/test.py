# -*- coding: utf-8 -*-
"""
Created on Wed May 10 10:14:43 2023

@author: xiaoyu
"""
import unittest
import model

class TestCode(unittest.TestCase):
    """
    Unit test for model module
    
    """
    def test_weight_and_add(self):
        """
        Test weighted_and_add function in model.py
        The test checks the correctness of weighting process
        by using specific values and comparing them with expected output
        
        Parameters
        ----------
        None

        Returns
        -------
        None.

        """
        gw = 0.5
        tw = 0.2
        pw = 0.3
        
        geology = [[0], [3]]
        transport = [[2], [1]]
        population = [[1], [5]]
        wr = model.weight_and_add(geology, transport, population, gw, tw, pw)
        self.assertEqual(wr, [[0.7], [3.2]])
            
if __name__ == '__main__':
    unittest.main()
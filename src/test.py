# -*- coding: utf-8 -*-
"""
Created on Wed May 10 10:14:43 2023

@author: xiaoyu
"""
import unittest
import model

class TestCode(unittest.TestCase):
    def test_weight_and_add(self):
        gw = 0.3
        tw = 0.4
        pw = 0.3
        
        geology = [[1], [2]]
        transport = [[0], [1]]
        population = [[3], [0]]
        wr = model.weight_and_add(geology, transport, population, gw, tw, pw)
        self.assertEqual(wr, [[1.2], [1.0]])
            
if __name__ == '__main__':
    unittest.main()
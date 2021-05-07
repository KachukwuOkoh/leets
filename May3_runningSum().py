# -*- coding: utf-8 -*-
"""
Created on Tue May  4 06:26:45 2021

@author: Oluchukwu Okoh
"""

class Solution(object):
    def runningSum(nums):
        return [sum(nums[:i+1]) for i in range(len(nums))]
    


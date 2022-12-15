#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 13:32:54 2022

@author: julianhayduk
"""
import numpy as np
import sympy as sn

from sympy import *
u, i, uu, ui = symbols("u,i,uu,ui")
r = u / i
ur = sqrt((diff(r, u) * uu)**2 + (diff(r, i) * ui)**2)
ur.subs([(u, 238.46), (uu, 7.34), (i, 0.9239), (ui, 0.0081)])
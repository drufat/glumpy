#! /usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2014, Nicolas P. Rougier
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
import numpy as np
from glumpy import app
from glumpy.graphics.collections import PointCollection
from glumpy.transforms import LogScale, PolarProjection, Position2D, Viewport


window = app.Window(1024,1024, color=(1,1,1,1))

@window.event
def on_draw(dt):
    window.clear()
    points.draw()

x_transform = LogScale("position.x", domain=(-1,2), range=(0,1))
transform = Position2D(PolarProjection(x_transform, "position.y")) + Viewport()
points = PointCollection("agg", transform = transform)

n = 10000
R = np.random.uniform(0,100,n)
T = np.random.uniform(0,2*np.pi,n)
Z = np.zeros(n)

points.append (np.dstack((R,T,Z)).reshape(n,3) )
app.run()

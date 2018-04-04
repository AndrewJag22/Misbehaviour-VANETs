#!/usr/bin/env python
"""
@file    runner.py
@author  Lena Kalleske
@author  Daniel Krajzewicz
@author  Michael Behrisch
@date    2009-03-26
@version $Id: runner.py 14678 2013-09-11 08:53:06Z behrisch $

Route generation script.

SUMO, Simulation of Urban MObility; see http://sumo.sourceforge.net/
Copyright (C) 2009-2012 DLR/TS, Germany

This file is part of SUMO.
SUMO is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.
"""

import os, sys
import optparse
import subprocess
import random

def generate_routefile():
    random.seed(445) # make tests reproducible
    N = 3600 # number of time steps
    # demand per second from different directions
    p214 = 1./8 		#right-down road
    p215 = 2./8			#Left-left road
    p314 = 3./8			#Down-low road
    p315 = 4./8			#Down-right road
    p412 = 5./8			#Down-down road
    p413 = 6./8
    p512 = 7./8
    p513 = 8./8
    with open("cross.rou.xml", "w") as routes:
        print >> routes, """<routes>
        <vType id="typePassenger" accel="0.8" decel="4.5" sigma="0.5" length="5" minGap="2.5" maxSpeed="16.67" guiShape="passenger"/>
        <vType id="typeBus" accel="0.8" decel="4.5"
        color="1,0,0" sigma="0.5" length="5" minGap="3" maxSpeed="25" guiShape="emergency"/>

        <route id="2-1-4" edges="2i 1i 4o" />
        <route id="2-1-5" edges="2i 1i 5o" />
        <route id="3-1-4"  edges="3i 1i 4o" />
        <route id="3-1-5"  edges="3i 1i 5o" />
        <route id="4-1-2" edges="4i 1o 2o" />
        <route id="4-1-3" edges="4i 1o 3o" />
        <route id="5-1-2" edges="5i 1o 2o" />
        <route id="5-1-3" edges="5i 1o 3o" />"""
        lastVeh = 0
        vehNr = 0
        for i in range(N):
            temp = random.uniform(0,1)
            if temp < p214:
                print >> routes, '    <vehicle id="%i" type="typeBus" route="2-1-4" depart="%i" />' % (vehNr, i)
                vehNr += 1
                lastVeh = i
            elif temp < p215:
                print >> routes, '    <vehicle id="%i" type="typePassenger" route="2-1-5" depart="%i" />' % (vehNr, i)
                vehNr += 1
                lastVeh = i
            elif temp < p314:
                print >> routes, '    <vehicle id="%i" type="typePassenger" route="3-1-4" depart="%i" />' % (vehNr, i)
                vehNr += 1
                lastVeh = i
            elif temp < p315:
                print >> routes, '    <vehicle id="%i" type="typePassenger" route="3-1-5" depart="%i" />' % (vehNr, i)
                vehNr += 1
                lastVeh = i
            elif temp < p412:
                print >> routes, '    <vehicle id="%i" type="typePassenger" route="4-1-2" depart="%i" />' % (vehNr, i)
                vehNr += 1
                lastVeh = i
            elif temp < p413:
                print >> routes, '    <vehicle id="%i" type="typePassenger" route="4-1-3" depart="%i" />' % (vehNr, i)
                vehNr += 1
                lastVeh = i
            elif temp < p512:
                print >> routes, '    <vehicle id="%i" type="typePassenger" route="5-1-2" depart="%i" />' % (vehNr, i)
                vehNr += 1
                lastVeh = i
            elif temp <= p513:
                print >> routes, '    <vehicle id="%i" type="typeBus" route="5-1-3" depart="%i" />' % (vehNr, i)
                vehNr += 1
                lastVeh = i
            print ("pDD: %f, pDR: %f") %(p215, p314)
            print ("random.uniform(0,1): %f") %(random.uniform(0,1))
        print >> routes, "</routes>"

# this is the main entry point of this script
if __name__ == "__main__":
    
    generate_routefile()

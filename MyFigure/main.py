import gmsh
import os
import sys
import math

gmsh.initialize()

path = os.path.dirname("C:/Users/Denchik/Downloads/")
gmsh.merge(os.path.join(path, "low_poly_elephant.stl"))

angle = 2
forceParametrizablePatches = False
includeBoundary = True
curveAngle = 180

gmsh.model.mesh.classifySurfaces(angle * math.pi / 180., includeBoundary,
                                 forceParametrizablePatches,
                                 curveAngle * math.pi / 180.)

gmsh.model.mesh.createGeometry()

s = gmsh.model.getEntities(2)
l = gmsh.model.geo.addSurfaceLoop([s[i][1] for i in range(len(s))])
gmsh.model.geo.addVolume([l])

gmsh.model.geo.synchronize()


gmsh.model.mesh.generate(3)
gmsh.write('elephant.stl')

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()

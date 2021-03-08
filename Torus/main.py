import gmsh
import sys
import math

gmsh.initialize()
lc = 0.15

def circle(r = 2.0, n = 1):
    cenPoint = gmsh.model.geo.addPoint(0., 0., 0., lc)
    p1 = gmsh.model.geo.addPoint(r, 0., 0., lc)
    p2 = gmsh.model.geo.addPoint(0., -r, 0., lc)
    p3 = gmsh.model.geo.addPoint(-r, 0., 0., lc)
    p4 = gmsh.model.geo.addPoint(0., r, 0., lc)
    ca1 = gmsh.model.geo.addCircleArc(p1, cenPoint, p2)
    ca2 = gmsh.model.geo.addCircleArc(p2, cenPoint, p3)
    ca3 = gmsh.model.geo.addCircleArc(p3, cenPoint, p4)
    ca4 = gmsh.model.geo.addCircleArc(p4, cenPoint, p1)
    gmsh.model.geo.addCurveLoop([ca1, ca2, ca3, ca4], n)
    gmsh.model.geo.synchronize()

circle(1.8, 1)
circle(1.4, 2)

gmsh.model.geo.addPlaneSurface([1, -2], 3)
v1 = gmsh.model.geo.revolve([(2, 3)], 3.0, 0.0, 0.0, 0.0, 1.0, 0.0, math.pi/2)
v2 = gmsh.model.geo.copy([(3, v1[1][1])])
gmsh.model.geo.rotate([(3, v2[0][1])], 3.0, 0.0, 0.0, 0.0, 1.0, 0.0, -math.pi/2)
v3 = gmsh.model.geo.copy([(3, v2[0][1])])
gmsh.model.geo.rotate([(3, v3[0][1])], 3.0, 0.0, 0.0, 0.0, 1.0, 0.0, -math.pi/2)
v4 = gmsh.model.geo.copy([(3, v3[0][1])])
gmsh.model.geo.rotate([(3, v4[0][1])], 3.0, 0.0, 0.0, 0.0, 1.0, 0.0, -math.pi/2)



gmsh.model.geo.synchronize()

gmsh.model.mesh.generate(3)

gmsh.write("torus.stl")

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

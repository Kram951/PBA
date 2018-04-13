import sys
sys.path.append('../src')
import pba
import math
import time

def buildAnt():
    w = pba.Robot_Module()

    # Main body
    w.addBody("torso","0 0 2")
    w.addGeom("torso_geom","0 0 0","0.25","sphere")
 
    # Front left leg
    w.addBody("front_left_leg","0 0 0","torso")
    w.addGeom("aux_1_geom","0.0 0.0 0.0 0.2 0.2 0","0.08","capsule")
    w.addBody("aux_1","0.2 0.2 0")
    w.addJoint("hip_1","0 0 0","0 0 1","-30 30","150")
    w.addGeom("left_leg_geom","0 0 0 0.2 0.2 0","0.08","capsule")
    w.addBody("shit1","0.2 0.2 0")
    w.addJoint("ankle_1","0 0 0","-1 1 0","30 70","150")
    w.addGeom("left_ankle_geom","0 0 0 0.4 0.4 0","0.08","capsule")
    # Front right leg
    w.addBody("front_right_leg","0 0 0","torso")
    w.addGeom("aux_2_geom","0.0 0.0 0.0 -0.2 0.2 0","0.08","capsule")
    w.addBody("aux_2","-0.2 0.2 0")
    w.addJoint("hip_2","0 0 0","0 0 1","-30 30","150")
    w.addGeom("right_leg_geom","0 0 0 -0.2 0.2 0","0.08","capsule")
    w.addBody("shit2","-0.2 0.2 0")
    w.addJoint("ankle_2","0 0 0","1 1 0","-70 -30","150")
    w.addGeom("right_ankle_geom","0 0 0 -0.4 0.4 0","0.08","capsule")
    # Left back leg
    w.addBody("back_leg","0 0 0","torso")
    w.addGeom("aux_3_geom","0.0 0.0 0.0 -0.2 -0.2 0","0.08","capsule")
    w.addBody("aux_3","-0.2 -0.2 0")
    w.addJoint("hip_3","0 0 0","0 0 1","-30 30","150")
    w.addGeom("back_leg_geom","0 0 0 -0.2 -0.2 0","0.08","capsule")
    w.addBody("shit3","-0.2 -0.2 0")
    w.addJoint("ankle_3","0 0 0","-1 1 0","-70 -30","150")
    w.addGeom("third_ankle_geom","0 0 0 -0.4 -0.4 0","0.08","capsule")
    # Right back leg
    w.addBody("right_back_leg","0 0 0","torso")
    w.addGeom("aux_4_geom","0.0 0.0 0.0 0.2 -0.2 0","0.08","capsule")
    w.addBody("aux_4","0.2 -0.2 0")
    w.addJoint("hip_4","0 0 0","0 0 1","-30 30","150")
    w.addGeom("right_back_leg_geom","0 0 0 0.2 -0.2 0","0.08","capsule")
    w.addBody("shit4","0.2 -0.2 0")
    w.addJoint("ankle_4","0 0 0","1 1 0","30 70","150")
    w.addGeom("fourth_ankle_geom","0 0 0 0.4 -0.4 0","0.08","capsule")

    return w
def moveAnt(w):
    w.startRun('our_ant')

    angular_velocity = 0.1
    place = math.pi / 4

    for i in range(100):
        w.makeStep()
    time.sleep(2)

    #Stand up
    for j in range(5):
        if j == 0: continue
        for i in range(1):
            if i == 1:
                print(str(j))
            angle = 50
            if j == 2 or j == 3:
                angle = -angle
            w.moveJoint("ankle_" + str(j), angle, 0 * angular_velocity)
            for _ in range(10):
                w.makeStep()   
                        
    print ("Try move")
    for j in [1, 4, 2, 3]:
        if j == 0: continue
        for i in range(100):
            if i == 1:
                print(str(j))
            angle = 30
            if j == 2 or j == 3:
                angle = -70
            w.moveJoint("ankle_" + str(j), angle, angular_velocity)
            w.makeStep()
        time.sleep(1)
    time.sleep(2)

    for i in range(100):
        if i == 1:
            print("2")
        w.moveJoint("ankle_3", place, angular_velocity)
        w.makeStep()
        w.moveJoint("ankle_4", place, angular_velocity)
        w.makeStep()
    
    for i in range(100):
        if i == 1:
            print("3")
        w.makeStep()
   
    for i in range(100):
        if i == 1:
            print("4")
        w.moveJoint("ankle_3", -place*2, angular_velocity)
        w.moveJoint("ankle_4", -place*2, angular_velocity)
        w.moveJoint("ankle_1", place*1.5, angular_velocity)
        w.moveJoint("ankle_2", place*1.5, angular_velocity)
        w.makeStep()

    while 1:
        w.makeStep()
    
    w.stopRun()
if __name__=="__main__":
    moveAnt(buildAnt())
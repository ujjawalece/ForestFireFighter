import matplotlib.pyplot as plt
import numpy as np
import pybullet as p
import time
import pybullet_data
import cv2
import os
import time
import math

file_path = os.getcwd()
file_name1 = "/foresturdf.urdf"
file_name2 = "/fireurdf.urdf"
file_name3 = "/water droplet  urdf.urdf"#blue colour cube which act as water droplet or fire extinguisher
file_name4 = "/quadrotorurdf.urdf"
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
fz=100
p.setGravity(0,0,-fz)

p.loadURDF(os.path.join(pybullet_data.getDataPath(), "plane.urdf"), 0, 0, 0)

p.loadURDF(file_path + file_name1, [0, 0, 0], cubeStartOrientation)#urdf of a green plate which shows a forest

p.loadURDF(file_path + file_name2, [0, 5, 0], cubeStartOrientation)#urdf of circular orange plate 1 which symbolises fire
p.loadURDF(file_path + file_name2, [5, 0, 0], cubeStartOrientation)#urdf of circular orange plate 2 which symbolises fire
p.loadURDF(file_path + file_name2, [0, 0, 0], cubeStartOrientation)#urdf of circular orange plate 3 which symbolises fire
p.loadURDF(file_path + file_name2, [-3,-4, 0], cubeStartOrientation)#urdf of circular orange plate 4 which symbolises fire
p.loadURDF(file_path + file_name2, [2, 3, 0], cubeStartOrientation)#urdf of circular orange plate 5 which symbolises fire

drone=p.loadURDF(file_path + file_name4, [5, 0, 2.2], cubeStartOrientation)#a drone which wil extinguish fire

width = 512
height = 512
fov = 60
aspect = width / height
near = 0.02
far = 30
projection_matrix = p.computeProjectionMatrixFOV(fov, aspect, near, far)
i=0
k=0
while(True):
	p.stepSimulation()
	view_matrix = p.computeViewMatrix([0, 0, 9],[0,0,0], [0, 1, 0])
	images = p.getCameraImage(width,height,view_matrix,projection_matrix,[0,0,-1],[1,1,1],9,0,renderer=p.ER_BULLET_HARDWARE_OPENGL)

	""" opencv code"""
	l = np.array([0, 80, 100])
	u = np.array([5, 165, 255])
	rgb_image = np.reshape(images[2], (height, width, 4))
	img_float32 = np.float32(rgb_image)
	bgr = cv2.cvtColor(img_float32, cv2.COLOR_RGB2BGR)
	mr1 = cv2.inRange(bgr, l, u)
	contours, hierarchy = cv2.findContours(mr1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cX = 0
	cY = 0
	for c in contours:
		area = cv2.contourArea(c)
		if(area>1000):
			print(area)
			M = cv2.moments(c)
			cX = int(M["m10"] / (M["m00"] + 0.01))
			cY = int(M["m01"] / (M["m00"] + 0.01))
			cv2.putText(bgr, ".", (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 2)
	cv2.imshow("pic", bgr)
	#cv2.imshow("pic", mr1)
	#cv2.imwrite("fd", images)
	cv2.waitKey(1)
	cv2.destroyAllWindows
	cX=cX/51.2-5
	cY = 5 - cY / 51.2
	dronePos, orn = p.getBasePositionAndOrientation(drone)
	fx = cX - dronePos[0]
	fy = cY - dronePos[1]
	dist = math.sqrt((cX - dronePos[0]) ** 2 + (cY - dronePos[1]) ** 2)
	print(dist)
	if(dist<0.1):
		p.resetBaseVelocity(drone,[0,0,0])
		i=200
		while (i):
			p.applyExternalForce(drone, -1, [0, 0, 10 * fz], [dronePos[0], dronePos[1], dronePos[2]],p.WORLD_FRAME)
			if (i % 5 == 0):
				water = p.loadURDF(file_path + file_name3, [dronePos[0], dronePos[1], dronePos[2]-0.2],cubeStartOrientation)
				p.stepSimulation()
			elif (i % 4 == 0):
				water = p.loadURDF(file_path + file_name3, [dronePos[0]+0.2, dronePos[1], dronePos[2]-0.2],cubeStartOrientation)
				p.stepSimulation()
			elif (i % 3 == 0):
				water = p.loadURDF(file_path + file_name3, [dronePos[0]-0.2, dronePos[1], dronePos[2] - 0.2],cubeStartOrientation)
				p.stepSimulation()
			elif (i % 2 == 0):
				water = p.loadURDF(file_path + file_name3, [dronePos[0], dronePos[1]+0.2, dronePos[2] - 0.2],cubeStartOrientation)
				p.stepSimulation()
			else:
				water = p.loadURDF(file_path + file_name3, [dronePos[0], dronePos[1]-0.2, dronePos[2] - 0.2],cubeStartOrientation)
				p.stepSimulation()
			i = i - 1
	elif(dist<1):
		p.resetBaseVelocity(drone, [10*fx, 10*fy, 0])
	else:
		p.applyExternalForce(drone, -1, [50*fx, 50*fy, 10*fz], [dronePos[0], dronePos[1], dronePos[2]], p.WORLD_FRAME)
	time.sleep(1. / 240.)
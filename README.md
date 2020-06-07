# ForestFireFighter(FFF)
## Abstract:
![forest fire image](https://github.com/ujjawalece/ForestFireFighter/blob/master/forestfireimg.jpeg)

Fire incident is a disaster that can potentially cause the loss of life, property damage and permanent disability to the affected victim. Fire fighters are primarily tasked to handle fire incidents, but they are often exposed to higher risks when extinguishing fire, especially in hazardous environments such as in nuclear power plant, petroleum refineries, gas tanks and especially in **Forests**. The main reason why forest fire are so dangerous is that in ther initial state these fire are very hard to find as they originate in forest where noone is to monitor them. these fire cause a lot of damage to naturl resources, wildlife and also human life when they become out of control. Like recently we see in Australia. Technological innovations can be utilized to assist firefighting in these areas. Therefore, in this project we presents the development of a firefighting robot which will detect the forest fire at its very initial state and will automatically extinguish it.


## Problem description:

In most of the forest fire the fire emerges somewhere inside a dense forest and we are unaware about the fire, And when we come to know it is very late as fire had spread very much and it become very difficult to control it.
**So, basically our aim is to make such a fire extinguishing system which can detect the fire at very early stage and then we can extinguish it.**
For this we have to make a system which will monitor a whole forest 24*7 and when any unfortunate thing happens, it will alert us.
We should also have some system which will automatically extinguish fire as it might happen that human fire fighters are unable to reach at that spot in time due to some circumstances.


## Approach:



As stated above we have to monitor the whole forest 24*7. So, the best way to do this is to use **cameras**. And when it comes to detect something from images the firt thing which come in our mind is **openCV**.

![camera](https://github.com/ujjawalece/ForestFireFighter/blob/master/WhatsApp%20Image%202020-06-05%20at%209.49.34%20AM.jpeg)


Basicallly we have to set cameras at different positions in forest(normally at high altitudes to get a bettrer view) in such a way that it cover whole forest. A single camera will cover some particular area of forest and in this way by using multiple cameras we can cover whole forest.

![forest camera](https://github.com/ujjawalece/ForestFireFighter/blob/master/WhatsApp%20Image%202020-06-05%20at%209.49.15%20AM.jpeg)

Then the images sent by the cameras willl be processed and searched for any fire in it by using opencv. And if fire is detected then a alarm is activated and a fully automatic robot which can extinguish fire will be sent at the spot. Again we will use opencv and image processing to navigate our robot to the spot. In this way our automatic system works.

## Key Concepts used:

### Detecting Fire-

* Firstly we have to detect fire. So, for detecting fire we will take input from camera and process that image. In our project we have placed the camera at a high place and we are getting top view of our forest. Fire contour will we something like below shown in photo.

![fire contour](https://github.com/ujjawalece/ForestFireFighter/blob/master/Fire%20Contour%20Image.jpeg)

* **Note-** In our simulation we have used orange colour plate to demonstrate fire and and green colour shows forest.

![firecontour](https://github.com/ujjawalece/ForestFireFighter/blob/master/Fire%20Contour%20Image.jpeg)

* After getting the contour we will find it location.

### Extinguishing Fire-

* For extinguishing fire we are uing a drone which which will automatically go to the fire spot and will extinguish it.

![drone](https://github.com/ujjawalece/ForestFireFighter/blob/master/drone.jpeg)

* We already have the cordinates of firespot(s) now we want to navigate our drone to that spot. For navigating drone we should know the cordinates of drne also hich can we easily done by using GPS devices. Once we have cordinates of both drone and fire spot our drone can navigate to the required spot.

**Note-** For our simulating purpose we have find a vector which is pointig toward firespot from drone postion. And then have we applied a force in that direction until our drone reached above fire spot. But in real life some different concepts of aerodynamic is used to fly a drone and it is not a hard job to do that.

* Once our drone reached the fire spot it will **switch on its fire extinguishing system**(it will throw water or some fire extinguishing substances on fire spot).

* After extinguishing fire from that spot it will navigate to the other fire spot(if present) by using the same way as stated above.

#### Above whole process is shown below with the help of a flowchart-

![flowchart](https://github.com/ujjawalece/ForestFireFighter/blob/master/Flow%20chart.png)

* You can see whole **python code** of our project [here](https://github.com/ujjawalece/ForestFireFighter/blob/master/ForestFireFighter.py).
* Some video of our project simulation are attached below-
* [**Video_1**](https://drive.google.com/file/d/1OpFGvZW1gKkTU-g1vixThIy_qL_uqXqy/view?usp=sharing)
* [**Video_2**(quick view)](https://drive.google.com/file/d/1VcxgkeSNZKo-gBvwXggBNgG123JWE7tn/view?usp=sharing)


## Conclusion:

This project can we broadly divided into two parts, first one is detecting fire and second one is an automatic system which will extinguish it.
For detecting fire we use opencv, which is a very good approach, but yet there are some limitations in this as we use are using cameras so sometimes like in foggy climate the range of camera can we reduce to very little diatance. Hence we should use fog resistance cameras.
For extinguishing fire in our simulation we have used a drone to extinguish fire but the capacity of drone to carry fire extinguishing substance are less. So they can we less effective in controlling the spreading fire which can cause a great trouble. So, we should focus on such system which is more effective in extinguishing fire like a fire extinguishing helicopter which is being used by humans to control forest fire. But, our aim is to make an automatic version of something like this, which is really a challenging task.
Yet, our system is quite efficient for small fire or fire at begning. 

## References:

* https://www.youtube.com/watch?v=h8-XLlTnAtY
* https://www.researchgate.net/publication/330827730_Development_of_Fire_Fighting_Robot_QRob
* https://www.geeksforgeeks.org/find-and-draw-contours-using-opencv-python/
* http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_table_of_contents_contours/py_table_of_contents_contours.html



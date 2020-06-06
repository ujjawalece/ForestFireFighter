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


## Conclusion:

This project can we broadly divided into two parts, first one is detecting fire and second one is an automatic system which will extinguish it.
For detecting fire we use opencv, which is a very good approach, but yet there are some limitations in this as we use are using cameras 



## References:

* https://www.youtube.com/watch?v=h8-XLlTnAtY
* https://www.researchgate.net/publication/330827730_Development_of_Fire_Fighting_Robot_QRob
* https://www.geeksforgeeks.org/find-and-draw-contours-using-opencv-python/
* http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_table_of_contents_contours/py_table_of_contents_contours.html



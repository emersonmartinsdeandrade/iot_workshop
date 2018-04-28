# -*- coding: utf-8 -*-
"""
Created on Sun Apr 08 12:46:06 2018

@author: USER
"""

import matplotlib.pyplot as plt

plt.plot([1,2,3,4], [1,2,3,4])

plt.xlabel("Time")
plt.ylabel("Variable")
plt.title("Iot Workshop")
plt.savefig("Hello.png")


import matplotlib.pyplot as plt
sizes = [10, 20, 15]
colors = ['red', 'yellow', 'lightskyblue']
explode = (0,0.05,0)
patches, texts = plt.pie(sizes, colors=colors, startangle=90, explode=explode, autopct='%.0f%%', shadow=True)
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
plt.tight_layout()
plt.savefig("pie.png")
plt.show()
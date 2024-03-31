# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 18:30:01 2024

@author: Mapmaking Team PyCamp Spain 2024
"""

if __name__ == '__main__':
    image_names = [
        [
            'a-a-a-a.jpg',
            'a-a-a-a-ballena.jpg',
            'a-a-a-a-barco.jpg',
        ],
        [
            'a-t-a-t-canal.jpg',
            'a-t-a-t-istmo.JPG',
            't-a-a-a.jpg',
        ],
        [
            't-t-a-a.jpg',
            't-t-t-a.jpg',
            't-t-t-t.jpg',
        ],
    ]

    generate_final_image(image_names, 3, 3)
# recipes-etl
HelloFresh Python assessment by Jelle Stoffels

Run the .py file with the recipes.json file in the same directory

This Python file takes a .json file called 'recipes.json', saved in the same directory and writes a csv-file including all recipes with chilies in it and adds a difficulty column to these recipes.

dependecies:

Python 3

import pandas as pd
import numpy as np
import datetime
import os
import re



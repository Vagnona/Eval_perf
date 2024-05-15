#!/bin/bash

awk '{if($1 == "r" && $5 == 0) print $1 " " $3 " " $5 " " $11}' alltrace.tr > usefull_data/data_0.tr
awk '{if($1 == "r" && $5 == 1) print $1 " " $3 " " $5 " " $11}' alltrace.tr > usefull_data/data_1.tr
awk '{if($1 == "r" && $5 == 2) print $1 " " $3 " " $5 " " $11}' alltrace.tr > usefull_data/data_2.tr
awk '{if($1 == "r" && $5 == 3) print $1 " " $3 " " $5 " " $11}' alltrace.tr > usefull_data/data_3.tr
awk '{if($1 == "r" && $5 == 4) print $1 " " $3 " " $5 " " $11}' alltrace.tr > usefull_data/data_4.tr
awk '{if($1 == "r" && $5 == 5) print $1 " " $3 " " $5 " " $11}' alltrace.tr > usefull_data/data_5.tr
awk '{if($1 == "r" && $5 == 6) print $1 " " $3 " " $5 " " $11}' alltrace.tr > usefull_data/data_6.tr
awk '{if($1 == "r" && $5 == 7) print $1 " " $3 " " $5 " " $11}' alltrace.tr > usefull_data/data_7.tr

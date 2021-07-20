#!/bin/bash


#Top 3 usuarios que mas tiempo han estado conectados
ac -p | sort -n -k2 -r | tail +2 | tail -3 > est1.stats

#Top 5 comandos mas veces llamados
sa -nac | head -6 | tail +2 > est2.stats

#Top 5 comandos que mas tiempo de cpu han consumido
sa -ac | head -6 | tail +2 > est3.stats



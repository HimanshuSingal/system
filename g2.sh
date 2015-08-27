out='g2.png'
gnuplot << PLOTTHIS
set term postscript eps enhanced color  "Helvetica" 32
set style histogram columnstacked

set terminal png
set output "${out}"
set autoscale
unset log                              
unset label
set grid 
set title "Histogram Frequency"
set key right top

set ylabel "Frequency (%)"
set xlabel "Score (%)"
#set format x "10^{%L}"

##########################
#set xrange [9100:9500]
#set yrange [0:0.8]
#########################


#set xrange [0.2:3]
set yrange [0:0.001]

#set xtics (0.2,0.25,0.5,0.75,1)

##############################################################

plot "hist_G.txt" using 1:2 title 'GENUINE' ,\
      "hist_I.txt" using 1:2 title 'IMPOSTER'



##############################################################

##############################################################
pause mouse
PLOTTHIS



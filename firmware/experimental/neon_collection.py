# SPDX-License-Identifier: GPL-3.0-only
# Experimental Neon Collection recipes for FMini-1 Bank.add API.
# Does not modify the original factory bank or allocate firmware slots.
def add_neon(b, o, osc_off, co):
    b.add("MINI MOOG LD","lead",(o("8","SAW",88),o("8","SAW",84,11),o("16","SQR",55)),cutoff=950,emph=3.8,cntr=co(1.8),fenv=(0,350,65),env=(4,350,112,200),glide=85,vib=28,mosc=True,send=(18,0,48,36),level_trim=-14,pat=4)
    b.add("CRYSTAL SINE","lead",(o("8","SIN",105),o("4","SIN",25),osc_off()),cutoff=2200,emph=0,env=(12,500,115,350),glide=100,vib=22,mosc=True,send=(0,0,45,55),level_trim=-14,pat=4)
    b.add("WORSHIP LEAD","lead",(o("8","TRI",95),o("8","SAW",48,11),o("16","SIN",35)),cutoff=1250,emph=2.5,env=(15,450,115,450),glide=95,vib=25,mosc=True,send=(0,25,65,65),dl=("P-PONG",375,42),level_trim=-14,pat=4)
    b.add("NOVA LEAD","lead",(o("8","SAW",85),o("8","PW",75,22),o("4","SAW",45,-22)),cutoff=1800,emph=3,cntr=co(1.2),env=(5,300,110,250),glide=65,vib=24,mosc=True,send=(15,45,50,40),level_trim=-14,pat=4)
    b.add("NEON SAW","lead",(o("8","SAW",85),o("8","SAW",80,-22),o("4","SAW",45,22)),cutoff=2400,emph=2,env=(5,300,110,220),send=(10,55,40,40),level_trim=-14,pat=4)
    b.add("ANALOG FAT","lead",(o("16","SAW",90),o("8","SAW",85,11),o("8","SQR",65,-11)),cutoff=700,emph=3.5,cntr=co(2),env=(5,400,110,220),glide=70,send=(25,0,35,25),level_trim=-14,pat=4)
    b.add("HEAVEN SYNTH","atmo",(o("8","SIN",85),o("4","TRI",65,11),o("8","SAW",35,-11)),cutoff=1600,emph=1.5,env=(450,900,110,1800),poly=True,send=(0,65,40,85),rv=("CLOUD",90,75),level_trim=-14,pat=5)
    b.add("MOTION SYNTH","pad",(o("8","PW",75),o("8","SAW",70,22),o("16","TRI",45)),cutoff=1100,emph=3,vib=35,mflt=True,lfo=(0.3,"SIN",0,"OFF"),env=(200,800,105,900),poly=True,send=(0,55,55,60),level_trim=-14,pat=5)
    b.add("DREAM PAD","pad",(o("8","SAW",70),o("8","TRI",80,22),o("4","SIN",40,-22)),cutoff=1000,emph=1.5,env=(650,1000,110,1800),poly=True,send=(0,70,30,80),rv=("HALL",95,75),level_trim=-14,pat=5)
    b.add("DEEP MOOG BS","bass",(o("16","SAW",95),o("16","SQR",70,11),o("32","SIN",80)),cutoff=220,emph=3,cntr=co(1.8),fenv=(0,280,45),env=(3,300,110,120),send=(15,0,0,5),level_trim=-14,pat=2)

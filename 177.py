
print("************************")
print("*   momo的商城   *")
print("日期，服装名称，单价，库存数量，日销售量")
print("1号	   羽绒服	253.6	500	10")
print("2号	   牛仔裤	86.3	600	60")
print("3号	     风衣	96.8	335	43")
print("4号	     皮草  	135.9	855	63")
print("5号	     T血	 65.8	632	63")
print("6号	     衬衫	 49.3	562	120")
print("7号	   牛仔裤	86.3	600	72")
print("8号	   羽绒服	253.6	500	69")
print("9号	   牛仔裤	86.3	600	35")
print("10号	    羽绒服	253.6	500	140")
print("11号	    牛仔裤	86.3	600	90")
print("12号	    皮草 	135.9	855	24")
print("13号	    T血	    65.8	632	45")
print("14号	    风衣	    96.8	335	25")
print("15号	    牛仔裤	86.3	600	60")
print("16号	    T血	    65.8	632	129")
print("17号	    羽绒服	253.6	500	10")
print("18号	    风衣	    96.8	335	43")
print("19号	    T血	    65.8	632	63")
print("20号	    牛仔裤	86.3	600	60")
print("21号	    皮草	   135.9	855	63")
print("22号	    风衣	    96.8	335	60")
print("23号	    T血	    65.8	632	58")
print("24号	    牛仔裤	86.3	600	140")
print("25号	    T血	    65.8	632	48")
print("26号	    风衣	    96.8	335	43")
print("27号	    皮草	   135.9	855	57")
print("28号	    羽绒服	253.6	500	10")
print("29号	    T血	    65.8	632	63")
print("30号	    风衣  	96.8	335	78")
sum=(253.6*(10+69+140+10+10)+65.8*(63+45+129+63+58+48+63)+49.3*120+96.8*(43+25+43+60+43+78)+86.3*(60+72
+35+90+60+60+140)+135.9*(63+24+63+57))
a=(10+60+43+63+63+120+72+69+35+140+90+24+45+25+60+129+10+43+63+60+63+60+58+140+48+43+57+10+63+78)/30
print(type(sum))
print("您的商城内总销售额为：",sum)
print("您的商城平均日销售数量为：",float(a) )

b=(63+45+129+63+58+48+63)/1844*100
c=(120)/1844*100
d=(43+25+43+60+43+78)/1844*100
e=(60+72+35+90+60+60+140)/1844*100
f=(63+24+63+57)/1844*100
g=(10+69+140+10+10)/1844*100
print("您每个种类月销售量占比为：",
     "\nT血：%d%%"%(b),
     "\n衬衫：%d%%"%(c),
     "\n风衣：%d%%"%(d),
     "\n牛仔裤：%d%%"%(e),
     "\n皮草：%d%%"%(f),
     "\n羽绒服：%d%%"%(g))

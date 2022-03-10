#####
# Author: Kan Zheng
# Date Begun: 14 December 2020
# Date Completed: Date finished (eg day of upload)
# Task: Assignment Stock Data
####
def showVolumeChart(sizeOption):
  pic=makeEmptyPic(sizeOption)
  #Function readCsv stores the return value in the list
  List=readCsv()
  #The function getDate stores the date value in the datelist
  dateList=getDate(List)
  #The function getVolume(List) stores the Volume in the Volumelist
  volumeList=getVolume(List)
  #The function getMax gets the maximum value in this Volume 
  maxNum=getMax(volumeList)
  #The function getMin gets the minimum value in this Volume
  minNum=getMin(volumeList)
  #set the start postion of chart
  sx=int(getWidth(pic)*0.1)
  sy=int(getHeight(pic)*0.1)
  ex=int(getWidth(pic)*0.9)
  ey=int(getHeight(pic)*0.9)
  #get width and height of the chart
  y=ey-sy
  x=ex-sx
  #Draw axes
  addLine(pic,sx,ey,ex,ey)
  text1='Volume'
  #Add the text volume of the ordinate
  addText(pic,1,getHeight(pic)/2-10,text1)
  grey=makeColor(144,144,144)
  #Draw the line of abscissa by loop
  for n in range(0,10):
    newy=int(y*n/10+sy)
    addLine(pic,sx,newy,ex,newy,grey) 
    #Write the scale value of the ordinate through the loop
  for n in range(0,11):
    newy=int(ey-y*n/10)
    volumeString=str(maxNum*n/10+0.00)
    addText(pic,sx-30,newy,volumeString)
    #Start drawing a histogram by looping
  for n in range(0,10):
    newx=int(x*n/10+sx)
    dateString=dateList[n]
    #Circularly type the date of abscissa
    addText(pic,newx+20,ey+20,dateString)
    volumeValue=float(volumeList[n])
    #Calculate the difference between the scale values
    volumeRate=(ey-sy)/maxNum 
    volumeHeight=volumeRate*volumeValue
    #Draw the highest value of red and the lowest value of green and other values of blue by if judgment
    if maxNum==volumeValue:
      addRectFilled(pic,newx+20,ey-int(volumeHeight),30,int(volumeHeight),red)
    elif minNum==volumeValue:
      addRectFilled(pic,newx+20,ey-int(volumeHeight),30,int(volumeHeight),green)
    else:
      addRectFilled(pic,newx+20,ey-int(volumeHeight),30,int(volumeHeight),blue)
  show(pic)
  ##################################################
  #This function is used to draw CandlestickChart
def drawCandlestickChart(inputDataFile,outputImageName,sizeOption): 
  pic=makeEmptyPic(sizeOption)
  #Read the file path by calling the function readCSV
  List=readCSV(inputDataFile)
  dateList=getDate(List)
  #Store openPrice in the new list by calling the function get_openPrice
  openPrice=get_openPrice(List)
  #Store closePrice in the new list by calling the function get_closePrice
  closePrice=get_closePrice(List)
  #Store highPrice in the new list by calling the function get_highPrice
  highPrice=get_highPrice(List)
  #Store lowPrice in the new list by calling the function get_lowPrice
  lowPrice=get_lowPrice(List)
  volumeList=getVolume(List) 
  maxNum=getMax(volumeList)
  minNum=getMin(volumeList)
  #Get the highest price through the function getHighestPrice
  highestPrice=getHighestPrice(highPrice)
  #Get the lowest price through the function getlowestPrice
  lowestPrice=getLowestPrice(lowPrice)
  #Draw the ordinate through the function addYAxis
  pic=addYAxis(pic,highestPrice,lowestPrice)
  difference=float(highestPrice)-float(lowestPrice)
  #Add the file name below the chart
  addText(pic,int(getWidth(pic)/2-50),int(getHeight(pic)-20),inputDataFile[:inputDataFile.index('.')])
  #set the start postion of chart
  sx=int(getWidth(pic)*0.1)
  sy=int(getHeight(pic)*0.1)
  ex=int(getWidth(pic)*0.9)
  ey=int(getHeight(pic)*0.9)
  #get width and height of the chart
  y=ey-sy
  x=ex-sx
  #Draw axes
  addLine(pic,sx,ey,ex,ey)
  text1='Price($)'
  addText(pic,1,getHeight(pic)/2-10,text1)
  grey=makeColor(144,144,144)
  for n in range(0,10):
    newy=int(y*n/10+sy)
    addLine(pic,sx,newy,ex,newy,grey) 
    
   #begin to draw candlestick
  for i in range(0,10):
    #these X and Y for lines
    startY=(float(highPrice[i])-lowestPrice)/difference*y
    startY=int(ey-startY)
    endY=(float(lowPrice[i])-lowestPrice)/difference*y
    endY=int(ey-endY)
    newx=int(x*i/10+sx)
    dateString=dateList[i]
    addText(pic,newx+20,ey+20,dateString)
    #Draw the vertical center line in CandlestickChart
    addLine(pic,newx+30,startY,newx+30,endY)
    #these X and Y for chart
    startNewY=(float(openPrice[i])-lowestPrice)/difference*y
    startNewY=int(ey-startNewY)
    endNewY=(float(closePrice[i])-lowestPrice)/difference*y
    endNewY=int(ey-endNewY)
    #Judging whether the CandlestickChart is black or white
    if float(closePrice[i])>float(openPrice[i]):
      pic=makeWhiteChart(pic,newx+20,endNewY,newx+40,startNewY)
    else:
      pic=makeBlackChart(pic,newx+20,startNewY,newx+40,endNewY)
  #Save the picture in the specified file name
  path=getMediaPath()+outputImageName
  writePictureTo(pic,path)
  #show image
  show(pic)
def makeEmptyPic(sizeOption):
  #Initialize the length and width of the picture
  pictureHeight=0
  pictureWidth=0
  #Select the size of the picture according to the parameters
  #Judging the image width corresponding to three different values by if
  if sizeOption==1:
    pictureWidth=600
  elif sizeOption==2:
    pictureWidth=700
  elif sizeOption==3:
    pictureWidth=800
  #The height of the picture is equal to three-quarters of the picture width
  pictureHeight=int(pictureWidth*3/4)
  #make an empty picture
  pic=makeEmptyPicture(pictureWidth,pictureHeight,white)
  return pic
#This function can extract date of file and save them in a list
def readCSV(filename):
  #get the file
  file = open(getMediaPath(filename), 'rt') 
  contents = file.readlines()
  file.close()
  #Remove the content through the loop and replace method\n
  for i in range(0,len(contents)):
   contents[i]=contents[i].replace("\n","")
  print(contents)
  #Create a new list for storing file contents
  List = []
  #Use the content of each piece of data to separate
  for i in range(0,len(contents)):
    myContents = contents[i].split(',')
    List.append(myContents)
    #Return to this list
  return List
  #################################
  
  #This function opens the file by manually selecting the file
def readCsv():
  #get the file
  filename=pickAFile()
  file = open(filename, 'rt') 
  contents = file.readlines()
  file.close()
  for i in range(0,len(contents)):
   contents[i]=contents[i].replace("\n","")
  print(contents)
  List = []
  for i in range(0,len(contents)):
    myContents = contents[i].split(',')
    List.append(myContents)  
  return List
  #################################
  
  #This function is used to get a list of dates
def getDate(List):
  date=[]
  for i in range(1,11):
    date.append(List[i][0])
    #Remove the year from the date in a circular way
  for i in range(0,10):
   date[i]=date[i].replace("/2020","")
  for i in range(0,10):
   date[i]=date[i].replace("/2021","")
   #Return to new date list
  return date
  ####################
  
  #This function is used to get the volume list
def getVolume(List):
  volume=[]
  for i in range(1,11):
    volume.append(List[i][5]) 
  return volume
  ####################
  
  #This function is used to get the openPrice list
def get_openPrice(List):
  openPrice=[]
  for i in range(1,11):
    openPrice.append(List[i][1])
  return openPrice
  ####################
  #This function is used to get the highPrice list
def get_highPrice(List):
  highPrice=[]
  for i in range(1,11):
    highPrice.append(List[i][2])
  return highPrice
  ####################
  #This function is used to get the lowPrice list
def get_lowPrice(List):
  lowPrice=[]
  for i in range(1,11):
    lowPrice.append(List[i][3])
  return lowPrice
  ####################
  #This function is used to get the closePrice list
def get_closePrice(List):
  closePrice=[]
  for i in range(1,11):
    closePrice.append(List[i][4])
  return closePrice
  #################### 
  #This function is used to get the Max value
def getMax(List):
  max_num = float(List[0])
  for i in range(len(List)):
    if float(List[i])>max_num:
      max_num=float(List[i])
  return max_num
  #This function is for the minimum
def getMin(List):
  min_num = float(List[0])
  for i in range(len(List)):
    if float(List[i])<min_num:
      min_num=float(List[i])
  return min_num
  #This function is used to draw a histogram

#get the highest price
def getHighestPrice(highPrice):
  highestPrice=0
  for i in range(0,10):
    if float(highPrice[i])>highestPrice:
      highestPrice=float(highPrice[i])
  return highestPrice
##################
def addYAxis(pic,highestPrice,lowestPrice):
  #Get the highest and lowest difference
  difference=highestPrice-lowestPrice
  sx=int(getWidth(pic)*0.1)
  sy=int(getHeight(pic)*0.1)
  ex=int(getWidth(pic)*0.9)
  ey=int(getHeight(pic)*0.9)
  #get width and height of the chart
  y=ey-sy
  x=ex-sx
  num=0.00
  for i in range(0,11):
    newy=int(y*i/10+sy)
    yAxis=highestPrice-difference*num
    yAxis='%.2f'%yAxis
    addText(pic,sx-30,newy,yAxis)
    num=num+0.10
  return pic
###############################

#get the lowest price
def getLowestPrice(lowPrice):
  lowestPrice=float(lowPrice[1])
  for i in range(0,10):
    if lowestPrice>float(lowPrice[i]):
      lowestPrice=float(lowPrice[i])
  return lowestPrice
#######################
# draw white chart on picture
def makeWhiteChart(pic,startX,startY,endX,endY):
  for X in range(startX,endX+1):
    for Y in range(startY,endY+1):
      pix=getPixel(pic,X,Y)
      if X==startX or X==endX:
        setColor(pix,black)
      elif Y==startY or Y==endY:
        setColor(pix,black)
      else:
        setColor(pix,white)
  return(pic)
##########################################

#draw black chart on picture
def makeBlackChart(pic,startX,startY,endX,endY):
  for X in range(startX,endX+1):
    for Y in range(startY,endY+1):
      pix=getPixel(pic,X,Y)
      setColor(pix,black)
  return(pic)      
##########################################
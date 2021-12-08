library(shiny)
library(fmsb)
library(wordcloud2)
library(grDevices)

data<-read.csv("total.csv",encoding = "UTF-8",header=T)
data[,2] <- as.character(data[,2])
data[,"name"] <- as.character(data[,"name"])
data[,"address"] <- as.character(data[,"address"])
data[,"state"] <- as.character(data[,"state"])
data[,"city"] <- as.character(data[,"city"])
data[,"Suggestions"] <- as.character(data[,"Suggestions"])
data[,"strengths"] <- as.character(data[,"strengths"])
ave <- read.csv("overall_review.csv",encoding = "UTF-8",header=T)
#data[,24]<- as.character(data[,24])
#data[,25]<- as.character(data[,25])

shinyServer(function(input,output){
  # Search by Business Name
  output$selectcityname<-renderUI({
    selectInput("city","Choose City:",
                sort(data[which(data[,"state"]==input$state),"city"]))
  })
  output$selectshopname<-renderUI({
    selectInput("name","Choose Business Name:",
                sort(data[which(data[,"city"]==input$city & data[,"state"]==input$state) ,"name"]))
  })
  #output$selectid<-renderUI({
  #  selectInput("nameid","Choose Business ID:",
  #              sort(data[which(data[,"city"]==input$city & data[,"name"]==input$name),"business_id"]))
  #})
  # 
  id <- eventReactive(input$submit,{
    return(data[which(data[,"city"]==input$city & data[,"name"]==input$name),"business_id"])
    #if( input$inputway == "bid" & input$id %in% as.character(data[,2]))
    #  return( input$id )
    #if( input$inputway == "bname" & is.na(input$nameid)==0)
    #  return( input$nameid )
    #else
    #  return( 0 )
  })
  # Page Competitor Analysis "Overall"
  output$plot1 <- renderPlot({
    data1<-rbind(data[which(data[,2]==id()),c("Atmosphere_Rating","Food_Rating","Price_Rating","Service_Rating","Tea_Ingredients_Rating","Tea_Types_Rating")],
                 as.numeric(ave[1,c("Atmosphere_Rating","Food_Rating","Price_Rating","Service_Rating","Tea_Ingredients_Rating","Tea_Types_Rating")]))
    rownames(data1)<-c("Shop","Average")
    data1<-rbind(rep(5,6),rep(0,6),data1)
    colors_border=c(  rgb(0.8,0.2,0.5,0.9),rgb(0.2,0.5,0.5,0))
    colors_in=c( rgb(0.8,0.2,0.5,0),rgb(0.2,0.5,0.5,0.4))
    r1<-radarchart( data1, axistype=1, seg = 5,
                    #custom polygon
                    pcol=colors_border , pfcol=colors_in , plwd=2 , plty=1,
                    #custom the grid
                    cglcol="grey", cglty=1, axislabcol="grey", caxislabels=seq(0,6,1), cglwd=1,
                    #custom labels
                    vlcex=1,title="Overall"
    )
    legend(-2, 1.4, legend = rownames(data1[-c(1,2),]), bty = "n", pch=20 , col=c(rgb(0.8,0.2,0.5,0.9),rgb(0.2,0.5,0.5,0.4)) , text.col = "grey", cex=1.2, pt.cex=3)
    return(r1)
  })
  
  # Page Competitor Analysis "Ingredients"
  output$plot2 <- renderPlot({
    data2<-rbind(data[which(data[,2]==id()),c("bubble","boba","rainbow","taro","herbal")],
                 as.numeric(ave[1,c("bubble","boba","rainbow","taro","herbal")]))
    rownames(data2)<-c("Shop","Average")
    data2<-rbind(rep(5,5),rep(0,5),data2)
    colors_border=c(  rgb(0.8,0.2,0.5,0.9),rgb(0.2,0.5,0.5,0))
    colors_in=c( rgb(0.8,0.2,0.5,0),rgb(0.2,0.5,0.5,0.4))
    r2<-radarchart( data2, axistype=1, seg = 5,
                    #custom polygon
                    pcol=colors_border , pfcol=colors_in , plwd=2 , plty=1,
                    #custom the grid
                    cglcol="grey", cglty=1, axislabcol="grey", caxislabels=seq(0,6,1), cglwd=1,
                    #custom labels
                    vlcex=1,title="Ingredients"
    )
    legend(-2, 1.4, legend = rownames(data2[-c(1,2),]), bty = "n", pch=20 , col=c(rgb(0.8,0.2,0.5,0.9),rgb(0.2,0.5,0.5,0.4))  , text.col = "grey", cex=1.2, pt.cex=3)
    return(r2)
  })
  
  # Page Competitor Analysis "Tea_Types"
  output$plot3 <- renderPlot({
    data3<-rbind(data[which(data[,2]==id()),c("green_tea","oolong_tea","black_tea","red_tea","matcha","jasmine")],
                 as.numeric(ave[1,c("green_tea","oolong_tea","black_tea","red_tea","matcha","jasmine")]))
    rownames(data3)<-c("Shop","Average")
    data3<-rbind(rep(5,6),rep(0,6),data3)
    colors_border=c(  rgb(0.8,0.2,0.5,0.9),rgb(0.2,0.5,0.5,0))
    colors_in=c( rgb(0.8,0.2,0.5,0),rgb(0.2,0.5,0.5,0.4))
    r3<-radarchart( data3, axistype=1, seg = 5,
                    #custom polygon
                    pcol=colors_border , pfcol=colors_in , plwd=2 , plty=1,
                    #custom the grid
                    cglcol="grey", cglty=1, axislabcol="grey", caxislabels=seq(0,6,1), cglwd=1,
                    #custom labels
                    vlcex=1,title="Tea_Types"
    )
    legend(-2, 1.4, legend = rownames(data3[-c(1,2),]), bty = "n", pch=20 , col=c(rgb(0.8,0.2,0.5,0.9),rgb(0.2,0.5,0.5,0.4))  , text.col = "grey", cex=1.2, pt.cex=3)
    return(r3)
  })
  
  # Page Competitor Analysis "Dessert"
  output$plot4 <- renderPlot({
    data4<-rbind(data[which(data[,2]==id()),c("dessert","cake","tiramisu","coffee")],
                 as.numeric(ave[1,c("dessert","cake","tiramisu","coffee")]))
    rownames(data4)<-c("Shop","Average")
    data4<-rbind(rep(5,4),rep(0,4),data4)
    colors_border=c(  rgb(0.8,0.2,0.5,0.9),rgb(0.2,0.5,0.5,0))
    colors_in=c( rgb(0.8,0.2,0.5,0),rgb(0.2,0.5,0.5,0.4))
    r4<-radarchart( data4, axistype=1, seg = 5,
                    #custom polygon
                    pcol=colors_border , pfcol=colors_in , plwd=2 , plty=1,
                    #custom the grid
                    cglcol="grey", cglty=1, axislabcol="grey", caxislabels=seq(0,6,1), cglwd=1,
                    #custom labels
                    vlcex=1,title="Dessert"
    )
    legend(-2, 1.4, legend = rownames(data4[-c(1,2),]), bty = "n", pch=20 , col=c(rgb(0.8,0.2,0.5,0.9),rgb(0.2,0.5,0.5,0.4))  , text.col = "grey", cex=1.2, pt.cex=3)
    return(r4)
  })
  
  # Notice2
  output$notice2<-renderText({
    # Add if condition to make sure the sentence won't show up before clicking "Submit"
    if (data[data[,2]==id(),2] != 0) print("No related reviews if there is any 0 in the radarplot")
  })
  
  
  # Business Overview Page
  output$nametitle <- renderText({data[data[,2]==id(),"name"]})
  img<-reactive({
    if(id() == 0 )
      return(0)
    else
      return(data[data[,2]==id(),"stars"])
  })
  
  output$image<-renderImage({
    list(src = paste(img(),"stars",".png",sep=""),
         contentType = 'image/png',
         width=190.4,
         height=37.4,
         alt = "OOF! The Pic Seems Broken!")
  },deleteFile = FALSE)
  
  output$title<-renderImage({
    list(src = "title.jpg",
         width=153.75,
         height=54.75,
         alt = "OOF! The Pic Seems Broken!")
  },deleteFile = FALSE)
  
  
  # how many stars
  output$stars<-renderValueBox({
    valueBox(
      data[data[,2]==id(),"stars"], "Stars", icon = icon("thumbs-up", lib = "glyphicon"), color = "yellow"
    )
  })
  
  # how many reviews
  output$revnum<-renderValueBox({
    valueBox(
      data[data[,2]==id(),"review_count"], "Reviews", icon = icon("credit-card")
    )
  })
  
  # Specific Address
  output$address1<-renderText({
    data[data[,2]==id(),"address"]
  })
  
  # Address in InfoBox
  output$address3<-renderInfoBox({
    infoBox(
      "ADDRESS", data[data[,2]==id(),"address"], icon = icon("list"),
      color = "purple"
    )
  })
  
  # City & State
  output$address2<-renderText({
    if(id()==0)
      return("oof, seems like there's something wrong with your input")
    else
      return(paste(data[data[,2]==id(),"city"],", ",data[data[,2]==id(),"state"],sep=""))
  })
  
  # title_open
  # output$title_open<-renderText({
  #   if (id()==0)
  #     return("oof, seems like there's something wrong with your input")
  #   else
  #     return("Open Hours:")
  # })
  
  # Open hours
  output$openhours<-renderUI({
    #str <- "Open Hours"
    for (i in c("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"))
    {
      if (data[data[,2]==id(),i] == "None") assign(paste0("d", i), "close")
      else assign(paste0("d", i), paste(i, ":", data[data[,2]==id(),i]))
    }
    HTML(paste(dMonday, dTuesday, dWednesday, dThursday, dFriday, dSaturday, dSunday, sep = '<br/>'))
  })
  
  
  # Aspect Scores
  output$barplot<-renderPlot({
    barplot(as.numeric(data[which(data[,2]==id()),c("Atmosphere_Rating","Food_Rating","Price_Rating","Service_Rating","Tea_Ingredients_Rating","Tea_Types_Rating")]),names.arg=c("Atmosphere", "Food", "Price", "Service","Ingredients", "TeaTypes"),col=c("#fbb4ae","#b3cde3","#ccebc5","#decbe4","#fed9a6","#fbb4ae"),
            main ="Stars in All Aspects",ylim=c(0,5))
    abline(h=data[data[,2]==id(),"Overall"],col="red",lty=5)
    abline(h=ave[1,"Overall"],col="darkblue",lty=5)
    legend("topright",legend = c("average","overall"), bty = "n", pch=20 , col=c("red","darkblue"), lty = c(2,2))
  })
  
  # Notice1
  output$notice1<-renderText({
    # Add if condition to make sure the sentence won't show up before clicking "Submit"
    if (data[data[,2]==id(),2] != 0) print("No related reviews if there are missing parts in the barplot")
  })
  
  # The Suggestion Part
  # strengh
  output$strength<-renderText({
    data[data[,2]==id(),"strengths"]
  })

  # suggestions
  output$suggestion<-renderText({
    data[data[,2]==id(),"Suggestions"]
  })
  
  # output$strength<-renderInfoBox({
  #   infoBox(
  #     "STRENGTH", data[data[,2]==id(),"strengths"], icon = icon("thumbs-up", lib = "glyphicon"),
  #     color = "yellow", width = 12
  #   )
  # })  
  # 
  # # suggestions
  # output$suggestion<-renderInfoBox({
  #   infoBox(
  #     "SUGGESTION", data[data[,2]==id(),"Suggestions"], icon = icon("list"),
  #     color = "purple", width = 12
  #   )
  # })
  
  
})


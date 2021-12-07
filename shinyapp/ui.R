library(shiny)
library(fmsb)
library(shinydashboard)
#library(wordcloud2)

# Read data
setwd("C:/Users/ellen/Desktop/STAT 628/Module 3/")
data<-read.csv("total.csv",encoding = "UTF-8",header=T)
data[,2] <- as.character(data[,2])
data[,"name"] <- as.character(data[,"name"])
data[,"state"] <- as.character(data[,"state"])
data[,"city"] <- as.character(data[,"city"])


shinyUI(dashboardPage(
  dashboardHeader(title = "Find the Shop"),

  dashboardSidebar(
    width = 350,
    radioButtons("inputway", "Find Your Business:",
                 #list("Business Name" = "bname", "Business ID" = "bid")),
                 list("Business Name" = "bname")),
    conditionalPanel(condition="input.inputway=='bid'",
                     textInput("id","Business ID:",value = "")),
    conditionalPanel(condition="input.inputway=='bname'",
                     selectInput("state","Choose State:",
                                 list("FL","BC","OH","WA","TX","CO","GA","OR","MA"))),
    conditionalPanel(condition="input.inputway=='bname'",
                     uiOutput("selectcityname")),
    conditionalPanel(condition="(input.inputway=='bname')",
                     uiOutput("selectshopname")),
    actionButton("submit", "Submit"),
    tags$hr(),
    helpText("@@ Designed to get information about bubble tea shop")
  ),
  
  dashboardBody(
    tabsetPanel(type = "tabs",
                tabPanel("Basic Information",
                         h2(strong(textOutput("nametitle"))),
                         fluidRow(valueBoxOutput("stars"), valueBoxOutput("revnum"), infoBoxOutput("address3")),
                         fluidRow(
                                  column(5, 
                                         box(title = "Open Hours", status = "primary", collapsible=TRUE, htmlOutput("openhours"))
                                        ),
                                  column(6, align = "center",
                                         fluidRow(
                                    plotOutput("barplot"),
                                    h4(textOutput("notice1"))
                                  )))
                ),
                tabPanel("Rating Analysis",
                         fluidRow(column(6,align="center",
                                         plotOutput("plot1"),h4(textOutput("note1"))),
                                  column(6,align="center",
                                         plotOutput("plot2"),h4(textOutput("note2")))),
                         fluidRow(column(6,align="center",
                                         plotOutput("plot3"),h4(textOutput("note3"))),
                                  column(6,align="center",
                                         plotOutput("plot4"),h4(textOutput("note4")))),
                         fluidRow(column(3),
                                  column(6,align="center",
                                         h4(textOutput("notice2"))))
                ),
                tabPanel("Performance", 
                         fluidRow(
                           column(width = 6,
                                  box(
                                    title = "STRENGTH", width = NULL, status = "primary",
                                    textOutput("strength")
                                  )
                                  # box(
                                  #   title = "Title 1", width = NULL, solidHeader = TRUE, status = "primary",
                                  #   "BOX CONTENT"
                                  # ),
                                  # box(
                                  #   width = NULL, background = "black",
                                  #   "A box with a solid black background"
                                  # )
                           ),
                           
                           column(width = 6,
                                  # box(
                                  #   status = "warning", width = NULL,
                                  #   "Box content"
                                  # ),
                                  box(
                                    title = "SUGGESTION", width = NULL, solidHeader = TRUE, status = "warning",
                                    textOutput("suggestion")
                                  )
                                  # box(
                                  #   title = "Title 5", width = NULL, background = "light-blue",
                                  #   "A box with a solid light-blue background"
                                  # )
                           )
                         # fluidRow(
                         #   infoBoxOutput("strength")
                         # ),
                         # fluidRow(
                         #   infoBoxOutput("suggestion")
                         # )
                         )
                )

  ))
))
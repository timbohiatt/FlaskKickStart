
#=========================================================================================
# Base Flask Docker Image for Basic Web App Quick Start
#
# Developed:
#     - Tim Hiatt [timbohiatt@gmail.com] 
#
# Variables Required:
#   
#   << GENERAL VARIABLES >>
#   ${APP_NAME} 		= The Qualifer of the App You Are Wokring on (Used as a Prefix)
#   ${APP_CODE_BRANCH} 	= Which Branch of the Code Should We Be Building Against
#   
#
#   << GIT VARIABLES >>
#   ${GIT_ACCESS_TOKEN} = This is the Access token to read private Git Repositories
#	${GIT_USERNAME} 	= This is the Username that hosts the git repository
#	${GIT_REPO_NAME} 	= This is the repoitory name
#
#=========================================================================================


#=========================================================================================
FROM python:2.7-slim
MAINTAINER Tim Hiatt <timbohiatt@gmail.com>
#=========================================================================================


#Update and Download APT-GET Package Contents including Git
#=========================================================================================
ENV INSTALL_PATH /${APP_NAME}
RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH
RUN apt-get update && apt-get install -y git


#Using GitHub Access Token Connect to Private Repository and Download Code Branch
#=========================================================================================
RUN git clone -b ${APP_CODE_BRANCH} https://${GIT_ACCESS_TOKEN}:x-oauth-basic@github.com/${GIT_USERNAME}/${GIT_REPO_NAME}.git /${APP_NAME}


#Copy the Requirements File. Install all Requirements
#=========================================================================================
#COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


FROM python:2.7-slim
MAINTAINER Tim Hiatt <timbohiatt@gmail.com>

ARG APP_NAME
ARG APP_CODE_BRANCH
ARG GIT_USERNAME
ARG GIT_REPO_NAME

ENV APP_NAME=$APP_NAME
ENV APP_CODE_BRANCH=$APP_CODE_BRANCH
ENV GIT_USERNAME=$GIT_USERNAME
ENV GIT_REPO_NAME=$GIT_REPO_NAME



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
#	${GIT_USERNAME} 	= This is the Username that hosts the git repository
#	${GIT_REPO_NAME} 	= This is the repoitory name
#
#=========================================================================================

#Update and Download APT-GET Package Contents including Git
#=========================================================================================
ENV INSTALL_PATH /${APP_NAME}
RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH
RUN apt-get update && apt-get install -y git


#Copy the Requirements File. Install all Requirements
#=========================================================================================
COPY . .	
RUN pip install -r requirements.txt
RUN ["chmod", "+x", "web_boot.sh"]


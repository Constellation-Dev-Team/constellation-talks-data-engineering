# syntax=docker/dockerfile:1
FROM python:3.11

### https://github.com/iskandre/asyncio-mssql-python/blob/main/Dockerfile

# UPDATE APT-GET
RUN apt-get update

# PYODBC DEPENDENCES
RUN apt-get install -y tdsodbc unixodbc-dev
RUN apt install -y unixodbc
RUN apt-get clean -y
RUN echo '[FreeTDS] \n\
Description=FreeTDS Driver  \n\
Driver=/usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so  \n\
Setup=/usr/lib/x86_64-linux-gnu/odbc/libtdsS.so ' > /etc/odbcinst.ini 

# UPGRADE pip3
RUN pip3 install --upgrade pip

# DEPENDECES FOR DOWNLOAD ODBC DRIVER
RUN apt-get install apt-transport-https 
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update

# INSTALL ODBC DRIVER
RUN ACCEPT_EULA=Y apt-get install msodbcsql17 --assume-yes

# INSTALL ODBC POSTGRESQL DRIVER
RUN apt-get install -y odbc-postgresql

# CONFIGURE ENV FOR /bin/bash TO USE MSODBCSQL17
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile 
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc 

RUN echo 'aioodbc \n\
          pytest' > /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

RUN sed -i.bak 's~MinProtocol = TLSv[^>]*~MinProtocol = TLSv1.0~' /etc/ssl/openssl.cnf
RUN sed -i.bak 's~CipherString = DEFAULT@SECLEVEL=[^>]*~CipherString = DEFAULT@SECLEVEL=1~' /etc/ssl/openssl.cnf


WORKDIR /code/app/
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
CMD ["fastapi", "run", "main.py", "--proxy-headers", "--port", "8000", "--reload"]
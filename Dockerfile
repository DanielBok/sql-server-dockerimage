FROM mcr.microsoft.com/mssql/server:2019-CU6-ubuntu-16.04

ENV MSSQL_CLI_TELEMETRY_OPTOUT 1
ENV ACCEPT_EULA Y
ENV PATH="/opt/mssql-tools/bin/:${PATH}"

USER root
RUN apt-get update

USER mssql

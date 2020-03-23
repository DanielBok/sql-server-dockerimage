FROM mcr.microsoft.com/mssql/server:2017-CU19-ubuntu-16.04

ENV MSSQL_CLI_TELEMETRY_OPTOUT 1
ENV ACCEPT_EULA Y
ENV PATH="/opt/mssql-tools/bin/:${PATH}"

RUN apt-get update

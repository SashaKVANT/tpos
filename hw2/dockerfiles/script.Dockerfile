FROM mariadb:10.11.5

# Установка mysql-client
RUN apt-get update && \
    apt-get install -y mysql-client && \
    rm -rf /var/lib/apt/lists/*

VOLUME /data

ENTRYPOINT []
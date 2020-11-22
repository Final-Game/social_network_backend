FROM java:8-jdk-alpine

WORKDIR /opt/app

ADD . /opt/app

RUN ./mvnw clean package

ARG JAR_FILE=target/SocialNetworkBackend-0.0.1-SNAPSHOT.jar

COPY ${JAR_FILE} app.jar

EXPOSE 8080

ENTRYPOINT ["java", "-Djava.security.egd=file:/dev/./urandom","-jar","app.jar"]
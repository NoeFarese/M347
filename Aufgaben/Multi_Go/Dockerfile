# Normal - Size: 291 MB

#FROM golang:1.21-alpine
#WORKDIR /app
#COPY src .
#RUN go build -o main
#EXPOSE 8080
#CMD ["./main"]

# Multistage - Size: 21.5 MB
FROM golang:1.18 AS build
WORKDIR /app
COPY src/go.mod src/main.go ./
RUN go mod download
COPY src/. .
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o main .

FROM alpine:latest
RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=build /app/main .
RUN chmod +x ./main
EXPOSE 8080
CMD ["./main"]


# Commands
# docker build -t my-go-app . 
# docker run -p 8080:8080 my-go-app  
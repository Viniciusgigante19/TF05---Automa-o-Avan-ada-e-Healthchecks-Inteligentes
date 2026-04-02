FROM nginx:alpine

RUN rm -rf /usr/share/nginx/html/*

COPY . /usr/share/nginx/html/

COPY nginx.conf /etc/nginx/conf.d/nginx.conf

EXPOSE 80
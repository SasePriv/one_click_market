FROM nginx:1.25.3
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx
COPY nginx_no_ssl /etc/nginx/sites-enabled/
RUN mkdir -p /www/static
RUN chmod -R 755 /www/static
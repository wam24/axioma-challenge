FROM python:3.9-alpine3.17



ARG APP_ADMIN_USER
ARG APP_ADMIN_PASSWORD

ARG DOMAIN_NAME


RUN apk add --no-cache --virtual .build-deps \
                                  curl

#COPY /data /data
COPY ./requirements.txt ./requirements.txt

RUN curl https://bootstrap.pypa.io/get-pip.py -o /get-pip.py  \
    && python /get-pip.py \
    && pip3 install --upgrade pip \
    && pip install virtualenv \
    && virtualenv /env \
    && chmod u+x /env/bin/activate

RUN . /env/bin/activate && pip install -r requirements.txt


ENV VIRTUAL_ENV=/env \
    PATH=/env/bin:$PATH \
    NAME=app \
    DJANGODIR=/www \
    NUM_WORKERS=2 \
    DJANGO_SECRET_KEY=xnZADbBeju69lkaXfAP2m58Cui2Wvsc3Em4TQa56uSRCuZtqgVV079DVcrDFMARu \
    RUNDIR=/www \

    DJANGO_SETTINGS_MODULE=axioma.settings.production \

    APP_ADMIN_USER=${APP_ADMIN_USER} \
    APP_ADMIN_PASSWORD=${APP_ADMIN_PASSWORD} \

    DOMAIN_NAME=${DOMAIN_NAME}




WORKDIR /www

COPY /www .


RUN ["chmod", "+x", "startup.sh"]
RUN ["chmod", "+x", "build.sh"]
RUN ["sh", "build.sh"]


EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

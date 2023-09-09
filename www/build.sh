#!/bin/sh
# exit on error
export USER_SCRIPT="from bank.models import Usuario; Usuario.objects.create_superuser('${APP_ADMIN_USER}', 'admin@example.com', '${APP_ADMIN_PASSWORD}') if not Usuario.objects.filter(username='$APP_ADMIN_USER').exists() else None"
export SITE_SCRIPT="from django.contrib.sites.models import Site; site = Site.objects.first() or Site(); site.domain = '$DOMAIN_NAME'; site.name = '$DOMAIN_NAME'; site.save()"


# cd www
echo "Building"
python manage.py migrate --settings=$DJANGO_SETTINGS_MODULE --noinput \
&& python manage.py collectstatic --noinput \
&& python manage.py shell -c "$USER_SCRIPT" \
&& python manage.py shell -c "$SITE_SCRIPT" \
&& python manage.py fill_users
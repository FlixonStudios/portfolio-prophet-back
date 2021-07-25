release: python3 manage.py migrate
release: python3 manage.py migrate django_cron
web: gunicorn portfolio_prophet.wsgi --preload --log-file -
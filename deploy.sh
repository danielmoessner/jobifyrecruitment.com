git pull
tmp/venv/bin/pip install -r requirements.txt
tmp/venv/bin/python manage.py migrate
npm run build
./permissions.sh
systemctl restart apache2

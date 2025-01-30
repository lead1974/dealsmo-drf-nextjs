# project structure command 
tree -I 'venv|__pycache__|*.pyc|*.pyo|*.pyd|.git' > project_structure.txt

# pipenv
pipenv -rm 
pipenv install
pipenv graph

# generate .gitignore file
npx gitignore python
#initialize git
git init -b main

# start django project
django-admin startproject config .
git config --global user.email "email2lead@gmail.com"
git config --global user.name "lead1974"

# check git files for ignore
git ls-files --other --exclude-standard

pipenv install --dev psycopg2-binary==2.9.9 watchfiles==0.21.0 black==24.3.0

# building requirements
mkdir -p requirements && touch requirements/{base,local,production}.txt
mkdir -p config/settings && touch config/settings/{__init__,base,local,production}.py

# generate secret key
python -c "import secrets; print(secrets.token_urlsafe(38))"

# ensure env variable are activated
pip install --upgrade setuptools

# start django server
python manage.py runserver

# create django apps
mkdir core_apps/__init__.py
python manage.py startapp users
python manage.py startapp common
python manage.py startapp profiles
python manage.py startapp posts
python manage.py startapp issues
python manage.py startapp ratings

python manage.py runserver

# docker setup
docker system prune -f

# check local.yml file for docker
docker compose -f local.yml config
# docker create network
docker network create dealsmo_nw  
output: d60d87eb4503891f0d866e86765f1c49f6cbcd2e39f58c14efea8e2a63d07600
# build images 
DOCKER_BUILDKIT=1 docker compose -f local.yml build --no-cache
docker compose -f local.yml up --build -d --remove-orphans
# check docker volumes
docker volume inspect backend_dealsmo_postgres_data

# makefiles
sudo apt update
sudo apt install make

# make superuser
docker compose -f local.yml run --rm backend python manage.py createsuperuser

# generate secret key for .env.SIGNING_KEY
python -c "import secrets; print(secrets.token_urlsafe(38))"


####### NEXT.JS #########
npm i -D eslint-config-standard@17.1.0 eslint-plugin-tailwindcss@3.14.1 eslint-config-prettier@9.1.0 prettier@3.2.4 sharp@0.33.2

#80 nextjs packages
npm i @heroicons/react 
npx shadcn@latest init

#83 dark/light themes
npm i next-themes

#85 shadcn components
npx shadcn@latest add dropdown-menu badge button avatar form card input label menubar pagination skeleton sheet tabs textarea select

npm install @radix-ui/react-icons
npm i date-fns

# Adding new API endpint for 'report' in this nextjs "fronend" project
1. Add typedTag to baseApiSlice.ts : 'Report'
2. Add new folder under lib/redux/features/reports
3. Add new validattionSchema to 'reports' : ReportCreateSchema.ts
4. Add new report schema to index.ts 
5. Add new endpoint to reportApiSlice.ts

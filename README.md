## Start Machine Learning Project.

### Software and account Requirements.

1. [Github Account](https://github.com/)
2. [Heroku Account](https://id.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT CLI](https://git-scm.com/downloads)

Create git clone to your system.
```
git clone <git repo URL>
```
Creating conda environment.
```
conda create -p venv python==3.7 -y
```
Activate conda environment.
```
conda activate <environment_name/>
```
OR
```
conda activate <environment_name>
```
To Install Requirements.
```
pip install -r requirements.txt
```
To add file into git.
```
git add .
```
OR
```
git add <file_name>
```

> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file.

To check the git status.
```
git status
```
To check all version mainted by git.
```
git log
```

To create version/commit all changes by git.
```
git commit -m "message"
```
To send version/changes to github.
```
git push origin main
```
To check remote URL.
```
git remote -v
```
To setup CI/CD pipeline in heroku we need 3 information
1. HEROKU_EMAIL = vedprakashjangid.jpr@gmail.com
2. HERUKU_API_KEY = <>
3. HEROKU_APP_NAME = ml-first-app-ved

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for dockermust be lowercase

To list docker images
```
docker images
```

Run Docker image
```
docker run -p 5000:5000 -e PORT=5000 <image_id>
```

To check running container docker
```
docker ps
```
To stop docker container
```
docker strop <container_id>
```


```
python setup.py install
```
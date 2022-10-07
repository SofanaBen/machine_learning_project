## Start Machine Learning project.

### Requirements.

1. [Github Account] (https://github.com/)
2. [Heroku Acccount] (https://dashboard.heroku.com/apps)
3. [VS Code IDE] (https://code.visualstudio.com/)
4. [git cli] (https://git-scm.com/download/mac)

Creating conda environement 
```

conda create -p venv python==3.7 -y
```

To activate the virtual env
```

conda activate venv/ or onda activate venv
```

To instsall flask
```

pip install -r requirements.txt
```

To setup CI/CD pipeline in heroku we need 3 information
1. HEROKU_EMIAL =  sofana.benoutiq123@gmail.com
2. HEROKU_API_KEY = <cannotshowhere>
3. HEROKU_APP_NAME = ml-regression-app75


BUILD DOCKER IMAGE

```

docker build -t <image_name>:<tagname>
```
Note: Image name for docker should be lowercase

To List docker images 
```

docker images
```
To Run Docker Images
```

docker run -p 5000:5000 -e PORT=5000 4fbdab1faea3
```
 
 To check running containers:
 ```

 docker ps
 ```

 To stop running container
 ```

 docker stop
 ```
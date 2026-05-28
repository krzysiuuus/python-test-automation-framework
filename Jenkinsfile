pipeline {

```
agent any

stages {

    stage('Checkout') {
        steps {
            git branch: 'main',
            url: 'https://github.com/krzysiuuus/python-test-automation-framework.git'
        }
    }

    stage('Build Docker image') {
        steps {
            sh 'docker build -t python-test-framework .'
        }
    }

    stage('Run API tests') {
        steps {
            sh 'docker run --rm -v $(pwd)/reports:/app/reports python-test-framework'
        }
    }

    stage('Publish Allure Report') {
        steps {
            allure([
                includeProperties: false,
                jdk: '',
                results: [[path: 'reports']]
            ])
        }
    }
}
```

}

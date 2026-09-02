pipeline {

    agent any

    options {
        skipDefaultCheckout(true)
    }

    triggers {
        pollSCM('H/5 * * * *')
    }

    parameters {
        choice(
            name: 'BROWSER',
            choices: ['chrome', 'firefox', 'edge'],
            description: 'Browser used for UI tests'
        )
    }

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
                sh '''
                    rm -rf reports
                    mkdir -p reports/api/allure

                    docker run --rm \
                        --volumes-from jenkins \
                        -w ${WORKSPACE} \
                        python-test-framework \
                        pytest api_tests/tests \
                        -v \
                        --alluredir=reports/api/allure

                    find reports -maxdepth 4 -type f -print
                '''
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'reports/api/allure']]
                ])
            }
        }
    }
}
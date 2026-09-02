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

        stage('Run UI tests') {
            steps {
                sh '''
                    mkdir -p reports/ui/allure

                    docker run --rm \
                        --volumes-from jenkins \
                        -e CI=true \
                        -e REMOTE_URL=http://host.docker.internal:4444/wd/hub \
                        -w ${WORKSPACE} \
                        python-test-framework \
                        pytest page_object_pattern/tests \
                        -v \
                        --browser=${BROWSER} \
                        --remote \
                        --reruns 1 \
                        --reruns-delay 2 \
                        --alluredir=reports/ui/allure
                '''
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [
                        [path: 'reports/api/allure'],
                        [path: 'reports/ui/allure']
                    ]
                ])
            }
        }
    }
}
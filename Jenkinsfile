pipeline{
    agent any
    stages{
        stage('calculate'){
            steps{
                sh 'pip3 install python3'
                sh 'python --version'
                sh 'python calc_pi.py'
            }
        }
    }
}

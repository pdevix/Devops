pipeline{
    agent any
    stages{
        stage('calculate'){
            steps{
                sh 'python --version'
                sh 'python calc_pi.py'
            }
        }
    }
}

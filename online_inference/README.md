### Docker

In this repository launch: `sudo docker build . -t reconrus/made-ml-prod-hw2:v2`  

To run the image: `sudo docker run -p 8000:8000 reconrus/made-ml-prod-hw2:v2`

To pull the image: `sudo docker pull reconrus/made-ml-prod-hw2:v2`

### Request

`python3 send_request.py --ip [server ip] --port [server port] --age [age] --sex [sex index] --cp [chest pain type index] --trestbps [resting blood pressure] --chol [serum cholestoral in mg/dl] --fbs [(fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)] --restecg [resting electrocardiographic results] --thalach [maximum heart rate achieved] --exang [exercise induced angina (1 = yes; 0 = no)] --oldpeak [ST depression induced by exercise relative to rest] --slope [the slope of the peak exercise ST segment] --ca [number of major vessels (0-3) colored by flourosopy] --thal [0 = normal; 1 = fixed defect; 2 = reversable defect and the label]`

Example:
`python3 send_request.py --ip localhost --port 8000 --age 55 --sex 0 --cp 1 --trestbps 50 --chol 50 --fbs 0 --restecg 1 --thalach 100 --exang 0 --oldpeak 110 --slope 2 --ca 3 --thal 2`

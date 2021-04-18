# README

## Copy Model from experiment

```sh
~/Give-Me-Some-Credit-Kaggle-Challenge/api$ chmod +x setup.sh
~/Give-Me-Some-Credit-Kaggle-Challenge/api$ ./setup.sh
```

## Build Docker Image

```sh
~/Give-Me-Some-Credit-Kaggle-Challenge/api$ docker build -t give-me-some-credit-api .
```

## Run Docker Container
```sh
~/Give-Me-Some-Credit-Kaggle-Challenge/api$ docker run -v `pwd`/src/:/app/ -e config_path=/app/config.ini -p 8001:80 give-me-some-credit-api:latest
```

## Test API

### Sample data in JSON
```json
{
    "RevolvingUtilizationOfUnsecuredLines":0.88551908,
    "age":43,
    "NumberOfTime3059DaysPastDueNotWorse":0,
    "DebtRatio":0.177512717,
    "MonthlyIncome":5700,
    "NumberOfOpenCreditLinesAndLoans":4,
    "NumberOfTimes90DaysLate":0,
    "NumberRealEstateLoansOrLines":0,"NumberOfTime6089DaysPastDueNotWorse":0,
    "NumberOfDependents":0
}
```

### Sample cURL to Classify
```sh
curl -i -H "Accept: application/json" -H "Content-type: application/json" -d '{"RevolvingUtilizationOfUnsecuredLines":0.88551908,"age":43,"NumberOfTime3059DaysPastDueNotWorse":0,"DebtRatio":0.177512717,"MonthlyIncome":5700,"NumberOfOpenCreditLinesAndLoans":4,"NumberOfTimes90DaysLate":0,"NumberRealEstateLoansOrLines":0,"NumberOfTime6089DaysPastDueNotWorse":0,"NumberOfDependents":0}' -X GET "http://127.0.0.1:8001/classify/"
```
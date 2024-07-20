
# GDSC-Email Template

This Python script automates the process of reading a list of email addresses from an Excel sheet and sending emails to them.

The message template is customizable, making it suitable for tasks such as filling out attendance forms or notifying recipients of sudden changes in plans.







## Documentation

[Email Documentation](https://drive.google.com/file/d/1Iy05h9xTIRvcrjFG7ZXRbpN2L7wEmK1r/view?usp=sharing)


## Project Structure

#### Basic Files



| Files | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `confirmedList.csv` | `csv` |  All the emails to be sent will be pasted onto column A |
| `main.py` | `py` |  Includes all the variables that can be customised|

#### Requirement

```
  Set your email App password : https://myaccount.google.com/u/1/apppasswords
  
  *Only works if the account has 2FA enabled
```



## Run Locally

Clone the project

```bash
  git clone https://github.com/The-Reaperx/GDSC-Email.git
```


Install dependencies

```bash
  npm install
```

Start the server

```bash
  npm run start
```


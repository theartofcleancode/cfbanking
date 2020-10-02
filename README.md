# cfbanking
Console File Banking: Banking using the console as user i/o interface and a text file as database

### **INSTALLATION:**

***Create a virtual env:***

```
python3 -m venv bank
```

Activate the virtual environment

```
source bank/bin/activate
```

***Install dependencies:***

After virtual env has been activated, install the following dependencies

- ***banking***
```shell
pip install git+https://github.com/theartofcleancode/banking.git@python#egg=banking-1.0.0
```

- ***pythonapi***
```
pip install git+https://github.com/theartofcleancode/pythonapi.git#egg=pythonapi-1.0.0
```

- ***consolefile***
```
pip install git+https://github.com/theartofcleancode/consolefile.git#egg=consolefile-1.0.0
```


***Main package:***
```
pip install git+https://github.com/theartofcleancode/cfbanking.git#egg=cfbanking-1.0.0
```

### **USAGE:**

Open your command line interface and run:

```
clean-bank
```

Results are saved into a file named `accounts.txt` in the local directory where you're running the command. Open it at the same time you are performing your actions.

N.B. You need to create a new account first. For that: chose option 1 before anything; this operation will create the `accounts.txt` database for the first time. Then you will be able to perform the other actions too.
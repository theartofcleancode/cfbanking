# cfbanking
Console File Banking: Banking using the console as user i/o interface and a text file as database

### **INSTALLATION:**

***Create a virtual env:***

```
python3 -m venv bank
```

Activate the virtual environment

<table class="docutils align-default">
<colgroup>
<col style="width: 18%">
<col style="width: 24%">
<col style="width: 58%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Platform</p></th>
<th class="head"><p>Shell</p></th>
<th class="head"><p>Command to activate virtual environment</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>POSIX</p></td>
<td><p>bash/zsh</p></td>
<td><p>$ source bank/bin/activate</p></td>
</tr>
<tr class="row-odd"><td></td>
<td><p>fish</p></td>
<td><p>$ . bank/bin/activate.fish</p></td>
</tr>
<tr class="row-even"><td></td>
<td><p>csh/tcsh</p></td>
<td><p>$ source bank/bin/activate.csh</p></td>
</tr>
<tr class="row-odd"><td></td>
<td><p>PowerShell Core</p></td>
<td><p>$ bank/bin/Activate.ps1</p></td>
</tr>
<tr class="row-even"><td><p>Windows</p></td>
<td><p>cmd.exe</p></td>
<td><p>C:\&gt; bank\Scripts\activate.bat</p></td>
</tr>
<tr class="row-odd"><td></td>
<td><p>PowerShell</p></td>
<td><p>PS C:\&gt; bank\Scripts\Activate.ps1</p></td>
</tr>
</tbody>
</table>



***Install dependencies:***

After virtual env has been activated, install the following dependencies

- ***banking***
```shell
pip install git+https://github.com/theartofcleancode/banking.git@python#egg=banking
```

- ***pythonapi***
```
pip install git+https://github.com/theartofcleancode/pythonapi.git#egg=pythonapi
```

- ***consolefile***
```
pip install git+https://github.com/theartofcleancode/consolefile.git#egg=consolefile
```


***Main package:***
```
pip install git+https://github.com/theartofcleancode/cfbanking.git#egg=cfbanking
```

### **USAGE:**

Open your command line interface and run:

```
clean-bank
```

Results are saved into a file named `accounts.txt` in the local directory where you're running the command. Open it at the same time you are performing your actions.

N.B. You need to create a new account first. For that: chose option 1 before anything; this operation will create the `accounts.txt` database for the first time. Then you will be able to perform the other actions too.

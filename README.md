# ima-python-ini_modifier
This python file can be used to modify one setting in an .ini file or add a setting directly without any other troubles.

Use it like this:

```
python configureIni.py pathToIniFile IniSection Property Value
```
# Writing to an existing file

## Updating an existing parameter in an existing section
So, a concrete example would be. Let's say you have the following .ini file located at /tmp/myIni.ini

```
[MySection]
firstParameter = 0
```

So, by running this command:
```
python /tmp/myIni.ini MySection firstParameter 3
```

you will get this in /tmp/myIni.ini:

```
[MySection]
firstParameter = 3
```

## Adding a new parameter in an existing section

```
[MySection]
firstParameter = 0
```

So, by running this command:
```
python /tmp/myIni.ini MySection secondParameter 45
```

you will get this in /tmp/myIni.ini:

```
[MySection]
firstParameter = 3
secondParameter = 45
```

## Adding a new parameter in a new section

```
[MySection]
firstParameter = 0
```

So, by running this command:
```
python /tmp/myIni.ini MyNewSection secondParameter 45
```

you will get this in /tmp/myIni.ini:

```
[MySection]
firstParameter = 3

[MyNewSection]
secondParameter = 45
```

# Writing to a new file
Writing to a new file works exactly as writing to an existing file would but the file and the sections will be created.

# db-hack

## How to install

Download `scripts.py` file and place it near `manage.py` file in the site's directory.

## How to use

Execute this command in terminal to run Django Shell:
```
python3 manage.py shell
```

You should see this:
```
(InteractiveConsole)
>>> 
```

Type this command to import all scripts and press `Enter`:
```
from scripts import *
```

Now you can use any of the three scripts.

### Fix marks

To fix marks of a student named `Фамилия Имя`, type this and press `Enter`:

```
fix_marks('Фамилия Имя')
```

### Remove Chastisements

To remove chastisements of a student named `Фамилия Имя`, type this and press `Enter`:

```
remove_chastisements('Фамилия Имя')
```


### Create Commendation

To create a commendation for a student named `Фамилия Имя` and for the subject named `Предмет`, type this and press `Enter`:

```
create_commendation('Фамилия Имя', 'Предмет')
```

## Afterword

If you had used wrong name, script will inform you. Retry the command with right name: the existing one or the more specified one.

To exit Django shell press Ctrl+D.

#TODO: translate to Russian
#TODO: add tutorial links
#TODO: add subject name error handling

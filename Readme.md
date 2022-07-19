# Forticonfig

> Script for check some params on fortigate firewall

## How to use

### config app (irst use)

> place your config in the required files
>
> create a file named cred.key in "config/"
> 
> add your cred in cred.key => username:password
>
> place your ip in file config/ip.cfg and port in config/port.cfg
>
> run script/init.py

### start app

```bash
python3 main.py <option>
```

### options (coming soon)

```txt
-p      -> test for know port use on firewall for ssh connexion
-g      -> compare group with group template
-o      -> compare object group with template
-og     -> compare group and object group with template
-r      -> compare filtering with template
-a      -> do all option
-h      -> show help
```

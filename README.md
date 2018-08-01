cloud configuration
===================

This repository hosts the standard configuration for all of my cloud services.

The `setup.py` script works by reading the markdown formatted files, and then executes commands to based on a simple syntax. This makes the documentation **easy to read**, and **scriptable**.


Quick setup
-----------
```bash
apt install python3; git clone https://github.com/jnwarp/cloud; cd cloud
python3 setup.py -s certbot nginx
```

Usage
-----

### -d {distro}

This command will attempt to run the configuration in `distro/distro.md`. Only one distro can be specified at a time.

### --service {service}

Any service confguration flags specified will be run in the order specified. First the `service/service.md` will be configured, then, after the whole process has been finished, the `service/service-defer.md` will be configured. This is useful for delaying longstanding processes.

### --host {host}

Host specific configurations can be stored in separate files. The `host/host.md` will be configured after the distro and service configurations. This allows the host configuration to override the defaults for the service specific configuration.

### --test {true, false}

By default, the script will only **simulate** the actions that it will take. In order to actually run the commands you must specify `-t false` or `--test false`. This a safety measure, as you could easily reconfigure an ***entire*** service will this script. That would be a mess to clean up...

Usage Example
--------------

```bash
apt install python3; git clone https://github.com/jnwarp/cloud; cd cloud
python3 setup.py -d ubuntu --service fbctf --host fbctf --test true
```

Document format
---------------

Headers are ignored, you may use any kind of formatting for the description or headings.

### Execute commands

Commands within a ` ```bash ` and ` ``` ` code snippet are executed. The line above is used as a code title.

#### Example

    Example title
    ```bash
    # code to execute
    ```

### Replace lines in file

If the script finds code snippet preceded by a filename, it will try to find the first word in the file and replace the whole line.  In the example below, the script finds `ConfigOptionToFind` and replaces the whole line with `ConfigOptionToFind yes`.

#### Example

    /root/example.file
    ```
    ConfigOptionToFind yes
    ```

### Replace whole file

If the script finds a code snippet preceded by an *italiciized* filename, it will repalce the whole file with the code snippet. In the example below, the **whole** file will be replaced with the contents between ` ``` ` and ` ``` `.

#### Example

    */root/replace.file*
    ```
    # file contents
    ```

### Append to file

If the script finds a code snippet preceded by a filename with a  `*` character at the end, it will append the line to the end of the file, if it doesn't already exist in the file.  In the example below, `append_me` will be added to the end of the file.

#### Example

    /root/append.file*
    ```
    append_me
    ```

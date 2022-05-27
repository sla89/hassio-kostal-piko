# Home Assistant Kostal PIKO Inverter Integration

This integration connects to the REST API of the Kostal PIKO inverter
to get the same data that are displayed on the web interface.

Thank you very much to https://www.msxfaq.de/sonst/iot/kostal15.htm for providing all the necessary information.

For detailled API information see the [API description](docs/api.yaml).

If you find any bugs or have questions do not hesitate to open a ticket. :-)
Help for improving is welcome.

## Installation
### HACS
Not yet supported

### Manual installation
1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
1. If you do not have a `custom_components` directory (folder) there, you need to create it.
1. In the `custom_components` directory (folder) create a new folder called `kostal_piko`.
1. Download file `kostal_piko.zip` from the [latest release section][releases-latest] in this repository or copy the `custom_components` folder of this repository.
1. Extract _all_ files from this archive you downloaded in the directory (folder) you created.
1. Restart Home Assistant
1. Add to the sensors list in your `configuration.yaml` file (or where ever you specify sensors):
```yaml
# Example configuration.yaml entry
sensors:
  - platform: kostal_piko
    host: IP_OF_YOUR_INVERTER
```
1. Check your configuration is valid
1. Restart Home Assistant

# Disclaimer
The code within this repository comes with no guarantee, the use of this code is your responsibility.

I take NO responsibility and/or liability for how you choose to use any of the source code available here. By using any of the files available in this repository, you understand that you are AGREEING TO USE AT YOUR OWN RISK. Once again, ALL files available here are for EDUCATION and/or RESEARCH purposes ONLY.**
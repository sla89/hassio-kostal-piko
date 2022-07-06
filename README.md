# Home Assistant Kostal PIKO Inverter Integration

This integration connects to the REST API of the Kostal PIKO inverter
to get the same data that are displayed on the web interface.

Thank you very much to https://www.msxfaq.de/sonst/iot/kostal15.htm for providing all the necessary information.

For detailled API information see the [API description](docs/api.yaml).

If you find any bugs or have questions do not hesitate to open a ticket. :-)
Help for improving is welcome.

## Compatibility
Tested with
|Type|UI version|FW version|PAR version|HW version|
|-|-|-|-|-|
|Piko 12, 15 and 17|06.53|06.17|03.50|0100|

Currently confirmed not to work with

|Type|FW version|
|-|-|
|Piko 4.2|3.74|
|Piko 4.2|3.78|

## Installation
### HACS
Not yet supported

### Manual installation
1. Download the source code of this repository.
1. Open the folder of your HA configuration (where you find `configuration.yaml`).
1. If you do not have a `custom_components` folder there, you need to create it.
1. Copy the content of the `custom_components` folder of the downloaded archive into your HA `custom_components` folder.
1. Restart Home Assistant
1. Add to the sensor list in your `configuration.yaml` file (or where ever you specify sensors):
    ```yaml
    # Example configuration.yaml entry
    sensor:
      - platform: kostal_piko
        host: IP_OF_YOUR_INVERTER
    ```
1. Ensure that your configuration is valid
1. Restart Home Assistant

# Disclaimer
The code within this repository comes with no guarantee, the use of this code is your responsibility.

> I and any contributor to this repository take **NO** responsibility and/or liability for how you choose to use any of the source code available here. **By using any of the files available in this repository, you understand that you are AGREEING TO USE AT YOUR OWN RISK.**
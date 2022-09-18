"""Kostal PIKO IQ Inverter."""
import logging

from datetime import timedelta
import voluptuous as vol
from dataclasses import dataclass

import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import (
    SensorEntity,
    PLATFORM_SCHEMA,
)

from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from homeassistant.const import (CONF_HOST)

from homeassistant.util import Throttle

from .const import (
    SENSOR_DESCRIPTIONS,
    KostalPikoSensorEntityDescription,
)

from .helper import KostalPikoClient

MIN_TIME_BETWEEN_UPDATES = timedelta(seconds=10)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_HOST): cv.string,
})

_LOGGER = logging.getLogger(__name__)


def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType = None,
) -> None:
    """Set up the Kostal PIKO Inverter platform."""
    host = config[CONF_HOST]
    _LOGGER.info(f'Setting up client for Kostal PIKO Inverter {host}...')
    client = KostalPikoClient(host)
    _LOGGER.info('Setting up Kostal PIKO Inverter sensors...')
    sensors = []
    for description in SENSOR_DESCRIPTIONS:
        sensors.append(KostalPikoSensor(client, description))

    add_entities(sensors)


class KostalPikoSensor(SensorEntity):
    """Representation of the Kostal PIKO Sensor."""
    def __init__(self, client: KostalPikoClient,
                 description: KostalPikoSensorEntityDescription):
        """Initialize the sensor."""
        self.entity_description = description.description

        self.entry_id = description.description.key
        self._client = client
        self._dxs_id = description.dxs_id
        self._formatter = description.formatter

        self.update()

    @property
    def unique_id(self) -> str:
        """Return the unique id of this Sensor Entity."""
        return f"{self.entry_id}_{self._dxs_id}"

    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    def update(self):
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        try:
            raw_value = self._client.get_data(self._dxs_id)

            if self._formatter:
                raw_value = self._formatter(raw_value)

            self._attr_native_value = raw_value
            self._attr_available = True
        except Exception as e:
            _LOGGER.error(
                f"Failed updating sensor {self.entity_description.name}: {repr(e)}"
            )
            self._attr_available = False
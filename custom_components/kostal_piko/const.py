from numbers import Number
from homeassistant.components.sensor import (SensorDeviceClass,
                                             SensorEntityDescription,
                                             SensorStateClass)

from homeassistant.const import (ENERGY_KILO_WATT_HOUR, POWER_WATT,
                                 ELECTRIC_POTENTIAL_VOLT, TIME_HOURS,
                                 PERCENTAGE, ELECTRIC_CURRENT_AMPERE,
                                 FREQUENCY_HERTZ)


class KostalPikoSensorEntityDescription():
    """A class that describes Kostal PIKO PIKO entities."""

    description: SensorEntityDescription = None
    dxs_id: Number = None

    def __init__(self, description: SensorEntityDescription, dxs_id: Number):
        self.description = description
        self.dxs_id = dxs_id


SENSOR_DESCRIPTIONS: tuple[KostalPikoSensorEntityDescription, ...] = (
    # Current DC Input total
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_total_dc_input",
            name="Kostal PIKO Total DC Input",
            device_class=SensorDeviceClass.POWER,
            state_class=SensorStateClass.MEASUREMENT,
            native_unit_of_measurement=POWER_WATT,
            icon="mdi:solar-panel"),
        dxs_id=33556736,
    ),

    # Current Grid output
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_grid_output_power",
            name="Kostal PIKO Grid Output Power",
            device_class=SensorDeviceClass.POWER,
            state_class=SensorStateClass.MEASUREMENT,
            native_unit_of_measurement=POWER_WATT,
            icon="mdi:solar-power"),
        dxs_id=67109120,
    ),

    # Current self consumption
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_current_self_consumption",
            name="Kostal PIKO Current Self Consumption",
            device_class=SensorDeviceClass.ENERGY,
            state_class=SensorStateClass.MEASUREMENT,
            native_unit_of_measurement=POWER_WATT,
            icon="mdi:power-plug"),
        dxs_id=83888128,
    ),

    # DC Input 1 sensors
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_dc_input_1_current",
            name="Kostal PIKO DC Input 1 Current",
            device_class=SensorDeviceClass.CURRENT,
            state_class=SensorStateClass.MEASUREMENT,
            native_unit_of_measurement=ELECTRIC_CURRENT_AMPERE,
            icon="mdi:power-plug"),
        dxs_id=33555201,
    ),
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_dc_input_1_voltage",
            name="Kostal PIKO DC Input 1 Voltage",
            device_class=SensorDeviceClass.VOLTAGE,
            state_class=SensorStateClass.MEASUREMENT,
            native_unit_of_measurement=ELECTRIC_POTENTIAL_VOLT,
            icon="mdi:power-plug"),
        dxs_id=33555202,
    ),
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_dc_input_1_power",
            name="Kostal PIKO DC Input 1 Power",
            device_class=SensorDeviceClass.POWER,
            state_class=SensorStateClass.MEASUREMENT,
            native_unit_of_measurement=POWER_WATT,
            icon="mdi:power-plug"),
        dxs_id=33555203,
    ),

    # DC Input 2 sensors
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_dc_input_2_current",
            name="Kostal PIKO DC Input 2 Current",
            device_class=SensorDeviceClass.CURRENT,
            state_class=SensorStateClass.MEASUREMENT,
            native_unit_of_measurement=ELECTRIC_CURRENT_AMPERE,
            icon="mdi:power-plug"),
        dxs_id=33555457,
    ),
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_dc_input_2_voltage",
            name="Kostal PIKO DC Input 2 Voltage",
            device_class=SensorDeviceClass.VOLTAGE,
            state_class=SensorStateClass.MEASUREMENT,
            native_unit_of_measurement=ELECTRIC_POTENTIAL_VOLT,
            icon="mdi:power-plug"),
        dxs_id=33555458,
    ),
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_dc_input_2_power",
            name="Kostal PIKO DC Input 2 Power",
            device_class=SensorDeviceClass.POWER,
            state_class=SensorStateClass.MEASUREMENT,
            native_unit_of_measurement=POWER_WATT,
            icon="mdi:power-plug"),
        dxs_id=33555459,
    ),

    # DC Input 3 sensors
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_dc_input_3_current",
            name="Kostal PIKO DC Input 3 Current",
            device_class=SensorDeviceClass.CURRENT,
            state_class=SensorStateClass.MEASUREMENT,
            native_unit_of_measurement=ELECTRIC_CURRENT_AMPERE,
            icon="mdi:power-plug"),
        dxs_id=33555713,
    ),
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_dc_input_3_voltage",
            name="Kostal PIKO DC Input 3 Voltage",
            device_class=SensorDeviceClass.VOLTAGE,
            state_class=SensorStateClass.MEASUREMENT,
            native_unit_of_measurement=ELECTRIC_POTENTIAL_VOLT,
            icon="mdi:power-plug"),
        dxs_id=33555714,
    ),
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_dc_input_3_power",
            name="Kostal PIKO DC Input 3 Power",
            device_class=SensorDeviceClass.POWER,
            state_class=SensorStateClass.MEASUREMENT,
            native_unit_of_measurement=POWER_WATT,
            icon="mdi:power-plug"),
        dxs_id=33555715,
    ),

    # Grid frequency
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_grid_frequency",
            name="Kostal PIKO Grid Frequency",
            device_class=SensorDeviceClass.FREQUENCY,
            state_class=SensorStateClass.MEASUREMENT,
            native_unit_of_measurement=FREQUENCY_HERTZ,
            icon="mdi:power-plug"),
        dxs_id=67110400,
    ),

    # Phase 1
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_phase_1_current",
            name="Kostal PIKO Phase 1 Current",
            device_class=SensorDeviceClass.CURRENT,
            state_class=SensorStateClass.MEASUREMENT,
            native_unit_of_measurement=ELECTRIC_CURRENT_AMPERE,
            icon="mdi:power-plug"),
        dxs_id=67109377,
    ),
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_phase_1_voltage",
            name="Kostal PIKO Phase 1 Voltage",
            device_class=SensorDeviceClass.VOLTAGE,
            state_class=SensorStateClass.MEASUREMENT,
            native_unit_of_measurement=ELECTRIC_POTENTIAL_VOLT,
            icon="mdi:power-plug"),
        dxs_id=67109378,
    ),
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_phase_1_power",
            name="Kostal PIKO Phase 1 Power",
            device_class=SensorDeviceClass.POWER,
            state_class=SensorStateClass.MEASUREMENT,
            native_unit_of_measurement=POWER_WATT,
            icon="mdi:power-plug"),
        dxs_id=67109379,
    ),

    # Phase 2
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_phase_2_current",
            name="Kostal PIKO Phase 2 Current",
            device_class=SensorDeviceClass.CURRENT,
            state_class=SensorStateClass.MEASUREMENT,
            native_unit_of_measurement=ELECTRIC_CURRENT_AMPERE,
            icon="mdi:power-plug"),
        dxs_id=67109633,
    ),
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_phase_2_voltage",
            name="Kostal PIKO Phase 2 Voltage",
            device_class=SensorDeviceClass.VOLTAGE,
            state_class=SensorStateClass.MEASUREMENT,
            native_unit_of_measurement=ELECTRIC_POTENTIAL_VOLT,
            icon="mdi:power-plug"),
        dxs_id=67109634,
    ),
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_phase_2_power",
            name="Kostal PIKO Phase 2 Power",
            device_class=SensorDeviceClass.POWER,
            state_class=SensorStateClass.MEASUREMENT,
            native_unit_of_measurement=POWER_WATT,
            icon="mdi:power-plug"),
        dxs_id=67109635,
    ),

    # Phase 3
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_phase_3_current",
            name="Kostal PIKO Phase 3 Current",
            device_class=SensorDeviceClass.CURRENT,
            state_class=SensorStateClass.MEASUREMENT,
            native_unit_of_measurement=ELECTRIC_CURRENT_AMPERE,
            icon="mdi:power-plug"),
        dxs_id=67109889,
    ),
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_phase_3_voltage",
            name="Kostal PIKO Phase 3 Voltage",
            device_class=SensorDeviceClass.VOLTAGE,
            state_class=SensorStateClass.MEASUREMENT,
            native_unit_of_measurement=ELECTRIC_POTENTIAL_VOLT,
            icon="mdi:power-plug"),
        dxs_id=67109890,
    ),
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_phase_3_power",
            name="Kostal PIKO Phase 3 Power",
            device_class=SensorDeviceClass.POWER,
            state_class=SensorStateClass.MEASUREMENT,
            native_unit_of_measurement=POWER_WATT,
            icon="mdi:power-plug"),
        dxs_id=67109891,
    ),

    # Yield Day
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_yield_day",
            name="Kostal PIKO Yield Day",
            device_class=SensorDeviceClass.ENERGY,
            state_class=SensorStateClass.TOTAL_INCREASING,
            native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
            icon="mdi:power-plug"),
        dxs_id=251658754,
    ),

    # Home consumption Day
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_home_consumption_day",
            name="Kostal PIKO Home Consumption Day",
            device_class=SensorDeviceClass.ENERGY,
            state_class=SensorStateClass.TOTAL_INCREASING,
            native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
            icon="mdi:power-plug"),
        dxs_id=251659010,
    ),

    # Own consumption Day
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_own_consumption_day",
            name="Kostal PIKO Own Consumption Day",
            device_class=SensorDeviceClass.ENERGY,
            state_class=SensorStateClass.TOTAL_INCREASING,
            native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
            icon="mdi:power-plug"),
        dxs_id=251659266,
    ),

    # Own consumption quota Day
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_own_consumption_quota_day",
            name="Kostal PIKO Own Consumption Quota Day",
            device_class=None,
            state_class=SensorStateClass.TOTAL_INCREASING,
            native_unit_of_measurement=PERCENTAGE,
            icon="mdi:power-plug"),
        dxs_id=251659278,
    ),

    # Own consumption quota Day
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_autarky_day",
            name="Kostal PIKO Autarky Day",
            device_class=None,
            state_class=SensorStateClass.TOTAL_INCREASING,
            native_unit_of_measurement=PERCENTAGE,
            icon="mdi:power-plug"),
        dxs_id=251659279,
    ),

    # Yield Total
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_yield_total",
            name="Kostal PIKO Yield Total",
            device_class=SensorDeviceClass.ENERGY,
            state_class=SensorStateClass.TOTAL_INCREASING,
            native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
            icon="mdi:power-plug"),
        dxs_id=251658753,
    ),

    # Home consumption Total
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_home_consumption_total",
            name="Kostal PIKO Home Consumption Total",
            device_class=SensorDeviceClass.ENERGY,
            state_class=SensorStateClass.TOTAL_INCREASING,
            native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
            icon="mdi:power-plug"),
        dxs_id=251659009,
    ),

    # Own consumption Total
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_own_consumption_total",
            name="Kostal PIKO Own Consumption Total",
            device_class=SensorDeviceClass.ENERGY,
            state_class=SensorStateClass.TOTAL_INCREASING,
            native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
            icon="mdi:power-plug"),
        dxs_id=251659265,
    ),

    # Own consumption quota Total
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_own_consumption_quota_total",
            name="Kostal PIKO Own Consumption Quota Total",
            device_class=None,
            state_class=SensorStateClass.TOTAL_INCREASING,
            native_unit_of_measurement=PERCENTAGE,
            icon="mdi:power-plug"),
        dxs_id=251659280,
    ),

    # Autarky Total
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_autarky_total",
            name="Kostal PIKO Autarky Total",
            device_class=None,
            state_class=SensorStateClass.TOTAL_INCREASING,
            native_unit_of_measurement=PERCENTAGE,
            icon="mdi:power-plug"),
        dxs_id=251659281,
    ),

    # Inverter state
    # (0  = off, 1 = idle, 2 = starting, DC too low, 3 = input (MPP), 4 = input limited)
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_inverter_state",
            name="Kostal PIKO Inverter State",
            device_class=None,
            state_class=SensorStateClass.MEASUREMENT,
            native_unit_of_measurement=None,
            icon="mdi:power-plug"),
        dxs_id=16780032,
    ),

    # Uptime
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_uptime",
            name="Kostal PIKO Uptime",
            device_class=None,
            state_class=SensorStateClass.MEASUREMENT,
            native_unit_of_measurement=TIME_HOURS,
            icon="mdi:power-plug"),
        dxs_id=251658496,
    ),

    # Current Home consumption solar
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_home_consumption_solar",
            name="Kostal PIKO Home Consumption Solar",
            device_class=SensorDeviceClass.POWER,
            state_class=SensorStateClass.MEASUREMENT,
            native_unit_of_measurement=POWER_WATT,
            icon="mdi:power-plug"),
        dxs_id=83886336,
    ),

    # Current Home consumption battery
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_home_consumption_battery",
            name="Kostal PIKO Home Consumption Battery",
            device_class=SensorDeviceClass.POWER,
            state_class=SensorStateClass.MEASUREMENT,
            native_unit_of_measurement=POWER_WATT,
            icon="mdi:power-plug"),
        dxs_id=83886592,
    ),

    # Current Home consumption grid
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_home_consumption_grid",
            name="Kostal PIKO Home Consumption Grid",
            device_class=SensorDeviceClass.POWER,
            state_class=SensorStateClass.MEASUREMENT,
            native_unit_of_measurement=POWER_WATT,
            icon="mdi:power-plug"),
        dxs_id=83886848,
    ),

    # Current Home consumption phase 1
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_home_consumption_phase_1",
            name="Kostal PIKO Home Consumption Phase 1",
            device_class=SensorDeviceClass.POWER,
            state_class=SensorStateClass.MEASUREMENT,
            native_unit_of_measurement=POWER_WATT,
            icon="mdi:power-plug"),
        dxs_id=83887106,
    ),

    # Current Home consumption phase 2
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_home_consumption_phase_2",
            name="Kostal PIKO Home Consumption Phase 2",
            device_class=SensorDeviceClass.POWER,
            state_class=SensorStateClass.MEASUREMENT,
            native_unit_of_measurement=POWER_WATT,
            icon="mdi:power-plug"),
        dxs_id=83887362,
    ),

    # Current Home consumption phase 3
    KostalPikoSensorEntityDescription(
        description=SensorEntityDescription(
            key="kostal_piko_home_consumption_phase_3",
            name="Kostal PIKO Home Consumption Phase 3",
            device_class=SensorDeviceClass.POWER,
            state_class=SensorStateClass.MEASUREMENT,
            native_unit_of_measurement=POWER_WATT,
            icon="mdi:power-plug"),
        dxs_id=83887618,
    ))

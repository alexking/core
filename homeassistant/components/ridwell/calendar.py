import datetime
from typing import Union

from homeassistant.components.calendar import CalendarEntity, CalendarEvent
from homeassistant.components.ridwell import RidwellEntity
from homeassistant.components.sensor import SensorDeviceClass, SensorEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DATA_ACCOUNT, DATA_COORDINATOR, DOMAIN, SENSOR_TYPE_SCHEDULE_PICKUPS

SENSOR_DESCRIPTION = SensorEntityDescription(
    key=SENSOR_TYPE_SCHEDULE_PICKUPS,
    name="Ridwell pickup",
    device_class=SensorDeviceClass.DATE,
)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Set up Ridwell sensors based on a config entry."""
    accounts = hass.data[DOMAIN][entry.entry_id][DATA_ACCOUNT]
    coordinator = hass.data[DOMAIN][entry.entry_id][DATA_COORDINATOR]

    async_add_entities(
        [
            RidwellCalendar(coordinator, account, SENSOR_DESCRIPTION)
            for account in accounts.values()
        ]
    )


class RidwellCalendar(RidwellEntity, CalendarEntity):
    """Provide calendar evenhts indicating opted-in Ridwell pickups"""

    @property
    def event(self) -> CalendarEvent | None:
        """Return the next upcoming event."""
        return CalendarEvent(
            description="pickup",
            start=datetime.date(2022, 7, 16),
            end=datetime.date(2022, 7, 16),
            location="test",
            summary="test",
        )

    async def async_get_events(
        self,
        hass: HomeAssistant,
        start_date: datetime.datetime,
        end_date: datetime.datetime,
    ) -> list[CalendarEvent]:
        """Return calendar events within a datetime range."""
        return [
            CalendarEvent(
                description="pickup",
                start=datetime.date(2022, 7, 16),
                end=datetime.date(2022, 7, 16),
                location="test",
                summary="test",
            )
        ]

from abc import ABC, abstractmethod
from dataclasses import dataclass

from alerts.domain.alert import AlertId
from shared.domain.coords import Coords


@dataclass
class AlertNewMissingPetEvent:
    alert_id : AlertId
    coords : Coords


class AlertHandler(ABC):

    @abstractmethod
    async def handle(self, alert : AlertNewMissingPetEvent) -> None:
        #Maneja el evento de una nueva mascota reportada desaparecida
        pass
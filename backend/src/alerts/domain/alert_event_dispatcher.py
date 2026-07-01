from alerts.domain.alert_handler import AlertHandler, AlertNewMissingPetEvent


# Nota importante: Sólo hay un tipo de evento: El reporte de una mascota desaparecida
class AlertNewMissingPetSubject:

    suscribers : list[AlertHandler]

    def __init__(self) -> None:
        self.suscribers = []

    async def attach( self, handler : AlertHandler):
        self.suscribers.append(handler)

    async def dettach( self, handler : AlertHandler ):
        self.suscribers.remove(handler)

    async def notify(self, event : AlertNewMissingPetEvent):
        for handler in self.suscribers:
            await handler.handle( event )


import {
  Box,
  Button,
  Checkbox,
  Flex,
  Heading,
  Input,
  Select,
  Stack,
  Switch,
  Text,
  Textarea,
} from "@chakra-ui/react";
import { useEffect, useState } from "react";
import { LuBell, LuPlus, LuUsers } from "react-icons/lu";
import { useNavigate, useParams } from "react-router";
import Header from "../components/Header";
import Sidebar from "../components/Sidebar";
import type { NavItem, Notification, User } from "../types/layout";

const NAV_ITEMS: NavItem[] = [
  { label: "Reportar mascota", icon: LuPlus },
  { label: "Alertas activas", icon: LuBell },
  { label: "Red de cuidadores", icon: LuUsers },
];

const normalizeRole = (role: string) => {
  switch (role) {
    case "Cuidador Solidario":
      return "SOLIDARIO";
    case "Profesional":
      return "PROFESIONAL";
    case "Especializado":
      return "ESPECIALIZADO";
    case "SOLIDARIO":
    case "PROFESIONAL":
    case "ESPECIALIZADO":
      return role;
    default:
      return "SOLIDARIO";
  }
};

const EMPTY_USER: User = { id: 0, name: "", email: "example@example.com", role: "SOLIDARIO" };
const EMPTY_REPORT = {
  nombre: "",
  especie: "",
  raza: "",
  imagen: "",
  descripcion: "",
  long: "",
  lat: "",
};

export default function HomePage() {
  const navigate = useNavigate();
  const { id } = useParams();

  const [currUser, setCurrUser] = useState<User>(EMPTY_USER);
  const [active, setActive] = useState("Reportar mascota");
  const [notifications, setNotifications] = useState<Notification[]>([]);
  const [loadingNotifications, setLoadingNotifications] = useState(false);
  const [notificationError, setNotificationError] = useState<string | null>(null);
  const [reportData, setReportData] = useState({ ...EMPTY_REPORT });
  const [reportMessage, setReportMessage] = useState<string>("");
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [caregiverRole, setCaregiverRole] = useState("SOLIDARIO");
  const [speciesAccepted, setSpeciesAccepted] = useState<string[]>(["Perro", "Gato"]);
  const [sizesAccepted, setSizesAccepted] = useState<string[]>(["Pequeño", "Mediano"]);
  const [medicationsAccepted, setMedicationsAccepted] = useState(false);
  const [receiveAlerts, setReceiveAlerts] = useState(true);
  const [caregiverMessage, setCaregiverMessage] = useState<string>("");
  const [ratingAverage] = useState(4.5);

  useEffect(() => {
    const storedRole = localStorage.getItem("caregiver_role");
    if (storedRole) setCaregiverRole(normalizeRole(storedRole));

    const storedSpecies = localStorage.getItem("caregiver_species");
    if (storedSpecies) setSpeciesAccepted(JSON.parse(storedSpecies));

    const storedSizes = localStorage.getItem("caregiver_sizes");
    if (storedSizes) setSizesAccepted(JSON.parse(storedSizes));

    const storedMedications = localStorage.getItem("caregiver_medications");
    if (storedMedications) setMedicationsAccepted(storedMedications === "true");

    const storedReceiveAlerts = localStorage.getItem("caregiver_receive_alerts");
    if (storedReceiveAlerts) setReceiveAlerts(storedReceiveAlerts === "true");
  }, []);

  const buildHeaders = () => {
    const token = localStorage.getItem("access_token");
    return {
      "Content-Type": "application/json",
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    };
  };

  const toggleArrayValue = (list: string[], value: string) => {
    if (list.includes(value)) {
      return list.filter((item) => item !== value);
    }
    return [...list, value];
  };

  const handleSaveCaregiverSettings = () => {
    localStorage.setItem("caregiver_role", caregiverRole);
    localStorage.setItem("caregiver_species", JSON.stringify(speciesAccepted));
    localStorage.setItem("caregiver_sizes", JSON.stringify(sizesAccepted));
    localStorage.setItem("caregiver_medications", String(medicationsAccepted));
    localStorage.setItem("caregiver_receive_alerts", String(receiveAlerts));
    setCaregiverMessage("Configuración de cuidador guardada correctamente.");
  };

  const clearSessionAndRedirect = () => {
    localStorage.removeItem("access_token");
    localStorage.removeItem("token_type");
    navigate("/login");
  };

  const handleAuthError = (status: number) => {
    if (status === 401 || status === 403) {
      clearSessionAndRedirect();
      return true;
    }
    return false;
  };

  useEffect(() => {
    if (!id) {
      navigate("/login");
      return;
    }

    const userId = Number(id);
    if (Number.isNaN(userId)) {
      navigate("/login");
      return;
    }

    const token = localStorage.getItem("access_token");
    if (!token) {
      navigate("/login");
      return;
    }

    fetch(`http://localhost:8000/api/users/${userId}`, {
      method: "GET",
      headers: buildHeaders(),
    })
      .then((res) => {
        if (!res.ok) {
          if (handleAuthError(res.status)) throw new Error("Token expirado");
          throw new Error(`HTTP ${res.status}`);
        }
        return res.json();
      })
      .then((res) => setCurrUser({ id: res.id, name: res.name, email: res.email, role: normalizeRole(res.role ?? "SOLIDARIO") }))
      .catch((err) => {
        console.error(err);
        navigate("/login");
      });
  }, [id, navigate]);

  useEffect(() => {
    if (active !== "Alertas activas" || currUser.id === 0) return;

    setLoadingNotifications(true);
    setNotificationError(null);

    const token = localStorage.getItem("access_token");
    if (!token) {
      setNotificationError("Debe iniciar sesión para ver las alertas.");
      setLoadingNotifications(false);
      return;
    }

    fetch(`http://localhost:8000/api/users/notification/${currUser.id}`, {
      method: "GET",
      headers: buildHeaders(),
    })
      .then((res) => {
        if (!res.ok) {
          if (handleAuthError(res.status)) throw new Error("Token expirado");
          throw new Error(`HTTP ${res.status}`);
        }
        return res.json();
      })
      .then((res) => setNotifications(res))
      .catch((err) => {
        console.error(err);
        if (!notificationError) {
          setNotificationError("No se pudieron cargar las alertas.");
        }
      })
      .finally(() => setLoadingNotifications(false));
  }, [active, currUser.id]);

  const handleReportSubmit = async () => {
    if (
      !reportData.nombre ||
      !reportData.especie ||
      !reportData.raza ||
      !reportData.imagen ||
      !reportData.descripcion ||
      !reportData.lat ||
      !reportData.long
    ) {
      setReportMessage("Complete todos los campos antes de enviar el reporte.");
      return;
    }

    setIsSubmitting(true);
    setReportMessage("");

    const token = localStorage.getItem("access_token");

    try {
      const res = await fetch("http://localhost:8000/api/alerts/", {
        method: "POST",
        headers: buildHeaders(),
        body: JSON.stringify({
          name: reportData.nombre,
          specie: reportData.especie,
          breed: reportData.raza,
          image: reportData.imagen,
          description: reportData.descripcion,
          long: Number(reportData.long),
          lat: Number(reportData.lat),
        }),
      });

      if (!res.ok) {
        if (handleAuthError(res.status)) {
          setReportMessage("Su sesión expiró. Inicie sesión nuevamente.");
          return;
        }
        const errorText = await res.text();
        throw new Error(errorText || "Error al enviar el reporte.");
      }

      setReportMessage(`Reporte de ${reportData.nombre || "la mascota"} creado correctamente.`);
      setReportData({ ...EMPTY_REPORT });
    } catch (error) {
      console.error(error);
      setReportMessage("No se pudo enviar el reporte. Verifique los datos e intente nuevamente.");
    } finally {
      setIsSubmitting(false);
    }
  };

  const renderReportForm = () => (
    <Box maxW="700px" p={6} bg="white" borderWidth="1px" borderColor="gray.200" borderRadius="md">
      <Stack spacing={4}>
        <Text color="gray.600">Complete los datos de la mascota perdida para crear un reporte.</Text>

        <Box>
          <Text mb={2} fontWeight="semibold">
            Nombre de la mascota
          </Text>
          <Input
            placeholder="Nombre"
            value={reportData.nombre}
            onChange={(e) => setReportData({ ...reportData, nombre: e.target.value })}
          />
        </Box>

        <Box>
          <Text mb={2} fontWeight="semibold">
            Especie
          </Text>
          <select
            style={{
              width: "100%",
              padding: "12px 14px",
              borderRadius: "12px",
              border: "1px solid #cbd5e1",
              fontSize: "16px",
              background: "#ffffff",
            }}
            value={reportData.especie}
            onChange={(e) => setReportData({ ...reportData, especie: e.target.value })}
          >
            <option value="">Seleccione una especie</option>
            <option value="DOG">Perro</option>
            <option value="CAT">Gato</option>
            <option value="BIRD">Ave</option>
          </select>
        </Box>

        <Box>
          <Text mb={2} fontWeight="semibold">
            Raza
          </Text>
          <Input
            placeholder="Raza"
            value={reportData.raza}
            onChange={(e) => setReportData({ ...reportData, raza: e.target.value })}
          />
        </Box>

        <Box>
          <Text mb={2} fontWeight="semibold">
            Imagen (URL)
          </Text>
          <Input
            placeholder="https://..."
            value={reportData.imagen}
            onChange={(e) => setReportData({ ...reportData, imagen: e.target.value })}
          />
        </Box>

        <Box>
          <Text mb={2} fontWeight="semibold">
            Longitud
          </Text>
          <Input
            placeholder="-58.12345"
            value={reportData.long}
            onChange={(e) => setReportData({ ...reportData, long: e.target.value })}
          />
        </Box>

        <Box>
          <Text mb={2} fontWeight="semibold">
            Latitud
          </Text>
          <Input
            placeholder="-34.12345"
            value={reportData.lat}
            onChange={(e) => setReportData({ ...reportData, lat: e.target.value })}
          />
        </Box>

        <Box>
          <Text mb={2} fontWeight="semibold">
            Descripción
          </Text>
          <Textarea
            placeholder="Descripción del incidente, comportamiento, características..."
            value={reportData.descripcion}
            onChange={(e) => setReportData({ ...reportData, descripcion: e.target.value })}
            minH="140px"
          />
        </Box>

        <Button colorPalette="blue" size="md" width="full" onClick={handleReportSubmit} isLoading={isSubmitting}>
          Enviar reporte
        </Button>

        {reportMessage ? <Text color="gray.700">{reportMessage}</Text> : null}
      </Stack>
    </Box>
  );

  const renderCaregiverNetwork = () => (
    <Box maxW="760px" p={6} bg="white" borderWidth="1px" borderColor="gray.200" borderRadius="md">
      <Stack spacing={5}>
        <Text color="gray.600">
          Configura tu perfil de cuidador para recibir alertas y mostrar tu calificación.
        </Text>

        <Box>
          <Text mb={2} fontWeight="semibold">
            Rol del cuidador
          </Text>
          <Select value={caregiverRole} onChange={(e) => setCaregiverRole(e.target.value)}>
            <option value="SOLIDARIO">Cuidador Solidario</option>
            <option value="PROFESIONAL">Profesional</option>
            <option value="ESPECIALIZADO">Especializado</option>
          </Select>
        </Box>

        <Box>
          <Text mb={2} fontWeight="semibold">
            Especies aceptadas
          </Text>
          <Stack direction={{ base: "column", md: "row" }} spacing={3}>
            {[
              { label: "Perro", value: "Perro" },
              { label: "Gato", value: "Gato" },
              { label: "Otro", value: "Otro" },
            ].map((option) => (
              <Checkbox
                key={option.value}
                isChecked={speciesAccepted.includes(option.value)}
                onChange={() => setSpeciesAccepted(toggleArrayValue(speciesAccepted, option.value))}
              >
                {option.label}
              </Checkbox>
            ))}
          </Stack>
        </Box>

        <Box>
          <Text mb={2} fontWeight="semibold">
            Tamaños aceptados
          </Text>
          <Stack direction={{ base: "column", md: "row" }} spacing={3}>
            {[
              { label: "Pequeño", value: "Pequeño" },
              { label: "Mediano", value: "Mediano" },
              { label: "Grande", value: "Grande" },
            ].map((option) => (
              <Checkbox
                key={option.value}
                isChecked={sizesAccepted.includes(option.value)}
                onChange={() => setSizesAccepted(toggleArrayValue(sizesAccepted, option.value))}
              >
                {option.label}
              </Checkbox>
            ))}
          </Stack>
        </Box>

        <Box>
          <Text mb={2} fontWeight="semibold">
            Administración de medicamentos
          </Text>
          <Switch
            isChecked={medicationsAccepted}
            onChange={(e) => setMedicationsAccepted(e.target.checked)}
          />
        </Box>

        <Box>
          <Text mb={2} fontWeight="semibold">
            Recibir alertas de mascotas perdidas
          </Text>
          <Switch
            isChecked={receiveAlerts}
            onChange={(e) => setReceiveAlerts(e.target.checked)}
          />
        </Box>

        <Box bg="gray.50" p={4} borderRadius="md">
          <Text color="gray.500" fontSize="sm">
            Calificación promedio del cuidador
          </Text>
          <Heading size="md" mt={2}>{ratingAverage.toFixed(1)} / 5</Heading>
        </Box>

        <Button colorPalette="blue" size="md" width="full" onClick={handleSaveCaregiverSettings}>
          Guardar configuración
        </Button>

        {caregiverMessage ? <Text color="green.600">{caregiverMessage}</Text> : null}
      </Stack>
    </Box>
  );

  const renderActiveAlerts = () => (
    <Box p={4} bg="white" borderWidth="1px" borderColor="gray.200" borderRadius="md">
      <Text color="gray.600" mb={4}>
        Las alertas activas se muestran como tarjetas desplazables.
      </Text>

      {loadingNotifications ? (
        <Text>Cargando alertas...</Text>
      ) : notificationError ? (
        <Text color="red.600">{notificationError}</Text>
      ) : (
        <Flex gap={4} overflowX="auto" pb={2}>
          {notifications.length > 0 ? (
            notifications.map((notification) => (
              <Box
                key={notification.alert_id}
                minW="280px"
                flex="0 0 auto"
                p={4}
                bg="gray.50"
                borderWidth="1px"
                borderColor="gray.200"
                borderRadius="md"
              >
                <Text fontSize="xs" color="gray.500">
                  Alerta #{notification.alert_id}
                </Text>
                <Heading size="sm" mt={2} mb={3}>
                  Notificación
                </Heading>
                <Text color="gray.700">{notification.text}</Text>
              </Box>
            ))
          ) : (
            <Box minW="320px" flex="0 0 auto" p={4} bg="gray.50" borderWidth="1px" borderColor="gray.200" borderRadius="md">
              <Text color="gray.600">No hay alertas activas en este momento.</Text>
            </Box>
          )}
        </Flex>
      )}
    </Box>
  );

  return (
    <Flex minH="100vh" flexDir="column">
      <Header user={currUser} />
      <Flex flex={1} overflow="hidden">
        <Sidebar navItems={NAV_ITEMS} active={active} onNavigate={setActive} user={currUser} />
        <Box flex={1} bg="gray.50" p={8} overflowY="auto">
          <Heading size="lg" mb={2} color="gray.800">
            {active}
          </Heading>
          <Text color="gray.500" mb={6}>
            Bienvenido, {currUser.name || "usuario"}. Selecciona una opción en el menú.
          </Text>
          {active === "Reportar mascota" && renderReportForm()}
          {active === "Alertas activas" && renderActiveAlerts()}
          {active === "Red de cuidadores" && renderCaregiverNetwork()}
        </Box>
      </Flex>
    </Flex>
  );
}
